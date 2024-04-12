'''
Python basics 

Looping (for while), 
Data types List (append), dictionary (update)
basics data types
'''


#Task 1 hints: 
# print(max([1,2,3]))
# print(sum([1,2,3]))

'''
Task 1, write a program that basically isolates N (input from user) 
number of even numbers into a list and then gets me the sum of N even numbers
'''

num = int(input("Enter how many numbers you want to insert: "))
if num <= 0:
    print("Please enter a positive integer.")
else:
    even_numbers = []
    even_sum = 0
    for _ in range(num):
        num = int(input("Enter a number: "))
        if num % 2 == 0:
            even_numbers.append(num)
            even_sum += num
    print("Even numbers:", even_numbers)
    print("Sum of even numbers:", even_sum)

#Task 2 hints: 

# print(float('32'))
# print(list('Apple'))
# print('Apple is something something'.split())
# random_word='ball'
# print(random_word[0])

'''
Task 2, Take an input passage from user, Count the total number of words
and also give the count of words starting from vowel sound
'''

passage = input("Enter a passage: ")
vowels = ['a', 'e', 'i', 'o', 'u']

words = passage.split()
word_count = len(words)
vowel_word_count = len([word for word in words if word[0].lower() in vowels])

print(f"Total words: {word_count}\nWords starting with a vowel: {vowel_word_count}")


'''
Task 3
Write a program to basically reverse each word of a sentence (user provided) and not the sentence 
itself

Input Sentence: I eat rice
Output Sentence: I tae ecir
'''
sentence = input("Enter a sentence: ")

words = sentence.split()
reversed_words = [word[::-1] for word in words]
reversed_sentence = ' '.join(reversed_words)

print(f"Reversed: {reversed_sentence}")

'''
Task 4: get an input passage from user, and also get the maximum length 
of a word allowed 
and print output excluding words having greater length then maximum length 

input passage: "I eat Rice and I am also working on something"
maximum length: 5
output passage: "I eat Rice and I am also on "

'''

passage = input("Enter a passage: ")
max_length = int(input("Enter maximum length of word: "))

words = passage.split()
new_passage = ' '.join([word for word in words if (len(word)<=max_length)])

print(f"{new_passage}")