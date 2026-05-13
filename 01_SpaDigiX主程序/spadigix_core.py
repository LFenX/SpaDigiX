from dataclasses import dataclass
from functools import lru_cache
import calendar
import datetime
import math

from ephem import Date, Ecliptic, Equatorial, Sun
from zhdate import ZhDate


TIANGAN = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
DIZHI = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
SHENGXIAO = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
YUE_DIZHI = ["寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥", "子", "丑"]

_DIZHI_INDEX = {ch: i for i, ch in enumerate(DIZHI)}

SIXTY_GANZHI = [
    "甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己巳", "庚午", "辛未", "壬申", "癸酉",
    "甲戌", "乙亥", "丙子", "丁丑", "戊寅", "己卯", "庚辰", "辛巳", "壬午", "癸未",
    "甲申", "乙酉", "丙戌", "丁亥", "戊子", "己丑", "庚寅", "辛卯", "壬辰", "癸巳",
    "甲午", "乙未", "丙申", "丁酉", "戊戌", "己亥", "庚子", "辛丑", "壬寅", "癸卯",
    "甲辰", "乙巳", "丙午", "丁未", "戊申", "己酉", "庚戌", "辛亥", "壬子", "癸丑",
    "甲寅", "乙卯", "丙辰", "丁巳", "戊午", "己未", "庚申", "辛酉", "壬戌", "癸亥",
]

SOLAR_TERMS = [
    "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种", "夏至",
    "小暑", "大暑", "立秋", "处暑", "白露", "秋分", "寒露", "霜降", "立冬", "小雪",
    "大雪", "冬至", "小寒", "大寒",
]

LUNAR_MONTH_TEXT_TO_NUMBER = {
    "一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6,
    "七": 7, "八": 8, "九": 9, "十": 10, "十一": 11, "十二": 12,
}
LUNAR_DAY_TEXT_TO_NUMBER = {
    "初一": 1, "初二": 2, "初三": 3, "初四": 4, "初五": 5,
    "初六": 6, "初七": 7, "初八": 8, "初九": 9, "初十": 10,
    "十一": 11, "十二": 12, "十三": 13, "十四": 14, "十五": 15,
    "十六": 16, "十七": 17, "十八": 18, "十九": 19, "二十": 20,
    "廿一": 21, "廿二": 22, "廿三": 23, "廿四": 24, "廿五": 25,
    "廿六": 26, "廿七": 27, "廿八": 28, "廿九": 29, "三十": 30,
}

_JIEQI_LIST_25 = (
    "冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨",
    "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑", "白露",
    "秋分", "寒露", "霜降", "立冬", "小雪", "大雪", "冬至", "小寒",
)

_JIEQI_YEAR_TERMS_INDEX = {
    term: idx
    for idx, term in enumerate((
        "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨",
        "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑",
        "白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪", "冬至",
    ))
}


def _make_jieqi_month_number():
    order = (
        "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种",
        "夏至", "小暑", "大暑", "立秋", "处暑", "白露", "秋分", "寒露", "霜降",
        "立冬", "小雪", "大雪", "冬至", "小寒", "大寒",
    )
    result = {}
    for i, term in enumerate(order):
        result[term] = (i + 2) // 2 if i % 2 == 0 else (i + 1) // 2
    return result


_JIEQI_MONTH_NUMBER = _make_jieqi_month_number()

_MONTH_TIANGAN_BY_STEM = {}
for _stems, _seq in (
    (("甲", "己"), ("丙", "丁", "戊", "己", "庚", "辛", "壬", "癸", "甲", "乙")),
    (("乙", "庚"), ("戊", "己", "庚", "辛", "壬", "癸", "甲", "乙", "丙", "丁")),
    (("丙", "辛"), ("庚", "辛", "壬", "癸", "甲", "乙", "丙", "丁", "戊", "己")),
    (("丁", "壬"), ("壬", "癸", "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛")),
    (("戊", "癸"), ("甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸")),
):
    for _stem in _stems:
        _MONTH_TIANGAN_BY_STEM[_stem] = _seq

_HOUR_TIANGAN_BY_STEM = {}
for _stems, _seq in (
    (("甲", "己"), ("甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸")),
    (("乙", "庚"), ("丙", "丁", "戊", "己", "庚", "辛", "壬", "癸", "甲", "乙")),
    (("丙", "辛"), ("戊", "己", "庚", "辛", "壬", "癸", "甲", "乙", "丙", "丁")),
    (("丁", "壬"), ("庚", "辛", "壬", "癸", "甲", "乙", "丙", "丁", "戊", "己")),
    (("戊", "癸"), ("壬", "癸", "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛")),
):
    for _stem in _stems:
        _HOUR_TIANGAN_BY_STEM[_stem] = _seq

_DAY_GANZHI_TIANGAN_OFFSETS = (-1, 0, -2, -1, -1, 0, 0, 1, 2, 2, 3, 3)
_DAY_GANZHI_DIZHI_OFFSETS = (-1, 6, 10, 5, -1, 6, 0, 7, 2, 8, 3, 9)

_YANG_JIEQI = frozenset({
    "冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种",
})

_SHANG_YUAN_DAYS = frozenset({
    "甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己卯", "庚辰", "辛巳", "壬午", "癸未",
    "甲午", "乙未", "丙申", "丁酉", "戊戌", "己酉", "庚戌", "辛亥", "壬子", "癸丑",
})
_ZHONG_YUAN_DAYS = frozenset({
    "己巳", "庚午", "辛未", "壬申", "癸酉", "甲申", "乙酉", "丙戌", "丁亥", "戊子",
    "己亥", "庚子", "辛丑", "壬寅", "癸卯", "甲寅", "乙卯", "丙辰", "丁巳", "戊午",
})

_QIJU_TABLE = {
    # 阳遁
    "冬至上元": "坎一", "冬至中元": "兑七", "冬至下元": "巽四",
    "小寒上元": "坤二", "小寒中元": "艮八", "小寒下元": "中五",
    "大寒上元": "震三", "大寒中元": "离九", "大寒下元": "乾六",
    "立春上元": "艮八", "立春中元": "中五", "立春下元": "坤二",
    "雨水上元": "离九", "雨水中元": "乾六", "雨水下元": "震三",
    "惊蛰上元": "坎一", "惊蛰中元": "兑七", "惊蛰下元": "巽四",
    "春分上元": "震三", "春分中元": "离九", "春分下元": "乾六",
    "清明上元": "巽四", "清明中元": "坎一", "清明下元": "兑七",
    "谷雨上元": "中五", "谷雨中元": "坤二", "谷雨下元": "艮八",
    "立夏上元": "巽四", "立夏中元": "坎一", "立夏下元": "兑七",
    "小满上元": "中五", "小满中元": "坤二", "小满下元": "艮八",
    "芒种上元": "乾六", "芒种中元": "震三", "芒种下元": "离九",
    # 阴遁
    "夏至上元": "离九", "夏至中元": "震三", "夏至下元": "乾六",
    "小暑上元": "艮八", "小暑中元": "坤二", "小暑下元": "中五",
    "大暑上元": "兑七", "大暑中元": "坎一", "大暑下元": "巽四",
    "立秋上元": "坤二", "立秋中元": "中五", "立秋下元": "艮八",
    "处暑上元": "坎一", "处暑中元": "巽四", "处暑下元": "兑七",
    "白露上元": "离九", "白露中元": "震三", "白露下元": "乾六",
    "秋分上元": "兑七", "秋分中元": "坎一", "秋分下元": "巽四",
    "寒露上元": "乾六", "寒露中元": "离九", "寒露下元": "震三",
    "霜降上元": "中五", "霜降中元": "艮八", "霜降下元": "坤二",
    "立冬上元": "乾六", "立冬中元": "离九", "立冬下元": "震三",
    "小雪上元": "中五", "小雪中元": "艮八", "小雪下元": "坤二",
    "大雪上元": "巽四", "大雪中元": "兑七", "大雪下元": "坎一",
}

_GONGHAO = {"坎一": 0, "坤二": 1, "震三": 2, "巽四": 3, "中五": 4, "乾六": 5, "兑七": 6, "艮八": 7, "离九": 8}
_SANQI = ("甲子戊", "甲戌己", "甲申庚", "甲午辛", "甲辰壬", "甲寅癸", "　丁　", "　丙　", "　乙　")

_ZHUANGDONG = (0, 7, 2, 3, 8, 1, 6, 5)
_ZHUANGDONG_INDEX = {v: i for i, v in enumerate(_ZHUANGDONG)}

_BASHEN_YANG = ("值符", "螣蛇", "太阴", "六合", "白虎", "玄武", "九地", "九天")
_BASHEN_YIN = ("值符", "九天", "九地", "玄武", "白虎", "六合", "太阴", "螣蛇")
_JIUXING = ("天蓬", "天芮", "天冲", "天辅", "天禽", "天心", "天柱", "天任", "天英")
_BAMEN = ("休", "生", "伤", "杜", "景", "死", "惊", "开")


def _make_xun_by_hour():
    xun_lists = (
        ("甲子戊", "甲子", ("甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己巳", "庚午", "辛未", "壬申", "癸酉")),
        ("甲戌己", "甲戌", ("甲戌", "乙亥", "丙子", "丁丑", "戊寅", "己卯", "庚辰", "辛巳", "壬午", "癸未")),
        ("甲申庚", "甲申", ("甲申", "乙酉", "丙戌", "丁亥", "戊子", "己丑", "庚寅", "辛卯", "壬辰", "癸巳")),
        ("甲午辛", "甲午", ("甲午", "乙未", "丙申", "丁酉", "戊戌", "己亥", "庚子", "辛丑", "壬寅", "癸卯")),
        ("甲辰壬", "甲辰", ("甲辰", "乙巳", "丙午", "丁未", "戊申", "己酉", "庚戌", "辛亥", "壬子", "癸丑")),
        ("甲寅癸", "甲寅", ("甲寅", "乙卯", "丙辰", "丁巳", "戊午", "己未", "庚申", "辛酉", "壬戌", "癸亥")),
    )
    result = {}
    for xuntou, xuntouzi, members in xun_lists:
        for hour_gz in members:
            result[hour_gz] = (xuntou, xuntouzi, members)
    return result


_XUN_BY_HOUR = _make_xun_by_hour()


def _make_laoda_by_hour():
    # 复刻 _xun_info 内 sanqiliuyilaoda 分支：
    # hour_gz[0] == '甲' 时按 [甲子,甲戌,甲申,甲午,甲辰,甲寅] 顺序映射到 _SANQI[0..5]
    # 否则按 [戊,己,庚,辛,壬,癸,丁,丙,乙] 顺序映射到 _SANQI[0..8]
    jia_keys = ("甲子", "甲戌", "甲申", "甲午", "甲辰", "甲寅")
    other_stems = ("戊", "己", "庚", "辛", "壬", "癸", "丁", "丙", "乙")
    result = {}
    for i, gz in enumerate(jia_keys):
        result[gz] = _SANQI[i]
    # 60 干支里所有非"甲子/甲戌/甲申/甲午/甲辰/甲寅"的，按首字天干查 _SANQI
    for gz in SIXTY_GANZHI:
        if gz in result:
            continue
        result[gz] = _SANQI[other_stems.index(gz[0])]
    return result


_LAODA_BY_HOUR = _make_laoda_by_hour()

_OUTPUT_PREFIXES = (
    (0, "output_2_1"),
    (1, "output_0_2"),
    (2, "output_1_0"),
    (3, "output_0_0"),
    (4, "output_1_1"),
    (5, "output_2_2"),
    (6, "output_1_2"),
    (7, "output_2_0"),
    (8, "output_0_1"),
)


@dataclass
class ChartResult:
    header_text: str
    info_text: str
    output_boxes: dict
    year_ganzhi: str
    month_ganzhi: str
    day_ganzhi: str
    hour_ganzhi: str
    jieqi: str
    yinyang_dun: str
    yuanri: str
    qiju: str
    xuntou: str


def build_chart_from_solar(year, month, day, hour, minute):
    year = int(year)
    month = int(month)
    day = int(day)
    hour = int(hour)
    minute = int(minute)

    nianfen = "闰年" if calendar.isleap(year) else "平年"
    lunar_date = ZhDate.from_datetime(datetime.datetime(year, month, day))
    shengxiaonian = SHENGXIAO[(int(lunar_date.lunar_year) - 1900) % 12]
    jieqi = _solar_term_for_date(year, month, day)
    year_gz, month_gz, day_gz, hour_gz = _ganzhi_from_solar(year, month, day, hour, jieqi)

    return _build_chart(
        year_gz=year_gz,
        month_gz=month_gz,
        day_gz=day_gz,
        hour_gz=hour_gz,
        jieqi=jieqi,
        info_text=f"你输入的时间是：{year}年{month}月{day}日{hour}时{minute}分",
        header_text=(
            f" {year_gz}年(属{shengxiaonian},{nianfen})\t{month_gz}月\t"
            f"{day_gz}日\t{hour_gz}时\t{jieqi}\t{{yinyang_dun}}\t{{yuanri}}日"
        ),
    )


def build_chart_from_lunar_date(year, lunar_month, lunar_day, hour, minute):
    solar_date = ZhDate(int(year), int(lunar_month), int(lunar_day)).to_datetime()
    return build_chart_from_solar(solar_date.year, solar_date.month, solar_date.day, int(hour), int(minute))


def fields_for_lunar_input_button(year, month, day, hour):
    """复刻原始主程序"获取当前时间.阴"按钮的五字段填充。

    与 build_chart_from_solar 的差异：年干支取 lunar_year，而非节气调整后的太阳年。
    其余字段（月/日/时干支与节气）均与 _ganzhi_from_solar 等价。
    返回 (年干支, 月干支, 日干支, 时干支, 节气) 五元字符串组。
    """
    year = int(year)
    month = int(month)
    day = int(day)
    hour = int(hour)
    lunar = ZhDate.from_datetime(datetime.datetime(year, month, day))
    ly = int(lunar.lunar_year)
    year_tg = TIANGAN[(ly - 4) % 10]
    year_dz = DIZHI[(ly - 4) % 12]
    jieqi = _solar_term_for_date(year, month, day, hour, 0)
    month_num = _JIEQI_MONTH_NUMBER[jieqi]
    month_tg = _MONTH_TIANGAN_BY_STEM[year_tg][(month_num - 1) % 10]
    month_dz = YUE_DIZHI[month_num - 1]
    day_tg, day_dz = _day_ganzhi(year, month, day)
    hour_dz = _hour_dizhi(hour)
    hour_tg = _HOUR_TIANGAN_BY_STEM[day_tg][_DIZHI_INDEX[hour_dz] % 10]
    return (
        f"{year_tg}{year_dz}",
        f"{month_tg}{month_dz}",
        f"{day_tg}{day_dz}",
        f"{hour_tg}{hour_dz}",
        jieqi,
    )


def build_chart_from_ganzhi(year_gz, month_gz, day_gz, hour_gz, jieqi):
    return _build_chart(
        year_gz=year_gz,
        month_gz=month_gz,
        day_gz=day_gz,
        hour_gz=hour_gz,
        jieqi=jieqi,
        info_text=f"你输入的时间是：{year_gz}年{month_gz}月{day_gz}日{hour_gz}时{jieqi}",
        header_text=(
            f" {year_gz}年\t{month_gz}月\t{day_gz}日\t{hour_gz}时\t"
            f"{jieqi}\t{{yinyang_dun}}\t{{yuanri}}日"
        ),
    )


@lru_cache(maxsize=256)
def _year_jieqi_boundaries(year):
    """返回该年的 26 个节气分界点（含跨年），结果按年缓存。

    与原始 jq(year) 完全等价：以 (year-1, 12, 15) 为起点二分迭代，每个边界
    再加 1/3 天平移并截取到小时。
    """
    def ecliptic_lon(jd_utc):
        sun = Sun(jd_utc)
        equ = Equatorial(sun.ra, sun.dec, epoch=jd_utc)
        return Ecliptic(equ).lon

    def sta(jd):
        return int(ecliptic_lon(jd) * 180.0 / math.pi / 15)

    def iteration(jd):
        s1 = sta(jd)
        s0 = s1
        dt = datetime.timedelta(days=1.0)
        while True:
            jd += dt
            s = sta(jd)
            if s0 != s:
                s0 = s
                dt = -dt / 2
            if abs(dt.total_seconds()) < 0.0000001 and s != s1:
                break
        return jd

    jd = datetime.datetime(year - 1, 12, 15, 0, 0, 0)
    n = int(ecliptic_lon(jd) * 180.0 / math.pi / 15) + 1
    boundaries = []
    third_day = datetime.timedelta(days=1 / 3)
    for _ in range(26):
        if n >= 24:
            n -= 24
        jd = iteration(jd)
        d = Date(jd + third_day).tuple()
        boundaries.append(datetime.datetime(d[0], d[1], d[2], d[3], 0, 0))
        n += 1
    return tuple(boundaries)


def _solar_term_for_date(year, month, day, hour=23, minute=59):
    boundaries = _year_jieqi_boundaries(year)
    v = datetime.datetime(year, month, day, hour, minute, 0)
    jieqi_index = 0
    for i in range(25):
        if boundaries[i] <= v <= boundaries[i + 1]:
            jieqi_index = i
            break
    return _JIEQI_LIST_25[jieqi_index]


def _ganzhi_from_solar(year, month, day, hour, jieqi):
    ganzhi_year = year
    jieqi_index = _JIEQI_YEAR_TERMS_INDEX[jieqi]
    if jieqi_index <= 1:
        ganzhi_year -= 1
    elif jieqi_index == 23 and month == 1:
        ganzhi_year -= 1

    year_tiangan = TIANGAN[(ganzhi_year - 4) % 10]
    year_dizhi = DIZHI[(ganzhi_year - 4) % 12]

    month_number = _JIEQI_MONTH_NUMBER[jieqi]
    month_tiangan = _MONTH_TIANGAN_BY_STEM[year_tiangan][(month_number - 1) % 10]
    month_dizhi = YUE_DIZHI[month_number - 1]

    day_tiangan, day_dizhi = _day_ganzhi(year, month, day)
    hour_dizhi = _hour_dizhi(hour)
    hour_tiangan = _HOUR_TIANGAN_BY_STEM[day_tiangan][_DIZHI_INDEX[hour_dizhi] % 10]
    return (
        year_tiangan + year_dizhi,
        month_tiangan + month_dizhi,
        day_tiangan + day_dizhi,
        hour_tiangan + hour_dizhi,
    )


@lru_cache(maxsize=256)
def _new_year_ganzhi_indexes(year):
    index = 0
    for i in range(1900, year):
        index += 6 if calendar.isleap(i) else 5
    return index % 10, (10 + index) % 12


def _day_ganzhi(year, month, day):
    y_tiangan_index, y_dizhi_index = _new_year_ganzhi_indexes(year)
    base_tg = y_tiangan_index + 1 + day + _DAY_GANZHI_TIANGAN_OFFSETS[month - 1]
    base_dz = y_dizhi_index + 1 + day + _DAY_GANZHI_DIZHI_OFFSETS[month - 1]
    if calendar.isleap(year) and month > 2:
        day_tiangan_index = base_tg % 10 + 1
        day_dizhi_index = base_dz % 12 + 1
    else:
        day_tiangan_index = base_tg % 10
        day_dizhi_index = base_dz % 12
    return TIANGAN[day_tiangan_index - 1], DIZHI[day_dizhi_index - 1]


def _hour_dizhi(hour):
    x = 1 if hour in (23, 0) else hour + 2
    return DIZHI[((x - 1) // 2) % 12]


def _yuanri(day_gz):
    if day_gz in _SHANG_YUAN_DAYS:
        return "上元"
    if day_gz in _ZHONG_YUAN_DAYS:
        return "中元"
    return "下元"


def _build_chart(year_gz, month_gz, day_gz, hour_gz, jieqi, info_text, header_text):
    yuanri = _yuanri(day_gz)
    yd_key = "yangdun" if jieqi in _YANG_JIEQI else "yindun"
    qiju = _QIJU_TABLE[jieqi + yuanri]
    palaces, sanqiliuyigong = _arrange_sanqi_liuyi(qiju, yd_key)
    yd_label = "阳遁" if yd_key == "yangdun" else "阴遁"

    xun_info = _xun_info(hour_gz, sanqiliuyigong)
    _arrange_bashen_and_tianpan(palaces, xun_info, yd_label)
    _arrange_jiuxing(palaces, xun_info)
    _arrange_bamen(palaces, hour_gz, xun_info, yd_label)

    return ChartResult(
        header_text=header_text.format(yinyang_dun=yd_label, yuanri=yuanri),
        info_text=info_text,
        output_boxes=_to_output_boxes(palaces),
        year_ganzhi=year_gz,
        month_ganzhi=month_gz,
        day_ganzhi=day_gz,
        hour_ganzhi=hour_gz,
        jieqi=jieqi,
        yinyang_dun=yd_label,
        yuanri=yuanri,
        qiju=qiju,
        xuntou=xun_info["xuntou"],
    )


def _arrange_sanqi_liuyi(qiju, yd_key):
    palaces = [{"地盘": "", "天盘": "", "八神": "", "九星": "", "八门": ""} for _ in range(9)]
    sanqiliuyigong = {}
    start = _GONGHAO[qiju]
    step = 1 if yd_key == "yangdun" else -1
    for offset, item in enumerate(_SANQI):
        index = (start + step * offset) % 9
        sanqiliuyigong[index] = item
        if index != 1:
            palaces[index]["地盘"] = item
    palaces[1]["地盘"] = f"{sanqiliuyigong[1]}\n{sanqiliuyigong[4]}"
    return palaces, sanqiliuyigong


def _xun_info(hour_gz, sanqiliuyigong):
    xuntou, xuntouzi, current_xun = _XUN_BY_HOUR[hour_gz]
    sanqiliuyilaoda = _LAODA_BY_HOUR[hour_gz]
    # 反查：sanqiliuyigong 由当次 _arrange_sanqi_liuyi 生成，键为宫号 0..8，值是 _SANQI 项。
    # 反向构造一次性的 value->key 即可避免重复 next() 扫描。
    by_value = {v: k for k, v in sanqiliuyigong.items()}
    return {
        "xuntou": xuntou,
        "xuntouzi": xuntouzi,
        "current_xun": current_xun,
        "xuntougonghao": by_value[xuntou],
        "laodagonghao": by_value[sanqiliuyilaoda],
    }


def _arrange_bashen_and_tianpan(palaces, xun_info, yd_label):
    xuntou_anchor = 1 if xun_info["xuntougonghao"] == 4 else xun_info["xuntougonghao"]
    laoda_anchor = 1 if xun_info["laodagonghao"] == 4 else xun_info["laodagonghao"]
    xuntou_zd = _ZHUANGDONG_INDEX[xuntou_anchor]
    laoda_zd = _ZHUANGDONG_INDEX[laoda_anchor]
    tianpan_list = [palaces[_ZHUANGDONG[i % 8]]["地盘"] for i in range(xuntou_zd, xuntou_zd + 8)]
    bashen = _BASHEN_YANG if yd_label != "阴遁" else _BASHEN_YIN
    for i in range(laoda_zd, laoda_zd + 8):
        palace = palaces[_ZHUANGDONG[i % 8]]
        offset = i - laoda_zd
        palace["八神"] = bashen[offset]
        palace["天盘"] = tianpan_list[offset]


def _arrange_jiuxing(palaces, xun_info):
    xuntougonghao = xun_info["xuntougonghao"]
    laodagonghao = xun_info["laodagonghao"]
    star_order = [_JIUXING[i % 9] for i in range(xuntougonghao, xuntougonghao + 9)]
    for i in range(laodagonghao, laodagonghao + 9):
        palaces[i % 9]["九星"] = star_order[i - laodagonghao]


def _arrange_bamen(palaces, hour_gz, xun_info, yd_label):
    bamen = list(_BAMEN)  # 每次新建，因为 (使) 标注会就地修改
    shicheng_index = xun_info["current_xun"].index(hour_gz)
    xuntou_index = xun_info["current_xun"].index(xun_info["xuntouzi"])
    diff = abs(shicheng_index - xuntou_index)
    xuntougonghao = xun_info["xuntougonghao"]
    if yd_label == "阳遁":
        fly_index = (xuntougonghao + diff) % 9
    else:
        fly_index = xuntougonghao - diff
        if fly_index < 0:
            fly_index += 9

    output_start = 5 if fly_index == 4 else _ZHUANGDONG_INDEX[fly_index]
    if xuntougonghao == 4:
        door_start = 5
        bamen[5] = bamen[5] + "(使)"
    else:
        door_start = _ZHUANGDONG_INDEX[xuntougonghao]
        bamen[door_start] = bamen[door_start] + "(使)"
    door_order = [bamen[i % 8] for i in range(door_start, door_start + 8)]
    for i in range(output_start, output_start + 8):
        palaces[_ZHUANGDONG[i % 8]]["八门"] = door_order[i - output_start]


def _to_output_boxes(palaces):
    output = {}
    for index, prefix in _OUTPUT_PREFIXES:
        palace = palaces[index]
        if index == 4:
            output[f"{prefix}_1"] = palace["九星"]
            output[f"{prefix}_2"] = palace["地盘"]
        else:
            output[f"{prefix}_1"] = palace["八神"]
            output[f"{prefix}_2"] = palace["八门"]
            output[f"{prefix}_3"] = palace["九星"]
            output[f"{prefix}_4"] = palace["地盘"]
            output[f"{prefix}_5"] = palace["天盘"]
            output[f"{prefix}_6"] = "+"
    return output
