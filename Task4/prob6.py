m = input()
k = 6174
def find_n(m, n = 0):
    if m == k:
        return n
    string_val = str(m)
    string_val = ((4 - len(string_val)) * "0" ) + string_val
    asc_val = "".join(sorted(string_val))
    dec_val = int(asc_val[::-1])
    asc_val = int(asc_val)
    value = dec_val - asc_val
    return find_n(value,n+1)
print(find_n(m))