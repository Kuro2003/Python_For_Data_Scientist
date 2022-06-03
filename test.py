def mergeSort(arr,a,d):
    if len(arr) > 1:

        mid = len(arr)//2

        L = arr[:mid]

        print(L)
        R = arr[mid:]
        
        d += 1
        if d == 1:
            a.append(L)
        else:
            a[0] = L
        print("k = " + str(d))
        print(a)

        mergeSort(L,a,d)
        mergeSort(R,a,d)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] < R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1
def printList(arr):
    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()


arr = [12, 11, 13, 5, 6, 7]
d = 0
a = []
b= []
print("Given array is")
printList(arr)
mergeSort(arr,a,d)
print("Sorted array is: ")
printList(arr)
print("Chi cuong")
