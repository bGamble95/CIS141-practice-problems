#1. Create a list of integers (you get to pick!). Write code to iterate through the list and calculate the sum of all even numbers. Print the resulting sum.
numbers = [7, 18, 25, 90, 235]
even_sum = 0
for i in numbers:
    if i % 2 == 0:
        even_sum += i
print(even_sum)
