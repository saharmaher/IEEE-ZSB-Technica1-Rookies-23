Rows = int(input("Give the number of rows:"))  
mat = []

for i in range(Rows):  
    single_row = list(map(int, input().split()))  
    mat.append(single_row)  
def difference(arr, n):
    d1 = 0
    d2 = 0
 
    for i in range(0, n):
        d1 = d1 + arr[i][i]
        d2 = d2 + arr[i][n - i - 1]
    return abs(d1 - d2)
difference(mat,Rows)