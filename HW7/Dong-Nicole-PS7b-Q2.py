# library allows shuffle
import random




# generates an array of n numbers in the range [1...n] and shuffles them
def generate(n):
    A = list(range(1, n + 1))
    random.shuffle(A)
    return A






# counts num flips using bubbleSort
def bubbleSort(A):
    flip = 0;
    for i in range(0, len(A)):
        for j in range(i + 1, len(A)):
            if A[j] < A[i]:
                flip += 1
    print("BubbleSort flips:", flip)








# given an array A, sorts the array and counts the number of flips. The sorted array is stored in Z
def mergeSort(A):
    Z = [0]*len(A)
    print("MergeSort flips:", countFlips(A, Z, 0, len(A) - 1))







# finds the mid index, recurs on the right subarray and left subarray to counts flips
def countFlips(A, Z, L, R):
    flip = 0
    if L < R:
        mid = (L + R)//2
        flip = countFlips(A, Z, L, mid)
        flip += countFlips(A, Z, mid + 1, R)
        flip += merge(A, Z, L, mid, R)
    return flip





# merges two sorted arrays and counts num flips
def merge(A, Z, L, mid, R):
    i = L
    j = mid + 1
    k = L
    flip = 0

    # place elements from the right and left subarray to the merged array; increment number of flips when elements are out of order
    while i <= mid and j <= R:
        if A[i] <= A[j]:
            Z[k] = A[i]
            k += 1
            i += 1
        else:
            Z[k] = A[j]
            flip += (mid - i + 1)
            k += 1
            j += 1

    # copy the remaining elements of the right and left subarray to the merged array
    while i <= mid:
        Z[k] = A[i]
        k += 1
        i += 1
    while j <= R:
        Z[k] = A[j]
        k += 1
        j += 1
    for m in range(L, R + 1):
        A[m] = Z[m]

    # return the number of flips
    return flip







def main():
    n = 2**3
    A = generate(n)
    print("A =", A)
    bubbleSort(A)
    mergeSort(A)
main()
