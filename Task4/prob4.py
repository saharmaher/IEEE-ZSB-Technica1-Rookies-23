n = int(input())
print("please enter " ,n ,"intger")
l = list(map(int,input().split()))
r = 0
for i in range(len(l)):
    n -= 1
    r += l[i]*(10**n)
r += 1

res = [int(x) for x in str(r)]
print(res)