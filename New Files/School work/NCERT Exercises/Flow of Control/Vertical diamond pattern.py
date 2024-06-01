
# Printing the following pattern:
'''

    *
  * * *
* * * * *
  * * *
    *
  
'''
# NCERT EXERCISES


n = 5  # number of horizontal lines in the pattern

# for upper half
k = (round(n/2) * 2)  # for initial spaces
for i in range(0, n, 2):
    for j in range(0, (k+1)):
        print(end=" ")
    for j in range(0, (i+1)):
        print("*",end=" ")
    k = k - 2
    print()

#lower half
k = 1
for i in range(n-1, 0, -2):
    for j in range(0, k + 2):
        print(end = " ")
    for j in range(0, i-1):
        print("*", end=" ")
    k = k + 2
    print()





'''
This code generates a pattern of asterisks (`*`). The pattern is a series of
horizontal lines, each line containing an odd number of asterisks. The number
of asterisks in each line increases by 2 from the previous line, starting from
1. The lines are centered by adding spaces before the asterisks.

Here's a dry run of the code with `n = 5`:

| i (Line Number) | k (Initial Spaces) | Asterisks |
|:---------------:|:------------------:|:---------:|
|        0        |          4         |     *     |
|        2        |          2         |   * * *   |
|        4        |          0         | * * * * * |

So, the output of the code would be:

```
    *
  * * *
* * * * *
```

Each row in the table corresponds to a line of output from the code. The 'i'
column represents the line number (starting from 0), the 'k' column represents
the number of initial spaces on that line, and the 'Asterisks' column represents
the asterisks printed on that line. The number of asterisks is `i+1`, and they
are separated by spaces. The number of initial spaces decreases by 2 for each
subsequent line. This creates the centered triangular pattern. The pattern only
includes lines with an odd number of asterisks, so it skips every other line
(hence the `range(0, n, 2)` in the code). The total number of lines is `n`,
which is 5 in this case. The pattern forms the upper half of a diamond shape.

In the lower half, the number of asterisks starts from `n-2` and decreases by
2 each time, and the number of initial spaces starts from 2 and increases by 2
each time. This creates the inverted triangular pattern that forms the lower
half of the diamond. The `range(n-3, -1, -2)` generates the line numbers for
the lower half in reverse order, skipping every other line just like the upper
half. The total number of lines in the lower half is `n-1`, one less than the
upper half, to avoid duplicating the middle line. The result is a full diamond
pattern. The pattern will look like this for `n = 5`:

```
    *
  * * *
* * * * *
  * * *
    *
```

Sure, here's a dry run of the entire code with `n = 5`:

| i (Line Number) | k (Initial Spaces) | Asterisks | Part |
|:---------------:|:------------------:|:---------:|:----:|
|        0        |          4         |     *     | Upper|
|        2        |          2         |   * * *   | Upper|
|        4        |          0         | * * * * * | Upper|
|        2        |          2         |   * * *   | Lower|
|        0        |          4         |     *     | Lower|

So, the output of the code would be:

```
    *
  * * *
* * * * *
  * * *
    *
```

Each row in the table corresponds to a line of output from the code.
The 'i' column represents the line number (starting from 0 for the upper half
and `n-3` for the lower half), the 'k' column represents the number of initial
spaces on that line, and the 'Asterisks' column represents the asterisks
printed on that line. The number of asterisks is `i+1`, and they are separated
by spaces. The number of initial spaces decreases by 2 for each subsequent line in the upper half and increases by 2 for each subsequent 
line in the lower half. This creates the diamond pattern. The pattern includes 
lines with an odd number of asterisks, so it skips every other line (hence the
`range(0, n, 2)` and `range(n-3, -1, -2)` in the code). The total number of lines
is `2n - 1`, which is 9 in this case. The pattern forms a full diamond shape.
The 'Part' column indicates whether the line is part of the 'Upper' or 'Lower'
half of the diamond. The middle line is included in both halves, so it appears
twice in the table. The pattern forms a full diamond shape. The 'Part' column
indicates whether the line is part of the 'Upper' or 'Lower' half of the diamond.
The middle line is included in both halves, so it appears twice in the table.

'''
