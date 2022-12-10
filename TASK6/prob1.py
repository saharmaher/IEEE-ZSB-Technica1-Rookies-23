import math
import os
import random
import re
import sys

#
# Complete the 'findDigits' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.
#


def findDigits(n):
    n1 = n
    count = 0
    
    while(n1!=0):
        
        newNum = n1%10
        n1 = n1//10
        
        try:
        
            if(n%newNum==0):
                count+=1
                
        except ZeroDivisionError:
            
            pass
            
    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
