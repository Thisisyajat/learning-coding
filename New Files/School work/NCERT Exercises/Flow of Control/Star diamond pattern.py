# Printing the following pattern:
'''
  *
 * *
*   *
 * *
  *
'''
# NCERT EXERCISES

n = 70      # size of the pattern (here, two rows in upper half, and 2 rows in lower half)
j = n - 1   # for the spaces in the second half of the pattern
print(' '*(n) + '*')    # printing the first line

for i in range(1, (2 * n)):     # prints the lines of the diamond from the second line to the second-to-last line.
    if i > n:                  # if i > n, then we are in the second half of the pattern
        print(' '*(i-n) + '*' + ' '*((2 * j) - 1) + '*') 
        j -= 1                 # j is decremented by 1 to print the correct number of spaces in the next line
    else:                     # if i <= n, then we are in the first half of the pattern
        print(' '*(n - i) + '*' + ' '*((2 * i) - 1) + '*')
if n > 1:
    print(' '*(n) + '*')
