N = int(input())
vol =[]
cap = []
vol_sum= 0
cap_sum =0
for i in range(N): 
    voll, capp = list(map(int, input().split()))
    vol_sum += voll
    cap.append(capp)
    vol.append(voll)
cap.sort(reverse=True)    
if vol_sum <= (cap[0]+cap[1]) :
    print("yes")
else:
    print("no")    


