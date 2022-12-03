l =list(map(int,input().split()))
res =[]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if (l[i] == l[j]):
            res.append(abs(j-i))
print(min(res))                         