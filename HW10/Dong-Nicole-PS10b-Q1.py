


# given two strings, returns the cost matrix
def alignStrings(x, y, insert, delete, sub):

    # create the DP array
    S = [[None] * (len(x) + 1) for i in range(len(y) + 1)]

    # initialize the costs
    temp = sub

    # use tabulation to fill the DP array
    for i in range(0, len(y) + 1):
        for j in range(0, len(x) + 1):

            # base case (empty strings): zero
            if i == 0 and j == 0:
                S[i][j] = 0

            # more base cases (one is an empty string)
            elif i == 0 and j != 0:
                S[i][j] = S[i][j - 1] + delete
            elif i != 0 and j == 0:
                S[i][j] = S[i - 1][j] + insert

            # subproblems
            # - if the characters are equal, the cost of substitute is 0
            # - the table entry is the min of the costs of: substitute, delete, insert
            else:
                if y[i - 1] == x[j - 1]:
                    sub = 0
                else:
                    sub = temp
                S[i][j] = min(S[i - 1][j - 1] + sub, S[i][j - 1] + delete, S[i - 1][j] + insert)

    # return the DP table
    return S















# given a cost matrix, returns a list of operations
def extractAlignment(S, x, y, insert, delete, sub):

    # create an empty list to store operations
    a = []

    # initialize variables
    i = len(y)
    j = len(x)
    temp = sub

    # keep iterating while base case has not yet been reached
    while i > 0 and j > 0:

        # if the characters are equal, sub = 0, else sub = sub
        if y[i - 1] == x[j - 1]:
            sub = 0
        else:
            sub = temp

        # if the current entry comes from a sub operation, backtrack diagonally
        if S[i][j] == S[i - 1][j - 1] + sub:
            if sub == 0:
                a.append("no-op")
            else:
                a.append("sub")
            i -= 1
            j -= 1

        # if the current entry comes from a delete operation, backtrack to the left
        elif S[i][j] == S[i][j - 1] + delete:
            a.append("delete")
            j -= 1

        # if the current entry comes from an insert operation, backtrack up
        elif S[i][j] == S[i - 1][j] + insert:
            a.append("insert")
            i -= 1

    if j != 0:
        for k in range(0, j):
            a.append("delete")
    if i != 0:
        for k in range(0, i):
            a.append("insert")

    # return the reversed list
    a.reverse()
    return a









# iterate through a
def commonSubstrings(x, L, a):

    # create list of substrings
    Z = []

    # iterate through the operations
    temp = ""
    for i in range(0, len(a)):
        # if the operation is an insert, insert a space
        if a[i] == "insert":
            x = x[:i] + "_" + x[i:]
        # if a no-op is reached, increase the temp string
        if a[i] == "no-op":
            temp += x[i]
        # if some other operation is reached, evaluate the temp string and reset
        else:
            if len(temp) >= L:
                Z.append(temp)
            temp = ""
    if len(temp) >= L:
        Z.append(temp)

    # return the substrings
    return Z













# driver function
def main():

    # open and read from files
    file1 = open("Song1_Folsom_Prison.txt", "r")
    file2 = open("Song2_Crescent_City_Blues.txt", "r")

    # define the strings
    y = file1.read()
    x = file2.read()

    y = "POLYNOMIAL"
    x = "EXPONENTIAL"
    L = 1

    # define the costs
    sub = 2
    delete = 1
    insert = 2

    # get the cost matrix
    print("alignStrings")
    print("-------------")
    S = alignStrings(x, y, insert, delete, sub)
    print("S =")
    for i in range(0, len(S)):
        print(S[i])

    # get the operations
    print("\nextractAlignment")
    print("-------------")
    a = extractAlignment(S, x, y, insert, delete, sub)
    print("a =", a)

    # get the common substrings
    print("\ncommonSubstrings")
    print("-------------")
    Z = commonSubstrings(x, L, a)
    print("Z =", Z)


main()
