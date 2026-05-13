import random
def move_to_eastorwest(easts, wests, nongfu_status, item=None):
    if nongfu_status == "east":
        if item:
            easts.remove(item)
            wests.append(item)
        nongfu_status = "west"
    elif nongfu_status == "west":
        if item:
            wests.remove(item)
            easts.append(item)
        nongfu_status = "east"
    return easts, wests, nongfu_status


def if_safeornot(easts, wests, nongfu_status):
    if nongfu_status == "east" and (("狼" in wests and "羊" in wests) or ("羊" in wests and "白菜" in wests)):
        safe_status = "notsafe"
    elif nongfu_status == "east":
        safe_status = "safe"
    elif nongfu_status == "west" and (("狼" in easts and "羊" in easts) or ("羊" in easts and "白菜" in easts)):
        safe_status = "notsafe"
    elif nongfu_status == "west":
        safe_status = "safe"
    return safe_status
easts=["羊","狼","白菜"]
wests=[]
nongfu_status="east"
move_count=0
while nongfu_status!="west" or len(wests)!=3:
    safe_status="notsafe"
    while safe_status=="notsafe":
        if nongfu_status == "east" :
            item = random.choice(easts)
        elif nongfu_status == "west" and(("狼" in wests and "羊" in wests) or ("羊"in wests and "白菜" in wests)):
            item = "羊"
        elif nongfu_status == "west":
            item = None
        eastss=easts[:]
        westss=wests[:]
        nongfu_statuss=nongfu_status
        status_set=move_to_eastorwest(eastss,westss,nongfu_statuss,item)
        safe_status=if_safeornot(status_set[0],status_set[1],status_set[2])
    easts=status_set[0]
    wests=status_set[1]
    nongfu_status=status_set[2]
    move_count+=1
    print(f"第{move_count}次移动后：东边->{easts},西边->{wests},农夫在{nongfu_status}")



