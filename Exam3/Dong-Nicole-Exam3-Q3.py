import random










# RECURSIVE SOLUTION
def recur(A):

    n = len(A)

    # base case
    if(n == 2):
        return min(A[0], A[1])

    # what opponent will pick next, if I pick A[0]
    if A[1] < A[n - 1]:
        B = A[2:n]
    else:
        B = A[1:n - 1]

    # what opponent will pick next, if I pick A[n - 1]
    if A[0] < A[n - 2]:
        C = A[1:n - 1]
    else:
        C = A[0:n - 2]

    # I should pick the solution that minimizes my points
    return min(A[0] + recur(B), A[n - 1] + recur(C))




















# DYNAMIC PROGRAMMING SOLUTION
def foo(A):

    n = len(A)

    # Create a dp table
    DP = [[0 for i in range(n)] for i in range(n)]

    # Skip the entries where index i is greater than index j; also fill in the DP matrix diagonally
    for gap in range(n):
        for j in range(gap, n):
            i = j - gap

            # x, y: if i choose card i, the opponent will choose i + 1 or j, which means I can choose either i + 2 or j - 1
            # y, z: if i choose card j, the opponent will choose i or j - 1, which means I can choose either i + 1 or j - 2
            x = 0
            if((i + 2) <= j):
                x = DP[i + 2][j]
            y = 0
            if((i + 1) <= (j - 1)):
                y = DP[i + 1][j - 1]
            z = 0
            if(i <= (j - 2)):
                z = DP[i][j - 2]

            # I seek to minimize my score while my opponent seeks to maximize it
            DP[i][j] = min(A[i] + max(x, y), A[j] + max(y, z))

    # return the min value possible when considering all the cards
    return DP[0][n - 1]















# DRIVER FUNCTION
def main():

    # initialize the array of card values
    n = 100
    A = list(range(1, n + 1))
    random.shuffle(A)

    x = foo(A)
    print("My sum at the end is", x)
    print("Opponent's sum at the end is", sum(A) - x)
main()
