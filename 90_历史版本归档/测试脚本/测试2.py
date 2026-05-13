from ephem import *
import math
import datetime
#24节气
jieqi=["春分","清明","谷雨","立夏","小满","芒种",\
       "夏至","小暑","大暑","立秋","处暑","白露",\
       "秋分","寒露","霜降","立冬","小雪","大雪",\
       "冬至","小寒","大寒","立春","雨水","惊蛰"]
#计算黄经
def ecliptic_lon(jd_utc):
    s=Sun(jd_utc)#构造太阳
    equ=Equatorial(s.ra,s.dec,epoch=jd_utc)#求太阳的视赤经视赤纬（epoch设为所求时间就是视赤经视赤纬）
    e=Ecliptic(equ)#赤经赤纬转到黄经黄纬
    return e.lon#返回黄纬
#根据时间求太阳黄经，计算到了第几个节气，春分序号为0
def sta(jd):
    e=ecliptic_lon(jd)
    n=int(e*180.0/math.pi/15)
    return n
#根据当前时间，求下个节气的发生时间
def iteration(jd,sta):#jd：要求的开始时间，sta：不同的状态函数
    s1=sta(jd)#初始状态(太阳处于什么位置)
    s0=s1
    dt = datetime.timedelta(days=1.0)
    while True:
        jd+=dt
        s=sta(jd)
        if s0!=s:
            s0=s
            dt=-dt/2#使时间改变量折半减小
        if abs(dt.total_seconds())<0.0000001 and s!=s1:
            break
    return jd
def jq(year):#从当前时间开始连续输出未来n个节气的时间
    jd=datetime.datetime(year-1,12, 15, 0, 0, 0)#获取当前时间的一个儒略日和1899/12/31 12:00:00儒略日的差值
    e=ecliptic_lon(jd)
    n=int(e*180.0/math.pi/15)+1
    a=[]
    for i in range(26):
        if n>=24:
            n-=24
        jd=iteration(jd,sta)
        d=Date(jd+datetime.timedelta(days=1/3)).tuple()
        jieqishijian = datetime.datetime(d[0], d[1], d[2], d[3], 0, 0)
        a.append(jieqishijian)
        print("{0}-{1:02d}-{2:02d} {3}：{4:02d}:{5:02d}:{6:03.1f}".format(d[0], d[1], d[2],jieqi[n],d[3], d[4], d[5]))
        n+=1
    return a
jq(2023)