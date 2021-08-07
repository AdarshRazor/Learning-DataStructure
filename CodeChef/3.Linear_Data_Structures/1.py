T= int(input())

for i in range(T):
    arr=[]
    N = int(input())
    for j in range(N):
        S,P,V = map(int,input().split())
        Profit=(P//(S+1))*V
        arr.append(Profit)
        #print(arr)

    arr=sorted(arr)
    print(arr[-1])