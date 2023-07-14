# Area calc

# Menu section for project

print("----------- Area Calculator ------------")
print(" ")
print("Menu")
print(" ")
print("1) Area of a rectangle")
print("2) Area of a tringle")

# prompt for user option
user_option = input("Enter option: ")

# perform option check
if (int(user_option) == 1):
    # formula= Length*width
    length = input("Enter the lenght: ")
    Width = input("Enter the Width: ")
    # Gettting the area

    Area = int(length) * int(Width)

    # printing result
    print("The Area = " + str(Area))

elif (int(user_option) == 2):
    # formula = 1/2*(b*h)

    Base = input("Enter the Base: ")
    Height = input("Enter the Height: ")
    # Getting the area

    Area = (1/2) * int(Base) * int(Height)
    # printing result

    print("The area = " + str(Area))

else:
    print("Error: Enter a valid option")
