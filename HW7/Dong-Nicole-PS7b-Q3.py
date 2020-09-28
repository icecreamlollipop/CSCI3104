# global variable - h-index
count = 0



# divide-and-conquer algorithm for finding h-index
def part(A, low, high):
    global count

    if low < high:

        # first find the middle index of the input array
        mid = int((high - low)/2)

        if A[mid] >= (mid + 1):
            # if the middle value is bigger than mid + 1, recur on left subarray
            if (mid + 1) > count:
                count = mid + 1
            # base case
            if (mid + 1) == count:
                return
            part(A, mid + 1, high)

        # if the middle value is smaller than mid + 1, recur on right subarray
        else:
            part(A, low, mid)



def main():
    global count

    # modify the array here
    A = [6, 5, 3, 1, 0]

    # call the divide-and-conquer algorithm
    part(A, 0, len(A) - 1)

    # print the h-index
    print("h-index =", count)

main()
