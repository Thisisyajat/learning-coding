#Test file (playground)
# Declare variables
lowest = float('inf')
second_lowest = float('inf')

# Get 10 numbers input from the user
for i in range(10):
    num = input("Enter a number: ")
    try:
        num = int(num)
    except:
        print ("Invalid input")
        continue

    # Update the lowest and second lowest numbers if necessary
    if num < lowest:
        second_lowest = lowest
        lowest = num
    elif num < second_lowest and num != lowest:
        second_lowest = num

# Print the lowest and second lowest numbers
print("Lowest number:", lowest)
print("Second lowest number:", second_lowest)