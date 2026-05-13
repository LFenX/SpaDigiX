def d(x,y):
    if y==0:
        raise RuntimeWarning("除0")
    return x/y
try:
    print(d(3,0))
    print("我有话讲")
except :
    print(f"朕已知，你继续吧")
print(f"从这里继续")