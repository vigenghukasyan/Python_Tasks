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

# nums = list(map(int, input("Enter a list of numbers separated by spaces: ").split()))
# even = []
# odd = []
# for i in nums:
#     if i % 2 == 0:
#         even.append(i)
#     else: 
#         odd.append(i)
# print("Even numbers: ", even, end = '\n')
# print("Odd numbers: ", odd) 


    #Sum of Elements

def sum_of_elements(numbers, exclude_negative=False):
    sum = 0
    for num in numbers:
        if not exclude_negative or num >= 0:
            sum += num
    return sum

def main():

    input_numbers = input("Enter a list of numbers separated by spaces: ")
    
    numbers = [int(num) for num in input_numbers.split()]
    
    exclude = input("Do you want to exclude negative numbers? (yes/no): ").lower()
    exclude_negative = exclude.startswith('y')
    
    total = sum_of_elements(numbers, exclude_negative)
    
    print("Sum of the elements:", total)

if __name__ == "__main__":
    main()

   

