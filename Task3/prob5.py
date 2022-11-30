noc , nosc = map(int, input().split())
sc = list(map(int, input().split())) 
if len(sc) != nosc :
    print( "invalid cities num of cities , pleas enter ", nosc , "city index")
    sc = list(map(int, input().split()))

hasStation = [0] * noc
for city in sc :
  hasStation[city] = 1
dist, maxDist = 0, min(sc)

for city in range(noc):
        if hasStation[city] == 1:
            maxDist = max((dist + 1) // 2, maxDist)
            dist = 0
             
        else:
            dist += 1
print(max(maxDist, dist))      