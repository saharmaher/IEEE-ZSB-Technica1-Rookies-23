import heapq
N ,k = map(int, input().split())
print("please Enter",N,"intger")
arr = list(map(int, input().split()))
def print_N_mostFrequentNumber(arr, N, K):
    mp = dict()
    for i in range(len(arr)):
        if arr[i] not in mp:
            mp[arr[i]] = 0
        else:
            mp[arr[i]] += 1
    heap = [(value, key) for key,
            value in mp.items()]
    largest = heapq.nlargest(K, heap)
    print(K, " numbers with most "
             "occurrences are:", sep="")
    for i in range(K):
        print(largest[i][1], end=" ")
print_N_mostFrequentNumber(arr,N,k)        