a,b,c = map(int,input().split())

s=(a+b+c)//2

area=(s*(s-a)*(s-b)*(s-c))**0.5

print(area)

if area>0:
    print("YES")
else:
    print("NO")
