
'''
Task 2, Take an input passage from user, Count the total number of words
and also give the count of words starting from vowel sound
'''
input_passage=input("enter passage: ")
words=input_passage.split()
total_words=len(words)
vowel_words=[i for i in words if i[0].lower() in 'aeiou']
vowel_count=len(vowel_words)
print(f"total number of words: {total_words}")
print(f"number of words starting with a vowel sound: {vowel_count}")