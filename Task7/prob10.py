x =[]
res = []
for j in range(3):
    a = list(map(int, input().split()))
    x.append(a)
if(x[0][0] + x[0][1] + x[1][0]) % 2 == 0:
    res.append("1")   
else:
    res.append("0")     
if(x[0][0] + x[0][1] + x[0][2]+x[1][1]) % 2 == 0:
    res.append("1")   
else:
    res.append("0")
if(x[0][1] + x[0][2] + x[1][2]) % 2 == 0:
    res.append("1")   
else:
    res.append("0")
if(x[0][0] + x[1][0] + x[1][1]+x[2][0]) % 2 == 0:
    res.append("1")   
else:
    res.append("0")
if(x[0][1] + x[1][0] + x[1][1]+x[1][2]+x[2][1]) % 2 == 0:
    res.append("1")   
else:
    res.append("0")
if(x[0][2] + x[1][1] + x[1][2]+x[2][2]) % 2 == 0:
    res.append("1")   
else:
    res.append("0")
if(x[1][0] + x[2][0]+x[2][1]) % 2 == 0:
    res.append("1")   
else:
    res.append("0")
if(x[2][2] + x[1][1] + x[2][1]+x[2][0]) % 2 == 0:
    res.append("1")   
else:
    res.append("0")
if(x[2][1] + x[1][2]+x[2][2]) % 2 == 0:
    res.append("1")   
else:
    res.append("0")
s1 = "".join(res[:3])
s2 = "".join(res[3:6])
s3 = "".join(res[6:9])
print(s1)
print(s2)
print(s3)

                
