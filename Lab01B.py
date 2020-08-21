# Lab01B question
# Calculate the volume of a cone
# Date : 13/08/2020

# Diplay the first two lines.
print("Volume of a cone\n----------------")
# input radius and height
radius = float(input("Enter radius: "))
height = float(input("Enter height: "))
# calculate the volume of cone
answer = 3.14* radius ** 2 * height / 3  # replace math.pi with 3.14 to do this without math library
# print the answer
print("The volume of the cone is ", answer)
