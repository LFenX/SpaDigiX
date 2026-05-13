from dataclasses import dataclass
import calendar
import datetime
import math

from ephem import Date, Ecliptic, Equatorial, Sun
from zhdate import ZhDate


TIANGAN = ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]
DIZHI = ["子", "丑", "寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥"]
SHENGXIAO = ["鼠", "牛", "虎", "兔", "龙", "蛇", "马", "羊", "猴", "鸡", "狗", "猪"]
YUE_DIZHI = ["寅", "卯", "辰", "巳", "午", "未", "申", "酉", "戌", "亥", "子", "丑"]

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
    solar_date = datetime.datetime(year, month, day)
    lunar_date = ZhDate.from_datetime(solar_date)
    shengxiaonian = SHENGXIAO[(int(lunar_date.lunar_year) - 1900) % 12]
    jieqi = _solar_term_for_date(year, month, day)
    year_gz, month_gz, day_gz, hour_gz = _ganzhi_from_solar(year, month, day, hour, jieqi)

    result = _build_chart(
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
    return result


def build_chart_from_lunar_date(year, lunar_month, lunar_day, hour, minute):
    solar_date = ZhDate(int(year), int(lunar_month), int(lunar_day)).to_datetime()
    return build_chart_from_solar(solar_date.year, solar_date.month, solar_date.day, int(hour), int(minute))


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


def _solar_term_for_date(year, month, day):
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
    for _ in range(26):
        if n >= 24:
            n -= 24
        jd = iteration(jd)
        d = Date(jd + datetime.timedelta(days=1 / 3)).tuple()
        boundaries.append(datetime.datetime(d[0], d[1], d[2], d[3], 0, 0))
        n += 1

    v = datetime.datetime(year, month, day, 23, 59, 0)
    jieqi_index = 0
    for i in range(25):
        if boundaries[i] <= v <= boundaries[i + 1]:
            jieqi_index = i
            break

    jieqi_list = [
        "冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨",
        "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑", "白露",
        "秋分", "寒露", "霜降", "立冬", "小雪", "大雪", "冬至", "小寒",
    ]
    return jieqi_list[jieqi_index]


def _ganzhi_from_solar(year, month, day, hour, jieqi):
    jieqi_year_terms = [
        "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨",
        "立夏", "小满", "芒种", "夏至", "小暑", "大暑", "立秋", "处暑",
        "白露", "秋分", "寒露", "霜降", "立冬", "小雪", "大雪", "冬至",
    ]
    ganzhi_year = year
    jieqi_index = jieqi_year_terms.index(jieqi)
    if jieqi_index <= 1:
        ganzhi_year -= 1
    elif jieqi_index == 23 and month == 1:
        ganzhi_year -= 1

    year_tiangan = TIANGAN[(ganzhi_year - 4) % 10]
    year_dizhi = DIZHI[(ganzhi_year - 4) % 12]

    month_number = _jieqi_month_number(jieqi)
    month_tiangan = _month_tiangan(year_tiangan, month_number)
    month_dizhi = YUE_DIZHI[month_number - 1]

    day_tiangan, day_dizhi = _day_ganzhi(year, month, day)
    hour_dizhi = _hour_dizhi(hour)
    hour_tiangan = _hour_tiangan(day_tiangan, DIZHI.index(hour_dizhi))
    return (
        year_tiangan + year_dizhi,
        month_tiangan + month_dizhi,
        day_tiangan + day_dizhi,
        hour_tiangan + hour_dizhi,
    )


def _jieqi_month_number(jieqi):
    jieqi_order = [
        "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种",
        "夏至", "小暑", "大暑", "立秋", "处暑", "白露", "秋分", "寒露", "霜降",
        "立冬", "小雪", "大雪", "冬至", "小寒", "大寒",
    ]
    i = jieqi_order.index(jieqi)
    if i % 2 == 0:
        return (i + 2) // 2
    return (i + 1) // 2


def _month_tiangan(year_tiangan, month_number):
    groups = [
        (("甲", "己"), ["丙", "丁", "戊", "己", "庚", "辛", "壬", "癸", "甲", "乙"]),
        (("乙", "庚"), ["戊", "己", "庚", "辛", "壬", "癸", "甲", "乙", "丙", "丁"]),
        (("丙", "辛"), ["庚", "辛", "壬", "癸", "甲", "乙", "丙", "丁", "戊", "己"]),
        (("丁", "壬"), ["壬", "癸", "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛"]),
        (("戊", "癸"), ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]),
    ]
    for stems, sequence in groups:
        if year_tiangan in stems:
            return sequence[(month_number - 1) % 10]
    raise ValueError(f"invalid year tiangan: {year_tiangan}")


def _hour_tiangan(day_tiangan, hour_dizhi_index):
    groups = [
        (("甲", "己"), ["甲", "乙", "丙", "丁", "戊", "己", "庚", "辛", "壬", "癸"]),
        (("乙", "庚"), ["丙", "丁", "戊", "己", "庚", "辛", "壬", "癸", "甲", "乙"]),
        (("丙", "辛"), ["戊", "己", "庚", "辛", "壬", "癸", "甲", "乙", "丙", "丁"]),
        (("丁", "壬"), ["庚", "辛", "壬", "癸", "甲", "乙", "丙", "丁", "戊", "己"]),
        (("戊", "癸"), ["壬", "癸", "甲", "乙", "丙", "丁", "戊", "己", "庚", "辛"]),
    ]
    for stems, sequence in groups:
        if day_tiangan in stems:
            return sequence[hour_dizhi_index % 10]
    raise ValueError(f"invalid day tiangan: {day_tiangan}")


def _new_year_ganzhi_indexes(year):
    index = 0
    for i in range(1900, year):
        index += 6 if calendar.isleap(i) else 5
    return index % 10, (10 + index) % 12


def _day_ganzhi(year, month, day):
    y_tiangan_index, y_dizhi_index = _new_year_ganzhi_indexes(year)
    tiangan_index = [-1, 0, -2, -1, -1, 0, 0, 1, 2, 2, 3, 3]
    dizhi_index = [-1, 6, 10, 5, -1, 6, 0, 7, 2, 8, 3, 9]
    if calendar.isleap(year) and month > 2:
        day_tiangan_index = (y_tiangan_index + 1 + day + tiangan_index[month - 1]) % 10 + 1
        day_dizhi_index = (y_dizhi_index + 1 + day + dizhi_index[month - 1]) % 12 + 1
    else:
        day_tiangan_index = (y_tiangan_index + 1 + day + tiangan_index[month - 1]) % 10
        day_dizhi_index = (y_dizhi_index + 1 + day + dizhi_index[month - 1]) % 12
    return TIANGAN[day_tiangan_index - 1], DIZHI[day_dizhi_index - 1]


def _hour_dizhi(hour):
    x = 1 if hour in (23, 0) else hour + 2
    return DIZHI[((x - 1) // 2) % 12]


def _yuanri(day_gz):
    shang = {
        "甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己卯", "庚辰", "辛巳", "壬午", "癸未",
        "甲午", "乙未", "丙申", "丁酉", "戊戌", "己酉", "庚戌", "辛亥", "壬子", "癸丑",
    }
    zhong = {
        "己巳", "庚午", "辛未", "壬申", "癸酉", "甲申", "乙酉", "丙戌", "丁亥", "戊子",
        "己亥", "庚子", "辛丑", "壬寅", "癸卯", "甲寅", "乙卯", "丙辰", "丁巳", "戊午",
    }
    if day_gz in shang:
        return "上元"
    if day_gz in zhong:
        return "中元"
    return "下元"


def _build_chart(year_gz, month_gz, day_gz, hour_gz, jieqi, info_text, header_text):
    yuanri = _yuanri(day_gz)
    yd_key = "yangdun" if jieqi in {
        "冬至", "小寒", "大寒", "立春", "雨水", "惊蛰", "春分", "清明", "谷雨", "立夏", "小满", "芒种",
    } else "yindun"
    qiju = _qiju(jieqi, yuanri, yd_key)
    palaces, sanqiliuyigong = _arrange_sanqi_liuyi(qiju, yd_key)
    yd_label = "阳遁" if yd_key == "yangdun" else "阴遁"

    xun_info = _xun_info(hour_gz, sanqiliuyigong)
    _arrange_bashen_and_tianpan(palaces, sanqiliuyigong, xun_info, yd_label)
    _arrange_jiuxing(palaces, xun_info)
    _arrange_bamen(palaces, hour_gz, xun_info, yd_label)

    output_boxes = _to_output_boxes(palaces)
    return ChartResult(
        header_text=header_text.format(yinyang_dun=yd_label, yuanri=yuanri),
        info_text=info_text,
        output_boxes=output_boxes,
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


def _qiju(jieqi, yuanri, yd_key):
    yang = {
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
    }
    yin = {
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
    return (yang if yd_key == "yangdun" else yin)[jieqi + yuanri]


def _arrange_sanqi_liuyi(qiju, yd_key):
    gonghao = {"坎一": 0, "坤二": 1, "震三": 2, "巽四": 3, "中五": 4, "乾六": 5, "兑七": 6, "艮八": 7, "离九": 8}
    sanqi = ["甲子戊", "甲戌己", "甲申庚", "甲午辛", "甲辰壬", "甲寅癸", "　丁　", "　丙　", "　乙　"]
    palaces = [{"地盘": "", "天盘": "", "八神": "", "九星": "", "八门": ""} for _ in range(9)]
    sanqiliuyigong = {}
    start = gonghao[qiju]
    step = 1 if yd_key == "yangdun" else -1
    for offset, item in enumerate(sanqi):
        index = (start + step * offset) % 9
        sanqiliuyigong[index] = item
        if index != 1:
            palaces[index]["地盘"] = item
    palaces[1]["地盘"] = f"{sanqiliuyigong[1]}\n{sanqiliuyigong[4]}"
    return palaces, sanqiliuyigong


def _xun_info(hour_gz, sanqiliuyigong):
    xun_lists = [
        ("甲子戊", "甲子", ["甲子", "乙丑", "丙寅", "丁卯", "戊辰", "己巳", "庚午", "辛未", "壬申", "癸酉"]),
        ("甲戌己", "甲戌", ["甲戌", "乙亥", "丙子", "丁丑", "戊寅", "己卯", "庚辰", "辛巳", "壬午", "癸未"]),
        ("甲申庚", "甲申", ["甲申", "乙酉", "丙戌", "丁亥", "戊子", "己丑", "庚寅", "辛卯", "壬辰", "癸巳"]),
        ("甲午辛", "甲午", ["甲午", "乙未", "丙申", "丁酉", "戊戌", "己亥", "庚子", "辛丑", "壬寅", "癸卯"]),
        ("甲辰壬", "甲辰", ["甲辰", "乙巳", "丙午", "丁未", "戊申", "己酉", "庚戌", "辛亥", "壬子", "癸丑"]),
        ("甲寅癸", "甲寅", ["甲寅", "乙卯", "丙辰", "丁巳", "戊午", "己未", "庚申", "辛酉", "壬戌", "癸亥"]),
    ]
    xuntou, xuntouzi, current_xun = next((a, b, c) for a, b, c in xun_lists if hour_gz in c)
    sanqi = ["甲子戊", "甲戌己", "甲申庚", "甲午辛", "甲辰壬", "甲寅癸", "　丁　", "　丙　", "　乙　"]
    if hour_gz[0] == "甲":
        sanqiliuyilaoda = sanqi[["甲子", "甲戌", "甲申", "甲午", "甲辰", "甲寅"].index(hour_gz)]
    else:
        sanqiliuyilaoda = sanqi[["戊", "己", "庚", "辛", "壬", "癸", "丁", "丙", "乙"].index(hour_gz[0])]
    xuntougonghao = next(key for key, value in sanqiliuyigong.items() if value == xuntou)
    laodagonghao = next(key for key, value in sanqiliuyigong.items() if value == sanqiliuyilaoda)
    return {
        "xuntou": xuntou,
        "xuntouzi": xuntouzi,
        "current_xun": current_xun,
        "xuntougonghao": xuntougonghao,
        "laodagonghao": laodagonghao,
    }


def _zhuangdong_index(palace_index):
    return [0, 7, 2, 3, 8, 1, 6, 5].index(palace_index)


def _arrange_bashen_and_tianpan(palaces, sanqiliuyigong, xun_info, yd_label):
    zhuangdong = [0, 7, 2, 3, 8, 1, 6, 5]
    xuntou_anchor = 1 if xun_info["xuntougonghao"] == 4 else xun_info["xuntougonghao"]
    laoda_anchor = 1 if xun_info["laodagonghao"] == 4 else xun_info["laodagonghao"]
    xuntou_zd = _zhuangdong_index(xuntou_anchor)
    laoda_zd = _zhuangdong_index(laoda_anchor)
    tianpan_list = [palaces[zhuangdong[i % 8]]["地盘"] for i in range(xuntou_zd, xuntou_zd + 8)]
    bashen = ["值符", "螣蛇", "太阴", "六合", "白虎", "玄武", "九地", "九天"]
    if yd_label == "阴遁":
        bashen = ["值符", "九天", "九地", "玄武", "白虎", "六合", "太阴", "螣蛇"]
    for i in range(laoda_zd, laoda_zd + 8):
        palace_index = zhuangdong[i % 8]
        offset = i - laoda_zd
        palaces[palace_index]["八神"] = bashen[offset]
        palaces[palace_index]["天盘"] = tianpan_list[offset]


def _arrange_jiuxing(palaces, xun_info):
    jiuxing = ["天蓬", "天芮", "天冲", "天辅", "天禽", "天心", "天柱", "天任", "天英"]
    star_order = [jiuxing[i % 9] for i in range(xun_info["xuntougonghao"], xun_info["xuntougonghao"] + 9)]
    for i in range(xun_info["laodagonghao"], xun_info["laodagonghao"] + 9):
        palaces[i % 9]["九星"] = star_order[i - xun_info["laodagonghao"]]


def _arrange_bamen(palaces, hour_gz, xun_info, yd_label):
    zhuangdong = [0, 7, 2, 3, 8, 1, 6, 5]
    bamen = ["休", "生", "伤", "杜", "景", "死", "惊", "开"]
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

    output_start = 5 if fly_index == 4 else _zhuangdong_index(fly_index)
    if xuntougonghao == 4:
        door_start = 5
        bamen[5] = bamen[5] + "(使)"
    else:
        door_start = _zhuangdong_index(xuntougonghao)
        bamen[door_start] = bamen[door_start] + "(使)"
    door_order = [bamen[i % 8] for i in range(door_start, door_start + 8)]
    for i in range(output_start, output_start + 8):
        palaces[zhuangdong[i % 8]]["八门"] = door_order[i - output_start]


def _to_output_boxes(palaces):
    prefixes = {
        0: "output_2_1",
        1: "output_0_2",
        2: "output_1_0",
        3: "output_0_0",
        4: "output_1_1",
        5: "output_2_2",
        6: "output_1_2",
        7: "output_2_0",
        8: "output_0_1",
    }
    output = {}
    for index, prefix in prefixes.items():
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
