N= int(input())
arr=[]
for i in range(N):
    intp= int(int(input()))
    arr.append(intp)

for i in range(N):
    arr[i]=i[::-1]

print(arr)