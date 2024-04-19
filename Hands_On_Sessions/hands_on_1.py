'''
task 1: write a program that isolates N number 
of even numbers into a list and then gets me 
the sum of N even numbers
'''
n = int(input("Enter any number N:"))
even_list = [i for i in range(0, 2*n, 2)]
print(even_list)
print(sum(even_list))

'''
task 2: 
print(list('apple))
print('apple is a fruit'.split())

Take an input passage from user, Count total no
word and also give the count of words from vowel sound
'''
word_list = []
vowel_words =[]
vowel = 'aeiou'
passage = input("Enter a passage:")
word_list = passage.split()
print(' total no of words: ' , len(word_list))
for word in word_list:
    if word[0].lower() in vowel:
        vowel_words.append(word)
print(vowel_words)
print('total no of words start with vowel: ', len(vowel_words))


'''
Task 3: WAP to reverse each word of a sentence
and not sentence itself
'''
reverse_words_list =[]
# passage = input("Enter a passage:")
# passage_words = passage.split()
# for words in passage_words:
#     reverse_words_list.append(words[::-1])
# print(' '.join(reverse_words_list))

# list comprehension
reverse_words_list = ' '.join([word[::-1] for word in input("Enter a passage:").split() ])
print((reverse_words_list))

'''
Task 4: get input passage from user and also get max length of
word allowed and print output excluding words having 
greater length than maximum length
'''
input_words = input("enter the passage:").split()
max_allowed = int(input("enter max word length"))
refine = ' '.join([words for words in input_words if len(words) <= max_allowed])
print(refine)