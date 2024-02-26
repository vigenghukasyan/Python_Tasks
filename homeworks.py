#     #Calculator

# a = float(input(" "))
# operation = input()
# b = float(input(" "))
# if operation == '+':
#     result = a + b
# elif operation == '-': 
#     result = a - b
# elif operation == '*':
#     result = a * b
# elif operation == '/':
#     if b != 0:
#         result = a / b
#     else:
#         result = "Error! Division by zero."
# else:
#     result = "Invalid operation"

# print("result = ", result, sep = "", end='\n')


#Number Classification

nums = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
even = []
odd = []
for i in nums:
    if i % 2 == 0:
        even.append(i)
    else: 
        odd.append(i)
print("Even numbers: ", even, end = '\n')
print("Odd numbers: ", odd) 
   

