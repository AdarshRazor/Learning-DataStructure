a= int(input())
arr=[]
for i in range(1,a+1):
    if a%i==0:
        arr.append(i)
        
print(len(arr)) 

# print arr in single line format
print(*arr)