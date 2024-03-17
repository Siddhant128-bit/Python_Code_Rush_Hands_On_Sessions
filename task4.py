'''
Get an input passage from user, and also get the maximum length of a word allowed and print output excluding words having a greater length then maximum length
'''

user_input = input("Enter a words: ").split()
max_length=int(input("Enter a maximum length of a word: "))

filtered_words = ' '.join(word for word in user_input if len(word) <= max_length)

print(f"Words after filtering: \n{filtered_words}")