# Printing the following pattern:
'''
1 2 3 4 5
  1 2 3 4
    1 2 3
      1 2
        1

'''
# NCERT EXERCISES

n = 5  # number of horizontal lines in the pattern

k = 0 # initial number of spaces
for i in range(n, 0, -1):
    for j in range(0, k):
        print(end=" ")
    for j in range(1, i + 1):
        print(j, end=" ")
    k += 2
    print()
