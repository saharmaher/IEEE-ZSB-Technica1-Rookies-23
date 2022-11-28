def subSequence(str1, str2):
    len_str1 = len(str1)
    len_str2 = len(str2)
    i = 0
    j = 0

    while i < len_str1 and j < len_str2:
        if str1[i] == str2[j]:
            i += 1
        j += 1
    return i == len_str1


str1 = 'hello'
str2 = input("enter string \n" )
print(subSequence(str1, str2))
