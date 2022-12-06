arr = list(map(int, input().split()))
def heapify(arr, N, i):
 
    largest = i  
    l = 2 * i + 1  
    r = 2 * i + 2  
    if l < N and arr[l] > arr[largest]:
        largest = l
    if r < N and arr[r] > arr[largest]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, N, largest)
def buildHeap(arr, N):
    startIdx = N 
    for i in range(startIdx, -1, -1):
        heapify(arr, N, i)
def printHeap(arr, N):
    print("Array representation of Heap is:")
 
    for i in range(N):
        print(arr[i], end=" ")
    print()

N = len(arr)
buildHeap(arr, N)
printHeap(arr, N)
