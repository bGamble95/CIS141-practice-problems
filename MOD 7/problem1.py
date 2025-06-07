#1. Write a function called count_vowels(input) that takes a string
#and returns the number of vowels (a, e, i, o, u) in it.
def count_vowels(input):
    vowels = ("a", "e", "i", "o", "u")
    v_count = 0
    for char in input.lower():
        if char in vowels:
          v_count += 1
    return v_count  
V_count = count_vowels("Spider-Man: Brand New Day")
print(V_count)
