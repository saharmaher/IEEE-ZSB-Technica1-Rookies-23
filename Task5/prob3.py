n = int(input())
l = []
def ss(n):
  return sum(int(i)**2 for i in str(n))
while True:
  n = ss(n)
  print(n)
  
  if n == 1 or n in l:
    break
  l.append(n)  
if n ==1 :
  print("True")
else:
  print("False")     