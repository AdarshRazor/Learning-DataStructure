a,b,c=map(int,input().split())
area_of_triangle = int((a*b)/2)

if ((a+b+c)==180 and area_of_triangle>0):
    print('YES')
else:
    print('NO')
