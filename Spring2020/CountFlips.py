# generate random array
import random
def init(n):
    A = list(range(1, n + 1))
    random.shuffle(A)
    return A




# mergesort implementation
def mergeSort(A, Z, l, r):
    numFlips = 0
    if l < r:
        m = (l + r)//2
        numFlips = mergeSort(A, Z, l, m)
        numFlips += mergeSort(A, Z, m + 1, r)
        numFlips += merge(A, Z, l, m, r)
    return numFlips

def merge(A, Z, l, m, r):
    i = l
    j = m + 1
    k = l
    numFlips = 0
    while i <= m and j <= r:
        if A[i] <= A[j]:
            Z[k] = A[i]
            i += 1
        else:
            Z[k] = A[j]
            numFlips += m + 1 - i
            j += 1
        k += 1
    while i <= m:
        Z[k] = A[i]
        i += 1
        k += 1
    while j <= r:
        Z[k] = A[j]
        j += 1
        k += 1
    for x in range(l, r + 1):
        A[x] = Z[x]
    return numFlips




# driver function
def main():
    n = 100
    A = init(n)
    print("-------- Input ----------------")
    print(A)
    numFlips = mergeSort(A, [0]*len(A), 0, len(A) - 1)
    print("\n-------- Output ---------------")
    print(A)
    print("\n-------- Num. Flips -----------")
    print(numFlips)

main()
