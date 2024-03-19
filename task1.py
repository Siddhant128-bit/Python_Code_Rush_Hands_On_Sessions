'''
Task 1, write a program that basically isolates N (input from user) 
number of even numbers into a list and then gets me the sum of N even numbers
'''

even_list=[]
number_list=[]
n=int(input("enter a number of even numbers you want to insert: "))
for _ in range(n):
    i=int(input("enter a number: "))
    number_list.append(i)
    if i%2==0:
        even_list.append(i)
print(even_list)
print(sum(even_list))