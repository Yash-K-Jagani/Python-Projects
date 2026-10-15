num_1 = input("Enter the first number: ")
num_2 = input("Enter the second number: ")
operator = input("Enter the operator (+, -, *, /): ")

if not num_1.replace('.', '', 1).isdigit() or not num_2.replace('.', '', 1).isdigit():
    print("Error: Please enter valid numbers.")
elif operator == "+":
    result = float(num_1) + float(num_2)
    print(f"The result of {num_1} + {num_2} is: {result}")
elif operator == "-":
    result = float(num_1) - float(num_2)
    print(f"The result of {num_1} - {num_2} is: {result}")
elif operator == "*":
    result = float(num_1) * float(num_2)
    print(f"The result of {num_1} * {num_2} is: {result}")
elif operator == "/":
    if float(num_2) != 0:
        result = float(num_1) / float(num_2)
        print(f"The result of {num_1} / {num_2} is: {result}")
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operator. Please use +, -, *, or /.")
