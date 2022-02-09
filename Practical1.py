import numpy as np

arr = np.array([1, 2, 3, 4, 5])   #Global array
print(arr)

def arr_sum():
    sum=0
    for i in range(0,len(arr)):
        sum=sum+arr[i]
    print("sum is:",sum)

def search_arr():
    key=(int)(input("Enter Key:"))
    x=np.where(arr==key)
    print(key,"Found at",x,"Location")

def minmax():
    print("Maximun",np.max(arr))
    print("Minimum",np.min(arr))

def evenodd():
    ev=0
    od=0
    for i in arr:
        if i % 2==0:
            ev=ev+1
        else:
            od=od+1
    print("Number of Even:",ev)
    print("Number of Odd:",od)

def errorhandeler():
    print("invalid Choice")
    exit()

switcher={
        1:arr_sum,
        2:search_arr,
        3:minmax,
        4:evenodd

    }

    

for i in range(len(switcher)+1):
    ch=(int)(input("enter ch"))
    switcher.get(ch,errorhandeler)()
    







