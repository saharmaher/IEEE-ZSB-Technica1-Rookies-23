n = int(input())
arr = []
  
for j in range(n):
    a = list(map(int, input().split()))
    arr.append(a)
for i in range(n):
        j = 0
        k = n-1
        while j < k:
            t = arr[j][i]
            arr[j][i] = arr[k][i]
            arr[k][i] = t
            j += 1
            k -= 1
for i in range(n):
    for j in range(i, n):  
        temp = arr[i][j]
        arr[i][j] = arr[j][i]
        arr[j][i] = temp 
print(arr)