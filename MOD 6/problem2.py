#2. Create a list of strings. Write code that counts how many times the word "Olympic" appears in the list, and then print the count.
strings = ["Olympic", "Oliver", "Olympic", "Ohana", "Obama", "Olympia"]
oly_counter = 0
for word in strings:
    if word == "Olympic":
        oly_counter += 1
print(oly_counter)
