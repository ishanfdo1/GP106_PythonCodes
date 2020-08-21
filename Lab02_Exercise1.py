# Convert C to K or F using if else
# Lab 02 Exercise 1
# 20/08/2020

string1 = ""
result_temp = None
# input the temperature value in Celcius
tempinC = float(input("Enter temperature in Celcius: "))
# input convert to K or F?
kOrF = input("Do you want to convert to K or F?: ")
if kOrF == "K":  # if kOrF is "K"
    result_temp = tempinC + 273.15
    string1 = "Kelvin"
else:  # if kOrF is not equal to "K", this will return answer in fahrenheit for wrong inputs too
    result_temp = (9/5)*tempinC + 32
    string1 = "Fahrenheit"
# print the asnwer
print(f"The temperature value in {string1} is {round(result_temp,2)} .")



