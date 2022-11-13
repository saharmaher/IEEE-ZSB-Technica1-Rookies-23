a = int(input("Enter a num: "))
b =  int(input("Enter a num: "))
n = min(a,b)
max=0
for i in range(2,n):
    if(a%i ==0 | b%i ==0):
        if( i > max):
           max = i
print(max)
