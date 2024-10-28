# Write program to find the grade of a student when grades are allocated as given in the table below.
# Percentage of Marks	Grade
# Above 90%	            A
# 80% to 90%	        B
# 70% to 80%	        C
# 60% to 70%	        D
# Below 60% 	        E
# Percentage of the marks obtained by the student is input to the program.
#
# NCERT EXERCISES

marks = input("Enter the percentage marks obtained out of 100 ==> ")
if marks.isnumeric():
    marks = float(marks)
    if marks > 100 or marks < 0:
        print("ERROR: Invalid marks entered. Exiting...")
    elif marks > 90:
        print("The student has obtained Grade A.")
        print("Program ran successfully. Exiting...")
    elif marks >= 80 and marks <= 90:
        print("The student has obtained Grade B.")
        print("Program ran successfully. Exiting...")
    elif marks >= 70 and marks <= 80:
        print("The student has obtained Grade C.")
        print("Program ran successfully. Exiting...")
    elif marks >= 60 and marks <= 70:
        print("The student has obtained Grade D.")
        print("Program ran successfully. Exiting...")
    else:
        print("The student has obtained Grade E.")
        print("Program ran successfully. Exiting...")

else: print("ERROR: Only numeric values are allowed. Exiting...")
