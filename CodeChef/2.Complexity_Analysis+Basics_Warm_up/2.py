N= int(input())
arr=[]

for i in range(N):
    a=int(int(input()))
    reverse=0
    while a!=0:
        rem=a%10
        reverse=reverse*10+rem
        a=a//10
    arr.append(reverse)

for i in range(N):
    print(arr[i])