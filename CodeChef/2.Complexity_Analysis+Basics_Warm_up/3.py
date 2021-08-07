N=int(input())

for i in range(N):
    wor=input()
    wl=len(wor)

    if wl%2==0:
        a,b=wor[:wl//2],wor[wl//2:]
    else:
        a,b=wor[:wl//2],wor[(wl//2)+1:]
    
    if sorted(a)==sorted(b):
        print('YES')
    else:
        print('NO')