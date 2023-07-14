# Temperature convertor

# Menu section

print("-------- TEMPERATURE CONVERTER ----------")
print(" ")
print("Menu")
print(" ")
print("1) convert from fahrenheit to celcius ")
print("2) convert from celsius to fahrenheit")

# prompt for user option
user_option = input("User option: ")

# Perform option check

if (int(user_option) == 1):

    # formula= 5/9*(f-32)
    temp_F = input("Enter temperature in fahrenheit: ")

    # cmputing the tempretarature in f
    result_F = (5/9) * (int(temp_F) - 32)
    # Printing the result
    print("The result is " + str(result_F))

elif (int(user_option) == 2):
    # formula = (c*(9/5) + 32)

    temp_c = input("Enter Temperature in celsius: ")

    result_c = (int(temp_c) * (9/5) + 32)

    print(temp_c + " c " + "is equivalent to " + str(result_c) + " F ")


else:
    print("Enter a valid option")
