# library allows shuffle
import random





# input: an integer n
# algorithm: generates an array of n numbers in the range [1...n] and shuffles them
def generate(n):
    A = list(range(1, n + 1))
    random.shuffle(A)
    return A





count = 0


# partition function used for quicksort
def partition_sort(A, l, r, k):
    global count
    for i in range(l, r):
        if A[i] == k:
            A[r], A[i] = A[i], A[r]
    # The pivot (x) is the last element in the given array
    x = A[r]
    # i is the index at the head of the given array
    i = l - 1
    # iterate through the given array
    for j in range(l, r):
        # if something is out of order, swap, and increase i
        count += 1
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]

    # put the pivot in its correct place as well
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1




# partition function used for quick select
def partition_select(A, l, r):
    global count
    # The pivot (x) is the last element in the given array
    x = A[r]
    # i is the index at the head of the given array
    i = l - 1
    # iterate through the given array
    for j in range(l, r):
        # if something is out of order, swap, and increase i
        if A[j] < x:
            i += 1
            A[i], A[j] = A[j], A[i]

    # put the pivot in its correct place as well
    A[i + 1], A[r] = A[r], A[i + 1]
    return i + 1











# quickselect algorithm
def QuickSelect(A, l, r, k):
    if k > 0 and k <= r - l + 1:
        # partition the given array based on the last element
        index = partition_select(A, l, r)
        # base case: return the k-th smallest element
        if index - l == k - 1:
            return index
        # recur on the left subarray
        if index - l > k - 1:
            return QuickSelect(A, l, index - 1, k)
        # recur on the right subarray
        return QuickSelect(A, index + 1, r, k - index + l - 1)








# quicksort function
def QuickSort(A, l, r):
    global count
    if l < r:
        # find the kth smallest element such that the array is split 1-3
        split = int((r - l + 1)/4)
        k = QuickSelect(A, l, r, split)

        # partition A based on k
        pi = partition_sort(A, l, r, k)

        # recur on the left and right subarrays
        QuickSort(A, l, pi - 1)
        QuickSort(A, pi + 1, r)








# counts num flips using bubbleSort
def bubbleSort(A):
    flip = 0;
    for i in range(0, len(A)):
        for j in range(i + 1, len(A)):
            if A[j] < A[i]:
                flip += 1
    print("BubbleSort comparisons:", flip)










# main function
def main():
    # generate the array
    n = 2**10;
    A = generate(n)

    # count the number of comparisons made using bubble sort
    #bubbleSort(A)

    # implement quicksort and count the number of comparisons made
    QuickSort(A, 0, len(A) - 1)
    print("QuickSort comparisons:", count)


# call the main function
main()
