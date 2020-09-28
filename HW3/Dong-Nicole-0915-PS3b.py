# counts min num of stops the robot must take
# params: array A of charging pod distances, k is max distance robot can travel
def countPods(A, k):

    # this variable is used in the if-statement
    temp = k

    # this is the list of stops returned at the end
    ret = []

    # iterate through given array to find stops
    for i in range(0, len(A)):

        # this if statement is for when the robot needs to make a stop
        if A[i] >= temp:
            # append the stop to the return list and update temp
            ret.append(A[i - 1])
            temp = A[i - 1] + k

    # return the list containing the distances where robot must stop
    return ret




# test cases (these are listed as examples in the homework pdf)
print(countPods([0, 20, 37, 54, 70, 90], 40))
print(countPods([0, 18, 21, 24, 37, 56, 66], 20))
print(countPods([0, 10, 15, 18], 20))
