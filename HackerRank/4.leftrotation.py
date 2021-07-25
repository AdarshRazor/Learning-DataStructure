arr=[1,2,3,4,5,6,7]

d=3

for i in range(d):
    temp=arr[0]
    arr.remove(arr[0])
    arr.append(temp)

print(arr)