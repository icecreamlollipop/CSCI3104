
def foo(s, t, k, n):

    # create dp table
    DP = [[[False for x in range(k + 1)] for x in range(t + 1)] for x in range(n + 1)]

    # base case is true
    DP[0][0][0] = True

    # backtracking matrix; same dimensions as DP matrix
    prev = [[[None for c in range(k + 1)] for b in range(t + 1)] for a in range(n + 1)]

    # iterate through the dp table and fill in values
    for a in range(n + 1):
        for b in range(t + 1):
            for c in range(k + 1):
                # if there's a subset of the first a elements of s with cardinality c that sum to b,

                # it's true if we add another element of s AND use it (both cardinality and weight increases)
                if (DP[a][b][c] == True) and (a + 1) < (n + 1) and (b + s[a]) < (t + 1) and (c + 1) < (k + 1):
                    DP[a + 1][b + s[a]][c + 1] = True
                    # record the previous indices in the backtracking matrix; (a, b, c) are the indices that make DP[a + 1][b + s[a]][c + 1] true
                    prev[a + 1][b + s[a]][c + 1] = (a, b, c)

                # it's true if we add another element of s and simply don't use it
                if (DP[a][b][c] == True) and (a + 1) < (n + 1):
                    DP[a + 1][b][c] = True
                    # record the previous indices in the backtracking matrix; (a, b, c) are the indices that make DP[a + 1][b][c] true
                    prev[a + 1][b][c] = (a, b, c)

    # if the final value is false, then return false
    if DP[n][t][k] == False:
        return False

    # if the final value is true, backtrack
    arr = []
    while n > 0 or t > 0 or k > 0:
        # find the previous indices of the current True/False value in the backtracking matrix
        p = prev[n][t][k]
        # if the previous k (cardinality) is smaller than the k (target cardinality), append the value: target sum - current sum (which equals the s[i] value added to the current sum in order to create the target sum)
        if p[2] < k:
            arr.append(t - p[1])
        # backtrack; move to the previous indices of the current True/False value in the backtracking matrix
        n,t,k = p

    # reverse and return the backtracking matrix
    arr.reverse()
    return arr






def main():
    # s is the input array
    s = [2, 1, 5, 7]

    # t is the target sum
    t = 6

    # this is the cardinality of the subset sum
    k = 2

    print(foo(s, t, k, len(s)))

main()
