# Equivalent resistance calc
# Lab02 Exercise 3
# 21/08/2020

# Section 1: input the resistor values
numbOfResistors = int(float(input("Enter number of resistors in either series or parallel: ")))
# create an empty list
resistorValues = []
# fill the list with values
for roundNumb in range(numbOfResistors):
    value = float(input(f"Input resistor value in ohms for resistor number {roundNumb + 1}:  "))
    resistorValues.append(value)
# print the list for verification
print(f"The values you entered are {resistorValues}")

# Section 2: Calculate the answer and print
string1 = ""
result = 0
# get input for series of parallel ?
SorP = input("Are they in series or parallel?\nS for series and P for parallel: ")
if SorP == "S":  # if series
    result = sum(resistorValues)  # sum of the list
    string1 = "series"  # string to print in answer
elif SorP == "P":  # if parallel
    oneDividedByResult = 0
    string1 = "parallel"  # string to print in answer
    for eachValue in resistorValues:  # calculate the reciprocal of the result
        oneDividedByResult += 1/eachValue
    result = 1/oneDividedByResult  # calc the result
else:  # if wrong input
    print("Error, please type \"S\" or \"P\"")
    quit()  # end the program as the input is wrong
# print the final answer
print(f"Equivalent resistance for resistors in {string1} is {round(result, 3)} ohms")

