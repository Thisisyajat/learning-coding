# Print the sum of digits of number entered by the user.
# NCERT EXERCISES

n = int(input("Enter a natural number : "))
nnum = n
add = 0

while (nnum != 0):
    dig = nnum % 10;
    nnum = (nnum // 10)
    add += dig
print(f"The sum of the digits in {n} is {add}.")
