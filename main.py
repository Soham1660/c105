import csv
import math
with open('data1.csv', newline='')as fileObject:
    reader=csv.reader(fileObject)
    file_data=list(reader)
data=file_data[0]

def mean (data):
    n=len(data)
    total=0
    for x in data:
        total+=int(x)
    mean=total/n
    return mean
squared_list=[]
for numbers in data:
    a=int(numbers)-mean(data)
    a=a**2
    squared_list.append(a)
sum=0
for i in squared_list:
    sum=sum+i
result=sum/(len(data)-1)
std_dev=math.sqrt(result)
print(std_dev)
