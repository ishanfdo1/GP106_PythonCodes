# Reynolds number
# Lab02 Exercise 2
# 21/08/2020

# input reynolds number
reynoldsNumb = float(input("Enter the reynols number: "))
if reynoldsNumb <= 2300:  # if reynoldsNumb is lower than or equal to 2300
    result = "laminar Region"
elif reynoldsNumb <= 4000:  # if 2300<reynoldsNumb<=4000
    result = "transition Region"
else:  # if reynoldsNumb is larger than 4000
    result = "turbulent Region"
# print the asnwer
print(f"The Reynolds number {reynoldsNumb} is in {result}")


