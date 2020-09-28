# library allows shuffle
import random








# param - positive int n
def countFlips(n):

    # this variable stores num of flips in array
    flip = 0

    # create a list consisting of [1...n] and shuffle the array
    A = list(range(1, n+1))
    random.shuffle(A)


    # iterate through each array element
    for i in range(0, n):
        # compare each element to all the elements after it
        for j in range(i+1, n):
            # if anything is out of order, increment the flip variable
            if A[j] < A[i]:
                flip += 1

    # count the num of flips
    print(flip)


# call the function that counts num of flips in array
countFlips(2**3)










# bubble sort - sorts an array, ascending
# params: array A of size n
def bubbleSort(A, n):
    # iterate through each index (except last idx, where max element will be)
    for i in range(0, n - 1):
        # the last i elements are already in place
        for j in range(0, n - i - 1):
            if A[j] > A[j + 1]:
                A[j], A[j + 1] = A[j + 1], A[j]
    print(A)

# calls bubble sort on an array
bubbleSort([4, 2, 7, 3, 6, 9, 1], 7)
