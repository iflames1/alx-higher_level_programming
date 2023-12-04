#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    nums = []
    j = 0

    for row in matrix:
        for i in row:
            nums.append(i)

    for i in nums:
        if j == 3:
            print()
            j = 0
        j += 1
        print("{} ".format(i), end="")
    print()


