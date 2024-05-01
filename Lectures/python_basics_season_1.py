'''
There are 2 main types of datatype
1. basic data type:
    Basic in nature, They can hold single variable
    They don't need to be traversed.
    examples: 
        integer, float, double,string, boolean

2. Collection Data type:
    Collection of various data types into a single one.
    They need to be traversed and studied in detail
    examples: 
        list, dictionary,set, tuple so on.
'''

# a=10
# print(a,type(a)) #Data type  is integer 

# a='10'
# print(a, type(a)) #Data type is string

# a=10.0
# print(a,type(a)) #Data type is float

# a='10'
# print(a, type(a))
# a=int(a)
# print(a, type(a))


# a='1'
# b='2'

a=True
print(type(a))

# sum_variable=int(a)+int(b) #converted into integer type and did the addition operation
# diff_variable=int(a)-int(b)
# mul_variable=int(a)*int(b)
# division_variable=int(a)/int(b)
# modulus_variable=int(a)%int(b)

# print(sum_variable,diff_variable,mul_variable,int(division_variable),modulus_variable)


#Task 1: Take 2 inputs from user name it input_1 and input_2 then display their sum, difference and product
# #No need to save it in any variable, just display it on runtime
# input_1=float(input('Enter input 1: '))
# input_2=float(input('Enter input 2: '))

# print('Division of 2 numbers is',input_1/input_2,input_1+input_2)
#print(f"Addition of 2 numbers {input_1},{input_2} that's {input_1+input_2}\nSubtraction of 2 numbers")

'''
Collection Data types: 
1. list 
2. Dictionary

It is used to collect multiple datatypes in a single variable.
It can be traveresed, multated / non mutated.

1. List
- denoted with '[' ']'
- new elements can be added using append.
'''

#This is an empty list
list_variable_1=[]
# print(list_variable_1,len(list_variable_1))

#list comprehension method
list_variable_1=[i for i in [1,2]]
# print(list_variable_1,len(list_variable_1))

list_variable_random=[i for i in range(1,101)]
print(len(list_variable_random))
print(max(list_variable_random))
#extend try it out: 
'''
2. Dictionary: 
- Sorted out in the format of keys and values
- O(1) -> Best system O(n)-> One of the worst case O(n**2)
{
    'word (key)': 'meaning (value)'
}
'''
# dictionary_variable={}
# print(len(dictionary_variable),type(dictionary_variable))

dictionary_variable={
    'apple': 'Round and Red Fruit that keeps doctor away'
}
#update can be used to update the value 
'''
Semi Task 1: 
    In the dictionary above dictionary_variable add another word Ball 
    and include its meaning. using update
'''

dictionary_variable.update({'ball': 'A play thing for kids'})
print(dictionary_variable)

print(list(dictionary_variable.keys()))

words=['apple','ball','cat']
meanings=['elppa','llab','tac']
dictionary_variable_2=dict(zip(words,meanings))
print(dictionary_variable_2)

'''
Task 1: 
- Get n from user n -> int(n)
- iterate over n times get student's name and marks 
- student_list should contain list of students and student_marks should contain 
list of marks 
- combine it into a dictionary
- Get the highest marks scored in the class
- Find out who scored that marks  (Assignment)
'''

# n=int(input('Enter value of n: '))
# student_list=[]
# student_marks=[]

# for iter in range(n):
#     print(iter)
#     student_list.append(input('Enter name of student: '))
#     student_marks.append(float(input('Enter marks of student: ')))

# print('Highest marks scored is: ',max(student_marks))
# student_info_dictionary=dict(zip(student_list,student_marks))

# print(student_list,student_marks)


'''
Task 2: 

1. For numbers ranging from 1-100, collect all the even numbers in even_list
odd numebrs in odd_list

1.5. Try it using list comprehension also 

2.Display all even numbers while multiplying them with 10 
'''
#solution to 2.1
even_list=[]
odd_list=[]

for number in range(1,101):
    if number%2==0:
        even_list.append(number)
    else: 
        odd_list.append(number)

#solution to 2.1.5

even_list_comprehension_style=[i for i in range(2,101,2)]
odd_list_comprehension_style=[i for i in range(1,101,2)]

even_list_comprehension_style=[i for i in range(1,101) if i%2==0]

#Solution to 2.2
for element in even_list_comprehension_style:
    print(element*10)



'''
Task 3
Get input from user, untill the user types bye keep showing whatever user types
'''
# while True:
#     user_input=input('>>')
#     if user_input.lower()=='bye':
#         print('Closing the program')
#         break
#     else: 
#         print('output log: ',user_input)

'''
Task 4: 
Get input N from user 
Iterate upto N 
check if a number is divisible by 3 (multiple of 3)
when the count of  divisible numbers  is greater then a number specified by user
terminate the program
Try both while and for loop 

'''

'''
Task 5
Print * pattern 
* 
**
***
****
upto n , n from user 

'''
n=int(input('Enter n '))
for i in range(1,n+1):
    print('*'*i)


# Assignment 1. Get highest scoring person name in dictionary examples
# Assignment 2. Try some leet code and other examples for string manipulation
