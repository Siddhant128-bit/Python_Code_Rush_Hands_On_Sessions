'''
Task 3
Write a program to basically reverse each word of a sentence (user provided) and not the sentence 
itself

Input Sentence: I eat rice
Output Sentence: I tae ecir
'''

input_sentence=input("enter a sentence: ")
reverse_words=' '.join(word[::-1] for word in input_sentence.split())
print(reverse_words)
