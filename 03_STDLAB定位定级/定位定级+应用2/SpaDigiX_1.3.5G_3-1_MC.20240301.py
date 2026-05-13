from functionSpadigiX_GetvaluefromFIVEthreeG_3_1_MC import gettheSpaDigiX_value
from functionSpaDigiXAPPONE import getthebasicmessageofnineGrids
year=int(input("请输入年份："))
month=int(input("请输入月份："))
day=int(input("请输入日期："))
hour=int(input("请输入小时："))
riganzhi = getthebasicmessageofnineGrids(year, month, day, hour)[1][3]
shichengganzhi = getthebasicmessageofnineGrids(year, month, day, hour)[1][4]
if riganzhi == "甲子":
    rigan="戊"
elif riganzhi == "甲戌":
    rigan="己"
elif riganzhi == "甲辰":
    rigan="壬"
elif riganzhi == "甲寅":
    rigan="癸"
elif riganzhi == "甲申":
    rigan="庚"
elif riganzhi == "甲午":
    rigan="辛"
else:
    rigan=riganzhi[0]

if shichengganzhi == "甲子":
    shigan="戊"
elif shichengganzhi == "甲戌":
    shigan="己"
elif shichengganzhi == "甲辰":
    shigan="壬"
elif shichengganzhi == "甲寅":
    shigan="癸"
elif shichengganzhi == "甲申":
    shigan="庚"
elif shichengganzhi == "甲午":
    shigan="辛"
else:
    shigan=shichengganzhi[0]
#时干
print("SDXAPP3")
print("时干：")
shigandeshu=gettheSpaDigiX_value(year,month,day,hour,"时干",shigan,rigan)
print(f"时干得数：{shigandeshu}")
print(
    "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
#日干
print("日干：")
rigandeshu=gettheSpaDigiX_value(year,month,day,hour,"日干",shigan,rigan)
print(f"日干得数：{rigandeshu}")
print(
    "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
#值符
print("值符：")
zhifudeshu=gettheSpaDigiX_value(year,month,day,hour,"值符",shigan,rigan)
print(f"值符得数：{zhifudeshu}")
print(
    "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
#值使
print("值使：")
zhishideshu=gettheSpaDigiX_value(year,month,day,hour,"值使",shigan,rigan)
print(f"值使得数：{zhishideshu}")
print(
    "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
#生门
print("生门：")
shengmendeshu=gettheSpaDigiX_value(year,month,day,hour,"生门",shigan,rigan)
print(f"生门得数：{shengmendeshu}")
print(
    "---------------------------------------------------------------------------------------------------------------\n---------------------------------------------------------------------------------------------------------------\n")
print("-----------------------------------------------------------------------------------------------------------------")
SpaDigiX_dingji_value=(shigandeshu+rigandeshu+zhifudeshu+zhishideshu+shengmendeshu)/5
while SpaDigiX_dingji_value<0:
    SpaDigiX_dingji_value=SpaDigiX_dingji_value+4
while SpaDigiX_dingji_value>4:
    SpaDigiX_dingji_value=SpaDigiX_dingji_value-4
print(f"G3-1MC定级结果：{SpaDigiX_dingji_value}")