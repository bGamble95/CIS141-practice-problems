#3. Create a text file called song_lyrics.txt and copy the lyrics of a song into
#it. Write a Python program that:
#- Reads the file
#- Requests 5 inputs from the user: 5 words the user would like to count the frequency of
#- Counts how many times each word appears
#- Creates a dictionary of the words and their counts
#- Print the dictionary to the console

file = open('song_lyrics.txt', 'r')
lyrics = file.read().lower().split()

words_search = []
for i in range(5):
    word = input(f"Enter word {i+1} to count: ")
    words_search.append(word)

words_count = {word: 0 for word in words_search}

for word in lyrics:
    if word in words_count:
        words_count[word] += 1
print("Word Count:")
print(words_count)
