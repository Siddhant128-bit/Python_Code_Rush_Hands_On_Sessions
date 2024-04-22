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
N=int(input("Enter your numbers:"))
sum_even_list=sum(num for num in range(2,N) if num%2==0)
print(sum_even_list)

# Task 2 hints: 
# print(float('32'))
# print(list('Apple'))
# print('Apple is something something'.split())
# random_word='ball'
# print(random_word[0])

'''
Task 2, Take an input passage from user, Count the total number of words
and also give the count of words starting from vowel sound
'''
passage=input("Enter your passage:")
words=passage.split()
total_words=len(words)
vowel_start_words =sum(1 for word in words if word[0].lower() in 'aeiou')
print(vowel_start_words ,total_words)

'''
Task 3
Write a program to basically reverse each word of a sentence (user provided) and not the sentence 
itself

Input Sentence: I eat rice
Output Sentence: I tae ecir
'''
print("Output sentence:", ' '.join(word[::-1] for word in input("Input sentence: ").split())) 


'''
Task 4: get an input passage from user, and also get the maximum length 
of a word allowed 
and print output excluding words having greater length then maximum length 

input passage: "I eat Rice and I am also working on something"
maximum length: 5
output passage: "I eat Rice and I am also on "

'''

input_passage = input("Enter the passage: ")
max_length = int(input("Enter the maximum length of a word allowed: "))
words = input_passage.split()
filtered_words = [word for word in words if len(word) <= max_length]
output_passage = ' '.join(filtered_words)
print("Output passage:", output_passage)

