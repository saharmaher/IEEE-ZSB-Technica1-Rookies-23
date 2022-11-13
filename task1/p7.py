num = int(input("Enter a num: "))
rev_num = 0
base_pos = 1
def reversDigits(num):
    global rev_num
    global base_pos
    if(num > 0):
        reversDigits((int)(num / 10))
        rev_num += (num % 10) * base_pos
        base_pos *= 10
    return rev_num
print("Reverse of no. is ",
      reversDigits(num) )
if( num == rev_num ):
      print("Yes" )
else:
       print("No")
