list=[1,1,5,4,3,5,5,2,6,7,8,98]
list_reverse=[]
for i in range(1,len(list)+1):
    list_reverse.append(list[len(list)-i])
print(list_reverse)
id_dist={}
def calculate_count(list):
    for i in range(len(list)):
        i_count=0
        iid=list[i]
        for j in range(len(list)):
            if list[j]==iid:
                i_count+=1
        id_dist[iid]=i_count
    for iid,i_count in id_dist.items():
        print(f"{iid}在列表中出现了{i_count}次")
a=calculate_count(list)

mean_value_listnumber=sum(list)/len(list)
great_then_mean_value=[num for num in list if num>mean_value_listnumber]
print(f"列表中所哟大于均值的数为：{great_then_mean_value}")



