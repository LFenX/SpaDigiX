xiangshu=int(input("请输入需要输出的数列项数："))
a,b=1,1
list=[a,b]
for i in range(xiangshu):
    a+=b
    list.append(a)
    b+=a
    list.append(b)
print(",".join(map(str,list)))
