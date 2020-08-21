# Lab01C - Vertical stress under the center of a loaded circular area
# Lab01C
# Date : 13/08/2020

# title
print("Veritcal stress under the center of a loaded circular "
      "area\n----------------------------------------------------------")
# input data
q = float(input("Enter q: "))
r = float(input("Enter r: "))
z = float(input("Enter z: "))
# calculate the answer
answer = q * (1 - 1 / ((r ** 2 / z ** 2 + 1) ** (3 / 2)))
# print answer
print("Vertical stress: ", round(answer, 3))
