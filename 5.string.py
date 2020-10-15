strings=['aba','baba','aba','xzxb']
queries=['aba','xzxb','ab']

count=0
out=[]

for i in range(len(queries)):
    count=0
    for j in range(len(strings)):
        if queries[i]==strings[j]:
            count+=1
    out.append(count)

print(out)
