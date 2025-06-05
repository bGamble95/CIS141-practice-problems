#4.  Create a list of integers. Write code that counts how many numbers are positive and how many are negative, then print both counts.
numbers = [1, -2, -5, 10, -3, 4, -7]
pos_count = 0
neg_count = 0
for num in numbers:
    if num > 0:
        pos_count += 1
    elif num < 0:
        neg_count += 1
print("Positive Count: ", pos_count)
print("Negative Count: ", neg_count)
