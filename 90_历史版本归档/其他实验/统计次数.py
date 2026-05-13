# 定义字符串列表
strings = ['时干值使生门生门生门值使值使值使生门时干值使',
           '时干生门时干生门生门时干时干',
           '生门时干生门时干生门生门生门时干',
           '生门生门时干生门生门生门',
           '生门时干时干值使生门值使值使生门值使生门值使时干生门',
           '值使值使生门时干值使生门值使值使生门时干值使时干值使时干值使值使值使',
           '值使生门时干生门时干值使值使值使时干值使',
           '生门时干生门生门生门生门时干',
           '时干生门值使时干值使值使值使生门值使生门时干生门时干',
           '时干值使生门时干生门时干值使值使时干值使生门值使',
           '生门时干生门时干生门生门生门时干时干']

# 定义固定词汇
keywords = ['生门', '值使', '时干']

# 定义名称列表
names = ["子时", "丑时", "寅时", "卯时", "辰时", "巳时", "午时", "未时", "申时", "酉时", "戌时", "亥时"]

# 初始化结果字典
result = {}

# 遍历每个字符串和对应的名称，计算最大频次的词
for idx, (string, name) in enumerate(zip(strings, names)):
    max_word = max(keywords, key=string.count)
    max_frequency = string.count(max_word)
    result[name] = {'最大频次词': max_word, '频次': max_frequency}
# 按频次大小顺序对result字典进行排序
sorted_result = dict(sorted(result.items(), key=lambda item: item[1]['频次'], reverse=True))
count=0
# 输出结果
print("以下为排序结果：")
for key, value in sorted_result.items():
    count+=1
    print(f"{key}: {value['最大频次词']}',  {value['频次']} ")
    if count==4:
        print("--------------")

s={"生使":"23"}
if str(2) in s["生使"]:
    print("zai")