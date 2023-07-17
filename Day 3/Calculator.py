# CALCULATOR

# MENU SECTION

print("---------- CALCULATOR ---------")
print(" ")
print("MENU")
print(" ")
print("1) Addition")
print("2) Substraction")
print("3) Multiplication")
print("4) Division")
print(" ")

operator = input("Enter an operator (+ - * / ): ")
x = input("Enter the value of X : ")
y = input("Enter the value of y : ")

if operator == "+":
    Result = int(x) + int(y)
    print("The result of the Addition is: " + str(Result))

elif operator == "-":
    result = Result = int(x) - int(y)
    print("The result of the Substraction is: " + str(Result))

elif operator == "*":
    result = Result = int(x) * int(y)
    print("The result of the Multiplication is: " + str(Result))

elif operator == "/":
    result = Result = int(x) / int(y)
    print("The result of the Division is: " + str(Result))

else:
    print("Error: Enter a valid Operator")
