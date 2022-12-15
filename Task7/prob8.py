s = str(input())
s2=[]
i = 0
while i < len(s):
    if(s[i]=='.'):
        s2.append('0')
    elif(s[i]=='-'and s[i+1]=='.'):
        s2.append('1')
        i += 1
    else:
        s2.append('2')
        i += 1
    i +=1    
print(''.join(s2))	 