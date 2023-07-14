# Temperature convertor

# Menu section

print("-------- TEMPERATURE CONVERTER ----------")
print(" ")
print("Menu")
print(" ")
print("1) convert from fahrenheit to celcius ")
print("2) convert from celcius to fahrenheit")

# prompt for user option
user_option = input("User option: ")

# Perform option check

if (user_option == 1):

    # formula= 5/9*(f-32)
    temp_F = input("Enter temperature in fahrenheit")

    # cmputing the tempretarature in f
    result_F = (5/9) * (int(temp_F) - 32)
    # Printing the result
    print("The result is " + str(result_F))

elif (user_option == 2):
    # formula = (c*(9/5) + 32)


else:
    print("Enter a valid option")
