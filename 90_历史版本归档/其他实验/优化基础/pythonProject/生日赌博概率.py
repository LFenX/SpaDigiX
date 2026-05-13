import random
defeat_count=0
test_count=10000
for i in range(test_count):
    a=set()
    for j in range(50):
        a.add(random.randint(1,365))
    if len(a)==50:
        defeat_count+=1
print(f"一个班有 50 人，我敢打赌，几乎一定有两个人是同一天生日。假设一年有 365 天，我赌对的概率是{(test_count-defeat_count)/test_count}")

