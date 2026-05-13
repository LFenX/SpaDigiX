def yingyong2():
    from datetime import datetime, timedelta
    yea = int(input("请输入年份："))
    mon = int(input("请输入月份："))
    day = int(input("请输入日期："))
    Z = int(input("请输入总天数："))
    L = int(input("请输入连续天数："))
    J = int(input("请输入间隔时长："))
    qishi = datetime(yea, mon, day)
    tian = []
    yy = []
    for i in range(1, Z + 1):
        dayzhouqi = i // L
        daylianxu = i % L
        if daylianxu == 0:
            tianshu = (dayzhouqi - 1) * (L + J) + L
            jiange = timedelta(days=tianshu - 1)
            rightnow = qishi + jiange
            tian.append(rightnow)
        else:
            tianshu = dayzhouqi * (L + J) + daylianxu
            jiange = timedelta(days=tianshu - 1)
            rightnow = qishi + jiange
            tian.append(rightnow)
        for j in range(0, 12):
            number_of_hours_to_add = 2 * j  # 修改的小时数
            number_of_minutes_to_add = number_of_hours_to_add * 60
            modified_date = rightnow + timedelta(minutes=number_of_minutes_to_add)
            ye = modified_date.year
            mo = modified_date.month
            da = modified_date.day
            ho = modified_date.hour
            if i == 1:
                yy.append(modified_date)
                print("%s年%s月%s日%s时" % (ye, mo, da, ho))

    print(tian)
    print(yy)



