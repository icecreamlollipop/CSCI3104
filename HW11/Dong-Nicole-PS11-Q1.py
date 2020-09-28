
# import libraries
import random
import linecache
import matplotlib.pyplot as plt










# Arguments: The name of a .txt file
# Algorithm: Selects a uniformly random 50% of the lines from the .txt file
# Returns: A list of the lines
def randLines(filename):
    idxs = random.sample(range(88799), 44399)
    return [linecache.getline(filename, i).split("\t")[0] for i in idxs]

















# Arguments: hash table, list of names, size of hash table
# Algorithm: Each letter is a number, h(name) = sum of letters mod l
def hashOne(tableOne, lines, l):

    # maps letters to their positions in the alphabet
    func = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
            "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15,
            "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
            "W": 23, "X": 24, "Y": 25, "Z": 26}

    # implement hash function and increment hash table position
    sum = 0
    for j in range(0, len(lines)):
        for i in range(0, len(lines[j])):
            sum += func[lines[j][i]]
        tableOne.append(sum % l)
        sum = 0

    plt.hist(tableOne, bins = l)
    plt.show()













# Arguments: hash table, list of names, size of hash table
# Algorithm: Universal hash function
def hashTwo(tableTwo, lines, l):

    # maps letters to their positions in the alphabet
    func = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6, "G": 7, "H": 8,
            "I": 9, "J": 10, "K": 11, "L": 12, "M": 13, "N": 14, "O": 15,
            "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
            "W": 23, "X": 24, "Y": 25, "Z": 26}

    sum = 0
    for j in range(0, len(lines)):
        # create a random list of weights
        weights = random.sample(range(0, l - 1), len(lines[j]))
        # implement hash function and increment hash table position
        for i in range(0, len(lines[j])):
            sum += func[lines[j][i]] * weights[i]
        tableTwo.append(sum % l)
        sum = 0

    plt.hist(tableTwo, bins = l)
    plt.show()












# Algorithm: Collect 50% random names from .txt file, call 2 hash functions on them, and graph the results
def main():

    lines = randLines("dist.all.last.txt")

    l = 5987
    tableOne = []
    tableTwo = []

    hashOne(tableOne, lines, l)
    hashTwo(tableTwo, lines, l)

main()
