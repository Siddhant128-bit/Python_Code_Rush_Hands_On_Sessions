'''
Take a input passage from user
Count the total number of words and also give the count of words starting from vowel sound
'''
user_input = input("Enter a words: ")
splitted_words=user_input.split()

total_no_of_words = len(splitted_words)
print(f"Total number of words: {total_no_of_words}")

word_starting_from_vowel=0

print(f"Words starting from vowel sound: \n")
for word in splitted_words:
    if word[0].lower() in ['a','e','i','o','u']:
        print(f"{word}\n")
        word_starting_from_vowel+=1

print(f"Number of words starting from vowel sound: {word_starting_from_vowel}")
