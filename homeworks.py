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

# def sum_of_elements(numbers, exclude_negative=False):
#     sum = 0
#     for num in numbers:
#         if not exclude_negative or num >= 0:
#             sum += num
#     return sum

# def main():

#     input_numbers = input("Enter a list of numbers separated by spaces: ")
    
#     numbers = [int(num) for num in input_numbers.split()]
    
#     exclude = input("Do you want to exclude negative numbers? (yes/no): ").lower()
#     exclude_negative = exclude.startswith('y')
    
#     total = sum_of_elements(numbers, exclude_negative)
    
#     print("Sum of the elements:", total)

# if __name__ == "__main__":
#     main()


    #Matrix Operations

import random

def generate_random_matrix(rows, cols):
    matrix = []
    for _ in range(rows):
        row = [random.randint(1, 100) for _ in range(cols)]
        matrix.append(row)
    return matrix

def get_column_sum(matrix, column_index):
    column_sum = 0
    for row in matrix:
        column_sum += row[column_index]
    return column_sum

def get_row_average(matrix, row_index):
    row = matrix[row_index]
    row_sum = sum(row)
    row_average = row_sum / len(row)
    return row_average

rows = int(input("rows: "))
cols = int(input("cols: "))
matrix = generate_random_matrix(rows, cols)
print("Generated Matrix:")
for row in matrix:
    print(row)

column_index = int(input("Column index: "))
while column_index >= cols:
    print("ERROR: The column index cant be bigger than the number of cols!")
    column_index = int(input("Column index: "))

column_sum = get_column_sum(matrix, column_index)
print("Sum of values in column", column_index, ":", column_sum)

row_index = int(input("Row index: "))
while row_index >= rows:
    print("ERROR: The row index cant be bigger than the number of rows!")
    row_index = int(input("Row index: "))

row_average = get_row_average(matrix, row_index)
print("Average of values in row", row_index, ":", row_average)

   

