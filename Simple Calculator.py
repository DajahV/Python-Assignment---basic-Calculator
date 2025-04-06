
def perform_operation(num1, num2, operation):
    if operation == '+':
        return num1 + num2
    elif operation == '-':
        return num1 - num2
    elif operation == '*':
        return num1 * num2
    elif operation == '/':
        return num1 / num2
    else:
        return "This is an Invalid Operation"
    
    # Example inputs
num1 = float(input("Enter your first number here:"))
num2 = float(input("Enter your first number here:"))
operation = input("What operation do you want to perform? ")

result = perform_operation(num1, num2, operation)
print(f"{num1} {operation} {num2} = {result}")




