import random
random.seed(42)
num = random.randint(100,999)
print (num)
z = str(num)
while True:
 mi =0
 hit = 0   
 a = int(input("guess a 3-digit number: "))
 x = str(a)
 for i in range(0,3):
    for j in range(0,3):
     if ( (i == j) and (x[i] == z[j]) ):
         hit += 1
     if ( (i != j) and (x[i] == z[j]) ):
         mi +=1
 print ( hit , "hit" , mi , "miss")

 if (a==num):
     print ("Game Over")
     print (num)
     break