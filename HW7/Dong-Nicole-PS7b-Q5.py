# library allows shuffle
import random



# partition function
def partition(A, low, high, pivot):
    i = low
    j = low
    # iterate from low index to high index
    while j < high:
        # if element at j is less than pivot, swap with element at i and increment i
        if A[j] < pivot:
            A[i], A[j] = A[j], A[i]
            i += 1
        # if element at j equals pivot, swap with element at high and decrement j
        elif A[j] == pivot:
            A[j], A[high] = A[high], A[j]
            j -= 1
        # increment j
        j += 1
    # swap element at i with element at high and return i, a new pivot
    A[i], A[high] = A[high], A[i]
    return i





def quickMatch(lids, bottles, low, high):
    if low < high:
        # partition the lids array using the last bottles element as pivot
        pivot = partition(lids, low, high, bottles[high])
        # partition the bottles array using lids[pivot] as pivot
        partition(bottles, low, high, lids[pivot])
        # recur on right and left subarrays
        quickMatch(lids, bottles, low, pivot - 1)
        quickMatch(lids, bottles, pivot + 1, high)
    else:
        return






def main():

    # generate lids
    lids = list(range(1, 101))
    random.shuffle(lids)

    # generate bottles
    bottles = list(range(1, 101))
    random.shuffle(bottles)

    print("Before Matching:")
    print("\nlids =", lids)
    print("\nbottles =", bottles)

    # match lids and bottles
    quickMatch(lids, bottles, 0, len(lids) - 1)

    print("\nAfter Matching:")
    print("\nlids =", lids)
    print("\nbottles =", bottles)


main()
