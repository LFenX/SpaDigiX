from functionSpadigiX_GetvaluefromFIVEfour import gettheSpaDigiX_value
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
year=int(input("请输入年份："))
month=int(input("请输入月份："))
day=int(input("请输入日期："))
for i in range(0, 12):
    riganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][3]
    shichengganzhi = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4]
    if riganzhi == "甲子" and shichengganzhi == "甲子":
        for j in range(0, 12):
            panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][0]
            if panduanwugan == "戊":
                shuanggan="戊"
                hour = 2 * j
                break
    elif riganzhi == "甲戌" and shichengganzhi == "甲戌":
        for j in range(0, 12):
            panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][0]
            if panduanwugan == "己":
                shuanggan = "己"
                hour = 2 * j
                break
    elif riganzhi == "甲申" and shichengganzhi == "甲申":
        for j in range(0, 12):
            panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][0]
            if panduanwugan == "庚":
                shuanggan = "庚"
                hour = 2 * j
                break
    elif riganzhi == "甲寅" and shichengganzhi == "甲子":
        for j in range(0, 12):
            panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][0]
            if panduanwugan == "癸":
                shuanggan = "癸"
                hour = 2 * j
                break
    elif riganzhi == "甲午" and shichengganzhi == "甲午":
        for j in range(0, 12):
            panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][0]
            if panduanwugan == "辛":
                shuanggan = "辛"
                hour = 2 * j
                break
    elif riganzhi == "甲辰" and shichengganzhi == "甲辰":
        for j in range(0, 12):
            panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * i)[1][4][0]
            if panduanwugan == "壬":
                shuanggan = "壬"
                hour = 2 * j
                break
    elif riganzhi[0] == "甲" and shichengganzhi[0] == "甲":
        if riganzhi == "甲子":
            for j in range(0, 12):
                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                if panduanwugan == "戊":
                    shuanggan = "戊"
                    hour = 2 * j
                    break
        elif riganzhi == "甲戌":
            for j in range(0, 12):
                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                if panduanwugan == "己":
                    shuanggan = "己"
                    hour = 2 * j
                    break
        elif riganzhi == "甲辰":
            for j in range(0, 12):
                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                if panduanwugan == "壬":
                    shuanggan = "壬"
                    hour = 2 * j
                    break
        elif riganzhi == "甲寅":
            for j in range(0, 12):
                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                if panduanwugan == "癸":
                    shuanggan = "癸"
                    hour = 2 * j
                    break
        elif riganzhi == "甲申":
            for j in range(0, 12):
                panduanwugan = getthebasicmessageofnineGrids(year, month, day, 2 * j)[1][4][0]
                if panduanwugan == "庚":
                    shuanggan = "庚"
                    hour = 2 * j
                    break
        elif riganzhi == "甲午":
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
#双干
print("SDXAPP3")
print("双干：")
shuanggandeshu=gettheSpaDigiX_value(year,month,day,hour,"双干",shuanggan)
print(f"双干得数：{shuanggandeshu}")
print(
    "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
#值符
print("值符：")
zhifudeshu=gettheSpaDigiX_value(year,month,day,hour,"值符",shuanggan)
print(f"值符得数：{zhifudeshu}")
print(
    "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
#值使
print("值使：")
zhishideshu=gettheSpaDigiX_value(year,month,day,hour,"值使",shuanggan)
print(f"值使得数：{zhishideshu}")
print(
    "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
#生门
print("生门：")
shengmendeshu=gettheSpaDigiX_value(year,month,day,hour,"生门",shuanggan)
print(f"生门得数：{shengmendeshu}")
print(
    "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
print("-----------------------------------------------------------------------------------------------------------------")
SpaDigiX_dingji_value=(shuanggandeshu*2+zhifudeshu+zhishideshu+shengmendeshu)/5
while SpaDigiX_dingji_value<0:
    SpaDigiX_dingji_value=SpaDigiX_dingji_value+4
while SpaDigiX_dingji_value>4:
    SpaDigiX_dingji_value=SpaDigiX_dingji_value-4
print(f"定级结果：{SpaDigiX_dingji_value}")