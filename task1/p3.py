a = int(input("Enter size of list: "))
b =[]
for i in range(0,a) :
   b.append(int(input("Enter list numbers: ")))
def sum1():
    sum = 0
    for i in b:
        sum += b[i]
    print (sum)
def sum2():
  i = 0
  sum = 0
  while (i!= a):
     sum += b[i]
     i +=1
  print(sum)
def getSum(b):
    if len(b)==0:
        return 0
    else:
        return b[0] + getSum(b[1:])
print(getSum(b))
