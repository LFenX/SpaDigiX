def getdingjideshu(year,month,day):
    from functionSpadigiX_GetvaluefromFIVEthreeG4MC import gettheSpaDigiX_value
    from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
    year = int(year)
    month = int(month)
    day = int(day)
    for i in range(0, 12):

        riganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][3]
        shichengganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4]
        if i ==0 and day==6:
            print(riganzhi,shichengganzhi)
        if riganzhi == "甲子" and shichengganzhi == "甲子":
            for j in range(0, 12):
                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                print(panduanwugan)
                if panduanwugan == "戊":
                    shuanggan = "戊"
                    hour = 2 * j
                    print('到了')
                    break
        elif riganzhi == "甲戌" and shichengganzhi == "甲戌":
            for j in range(0, 12):
                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                if panduanwugan == "己":
                    shuanggan = "己"
                    hour = 2 * j
                    break
        elif riganzhi == "甲申" and shichengganzhi == "甲申":
            for j in range(0, 12):
                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                if panduanwugan == "庚":
                    shuanggan = "庚"
                    hour = 2 * j
                    break
        elif riganzhi == "甲寅" and shichengganzhi == "甲子":
            for j in range(0, 12):
                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                if panduanwugan == "癸":
                    shuanggan = "癸"
                    hour = 2 * j
                    break
        elif riganzhi == "甲午" and shichengganzhi == "甲午":
            for j in range(0, 12):
                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                if panduanwugan == "辛":
                    shuanggan = "辛"
                    hour = 2 * j
                    break
        elif riganzhi == "甲辰" and shichengganzhi == "甲辰":
            for j in range(0, 12):
                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                if panduanwugan == "壬":
                    shuanggan = "壬"
                    hour = 2 * j
                    break
        elif riganzhi[0]=="甲" and shichengganzhi[0]=="甲":
            if riganzhi=="甲子":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    if panduanwugan == "戊":
                        shuanggan = "戊"
                        hour = 2 * j
                        break
            elif riganzhi=="甲戌":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    if panduanwugan == "己":
                        shuanggan = "己"
                        hour = 2 * j
                        break
            elif riganzhi=="甲辰":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    if panduanwugan == "壬":
                        shuanggan = "壬"
                        hour = 2 * j
                        break
            elif riganzhi=="甲寅":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    if panduanwugan == "癸":
                        shuanggan = "癸"
                        hour = 2 * j
                        break
            elif riganzhi=="甲申":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    if panduanwugan == "庚":
                        shuanggan = "庚"
                        hour = 2 * j
                        break
            elif riganzhi=="甲午":
                for j in range(0, 12):
                    panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                    if panduanwugan == "辛":
                        shuanggan = "辛"
                        hour = 2 * j
                        break

        else:
            if riganzhi[0] == shichengganzhi[0]:
                shuanggan = riganzhi[0]
                hour = 2 * i
                break
    # 双干
    shuanggandeshu = gettheSpaDigiX_value(year, month, day, hour, "双干", shuanggan)
    # 值符
    zhifudeshu = gettheSpaDigiX_value(year, month, day, hour, "值符", shuanggan)
    # 值使
    zhishideshu = gettheSpaDigiX_value(year, month, day, hour, "值使", shuanggan)
    # 生门
    shengmendeshu = gettheSpaDigiX_value(year, month, day, hour, "生门", shuanggan)
    print(
        "-----------------------------------------------------------------------------------------------------------------")
    SpaDigiX_dingji_value = (shuanggandeshu * 2 + zhifudeshu + zhishideshu + shengmendeshu) / 5
    while SpaDigiX_dingji_value < 0:
        SpaDigiX_dingji_value = SpaDigiX_dingji_value + 4
    while SpaDigiX_dingji_value > 4:
        SpaDigiX_dingji_value = SpaDigiX_dingji_value - 4
    if SpaDigiX_dingji_value==0:
        SpaDigiX_dingji_value=1
    nianyueriganzhi = getthebasicmessageofnineGrids(year, month, day, hour)[2]
    return SpaDigiX_dingji_value,shuanggandeshu,zhishideshu,zhifudeshu,shengmendeshu,nianyueriganzhi,riganzhi
