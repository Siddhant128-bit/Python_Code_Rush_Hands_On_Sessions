'''
Write a program to basically reverse each word of a sentence (user provided) and not the sentence itself

'''
user_input = input("Enter a sentence: ").split()
reverse_sentence = ' '.join(word[::-1] for word in user_input)
print(f"Sentence after reverse: \n{reverse_sentence}")

