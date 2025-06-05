#3. Create a list of strings. Write code to create a new list that includes only the strings longer than three characters. Print the resulting filtered list.
words = ["The", "answer", "to", "the", "question"]
long_words = []
for w in words:
    if len(w) > 3:
        long_words.append(w)
print(long_words)
