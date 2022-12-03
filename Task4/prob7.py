n = int(input())
s = []
for i in range(n):
    s.append(str(input()))
from collections import defaultdict 
temp = defaultdict(list)  
for ele in s:
    temp[str(sorted(ele))].append(ele)
res = list(temp.values())
print(res)