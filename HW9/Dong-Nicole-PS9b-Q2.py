# tabulation function
# input: a list of assignments
# output: prints the max points
def tabulation(A):

    # Edge case: If A is empty, return
    if len(A) == 0:
        return

    # Create a lookup table that is the same size as the assignments list
    Z = []
    for i in range(0, len(A)):
        Z.append(0)

    # When there's only one assignment, include this assignment
    Z[0] = A[0]

    # Iterate to fill up the lookup table
    for i in range(1, len(A)):
        # Z[i] is the max of two values:
        # 1. If we exclude the current assignment A[i], the max points is Z[i - 1]
        # 2. If we include the current assignment A[i], the max points is A[i] + Z[i - 2]
        Z[i] = max(Z[i - 1], A[i] + Z[i - 2])

    # Print the max points obtained
    print("Tabulation method:", Z[-1], "points")






def iterative(A):
    # Edge case: If A is empty, return
    if len(A) == 0:
        return

    # When there's only one assignment, include this assignment
    inc = 0
    ex = 0
    curr = 0

    for i in range(0, len(A)):
        # curr is the max of excluding or including A[i]
        # inc is the value of excluding A[i - 1] plus A[i]
        # ex is the value of curr: nothing changes, basically
        inc = ex + A[i]
        ex = curr
        curr = max(inc, ex)

    # Print the max points obtained
    print("Iterative method:", curr, "points")







# main function
# define a list of assignments
# call tabulation() and iterative() on list to output the max points
def main():
    A = [2, 7, 9, 3, 1]
    tabulation(A)
    iterative(A)
main()
