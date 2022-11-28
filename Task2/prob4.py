str = input('Enter elements of a list separated by space ')
print("\n")
ulst = str.split()
print(ulst)
not_repeated = []
for i in ulst:
    if i not in not_repeated:
        not_repeated.append(i)

print(not_repeated)
