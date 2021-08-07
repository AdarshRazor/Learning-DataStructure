N = int(input())

even = 0
odd = 0

for i in range(1,(N*2)+1):
    if i%2==0:
        even+=i
    else:
        odd+=i

print(odd,even)    