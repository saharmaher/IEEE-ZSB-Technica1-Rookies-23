x = int(input())
while True:
    x +=1
    a = int(x / 1000)
    b = int(x / 100 % 10)
    c = int(x / 10 % 10)
    d = int(x % 10)
    if ((a != b) and (a != c) and (a != d) and (b != c) and (b != d) and (c != d)):
        break
print(x)        