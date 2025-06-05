#5. Create a list of integers. Use a loop to build a new list where each element is the square of the corresponding element in the original list. Print the new list.
numbers = [2, 4, 6, 8, 10, 12]
numbers_squared = []
for num in numbers:
    numbers_squared.append(num ** 2)
print(numbers_squared)
