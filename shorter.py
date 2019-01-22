'''
[WARNING] It is recommended not to add more than 7 destinations.
          For more, the execution time is minutes.
'''

from collections import deque, namedtuple
import openpyxl as xl
from datetime import datetime


def submatrix(matrix,num):
    to_return = []
    for line in matrix[0:num] + matrix[num+1:len(matrix)]:
        subline = line[0:num] + line[num+1:len(line)]
        to_return.append(subline)
    return to_return


def walker(matrix):
    if len(matrix) == 1:
        return 0
    else:
        paths = []
        for i in range(len(matrix)):
            for j in range(len(matrix)):
                if i != j:
                    distance = matrix[i][j] + walker(submatrix(matrix, i))
                    paths.append(distance)
        return min(paths)




if __name__ == "__main__":

    matrix = [[0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 0, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
              [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],]

    matrix2 = [[0, 2, 3],
               [4, 0, 6],
               [7, 8, 0]]

    #walker(matrix)
    for i in range(1,9):
        print("--------------------")
        print("{0}x{0}".format(i))
        init = datetime.now()
        a = walker(matrix[:i])
        print(datetime.now()-init)
        print(a)
    #print(matrix)
    #print("")
    #print(walker(matrix))
