# Printing the following pattern:
'''

        1
      2 1 2
    3 2 1 2 3
  4 3 2 1 2 3 4
5 4 3 2 1 2 3 4 5

'''
# NCERT EXERCISES

n = 5  # number of horizontal lines in the pattern

k = (n * 2) - 1  # total number of initial spaces
for i in range(1, n + 1):
    for j in range(0, k):  # printing the initial spaces
        print(end=" ")
    for j in range(i, 0, -1):  # printing the left half of the pattern
        print(j, end=" ")
    for j in range(2, i + 1):  # printing the right half of the pattern
        print(j, end=" ")
    k -= 2
    print()
  