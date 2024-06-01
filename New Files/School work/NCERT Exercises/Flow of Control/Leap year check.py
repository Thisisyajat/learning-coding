
# Check if the entered year is a leap year.
# NCERT EXERCISES

year = int(input("Enter the year ==> "))
leap = bool()

if ((year % 400) == 0):
    leap = True
elif ((year % 4) == 0):
    leap = True
else: leap = False

print(f"The year {year} is a leap year? ==> {leap}.")
