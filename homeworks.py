    #Calculator

a = float(input(" "))
operation = input()
b = float(input(" "))
if operation == '+':
    result = a + b
elif operation == '-': 
    result = a - b
elif operation == '*':
    result = a * b
elif operation == '/':
    if b != 0:
        result = a / b
    else:
        result = "Error! Division by zero."
else:
    result = "Invalid operation"

print("result = ", result, sep = "", end='\n')


   

