s1 = str(input())
s2 = str(input())
s3 = s1[::-1]
z = s2.find(s3)
if  (z == -1):
  print("False")
else:
   print("True")  