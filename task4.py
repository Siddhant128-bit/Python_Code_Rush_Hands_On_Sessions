'''
Task 4: get an input passage from user, and also get the maximum length 
of a word allowed 
and print output excluding words having greater length then maximum length 

input passage: "I eat Rice and I am also working on something"
maximum length: 5
output passage: "I eat Rice and I am also on "

'''

input_passage=input("enter passage: ")
max_length=int(input("enter max length: "))
words=[word for word in input_passage.split() if len(word) <= max_length]
output_passage=' '.join(words)
print(output_passage)