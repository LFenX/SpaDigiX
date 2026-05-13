def cal(ori_str=[]):
    new_str=[]
    for el in ori_str:
        if el not in ["e","i","o","u"]:
            new_str.append(el)
    return new_str
new_str=cal(["H","e","l","l","o",",","W","o","r","l","d","d","!"])
print(new_str)
