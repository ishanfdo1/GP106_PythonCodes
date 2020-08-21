# print 10 stars
# Lab02 Exercise 3
# 21/08/2020

# input numb of lines, converted to int to prevent errors in range()
# conversion solves the error but if you input a fraction if will only print
# the number for of lines for the int value.
numbOfLines = int(float(input("Enter the number of rows: ")))
# loops for the number of times inputted by user.
for line in range(numbOfLines):
    print("*"*10)  # print stars 10 times in the same line.




