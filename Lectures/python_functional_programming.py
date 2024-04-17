
'''
function
z(x)
y= f(x) (2x+3) (x=1)
y=g(x) (3x+2) (X=2)

#scope of variables defines from where till where the variable exists

Function has 2 parts: 
1. defintion (define what that specific funtion does)
2. Call (using that function with certani parameter/argument )

Can define empty function as well 
def function_name(arg1,arg2):
    pass

Function has 2 types: 
1. return type function 
2. non return type function

'''

#Basic funciton
def function_name(arg1,arg2):
    print(arg1,arg2)

#Non return function 
def display_10_numbers_from_n(n):
    for i in range(n,n+11,1):
        print(i)

def display_and_grab_10_numbers_from_n(n):
    output_list=[]
    for i in range(n,n+11,1):
        output_list.append(i)
    return output_list

#main flow of program
#display_10_numbers_from_n(10)
#numbers_from_something=display_and_grab_10_numbers_from_n(10)
#print(numbers_from_something)


def main():
    def some_other_main():
        print('hello world nested')

    print('hello world')
    some_other_main()

# def fibonaci(kasdflasdf):
#     if n==0:
#         return 1
#     else: 
#         return fibonaci()
    

'''
Task 1: Create a function that takes in Principle time and Rate and returns SI 
Task 2: Make it such that the function doesn't return SI just displays it 
'''

def calculate_simple_Interest(P,T,R):
    return (P*T*R)/100



#print(calculate_simple_Interest(1000,1,10))

'''
Task 3: Write a function that takes in Multiply_number and multiply_upto argumenets where Muliply_number's multipilication table is
displayed untill multiply_upto

output->5x1=5
        5x2=10
        5x3=15


by default mulitply_upto should be 10 and multiply_number should be 1

'''
#Imbalance parameter errors: 
# 1. Default value setttings

def bacha_lai_sikaune_multiplication_table(klai_multiply_garne=1,kati_samma_multiply_garne=10):
    for number in range(kati_samma_multiply_garne+1):
        print(f'{klai_multiply_garne} X {number} = {klai_multiply_garne*number}')


#bacha_lai_sikaune_multiplication_table(2,20)

#2. Args and kwargs
'''
Task 4: Create a function which takes in N number of variables and returns their sum (N=random)
'''
#x=[1,2,3,4,5]
def sum_of_n_numbers(*numbers_tuple):
    return sum(list(numbers_tuple))
    #print(numbers_tuple)

# # N =5

# print(sum_of_n_numbers(1,2,3,4,5))


# #N=7
# print(sum_of_n_numbers(6,7,8,9,10,11,12))

# #N=3
# print(sum_of_n_numbers(1,2,3))

# print(sum_of_n_numbers())

'''
Task 5: Create a function that takes in username, password ,DOB,phone_number,from user and creates a dictionary from it with and without using kwargs
'''

def user_credentials_without_using_kwargs(user_name,password,DOB):
    return_dictionary={}
    return_dictionary['user_name']=user_name
    return_dictionary['password']=password
    return_dictionary['DOB']=DOB
    return return_dictionary

def user_credentials_using_kwargs(**result_dictionary):
    return result_dictionary


storage_data=user_credentials_without_using_kwargs('Siddhant','asdf','1234')
#print(storage_data)
#print('--'*25)
storage_data_new=user_credentials_using_kwargs(user_name='Siddhant',password='asdf',DOB='1234',phone_number='909090')
#print(storage_data_new)


'''
Task 6: Create a function named Calculator that takes a string '5+5' and basically can return 10 in the same case '5-5' returns 0 
and all that, All other operations should take place as function within the calculator function 
'''

def Calculator():
    def addition(operators):
        return int(operators[0])+int(operators[1])

    def subtraction(operators):
        return int(operators[0])- int(operators[1])

    def multiply(operators):
        return int(operators[0]) * int(operators[1])

    def divide(operators):
        try:
            return int(operators[0]) / int(operators[1])
        except:
            return 'Not possible'

    user_input=input('>> ')
    if '+' in user_input:
        return (addition(user_input.split('+')))
    
    elif '-' in user_input: 
        return(subtraction(user_input.split('-')))
    
    elif '*' in user_input: 
        return(multiply(user_input.split('*')))
    else: 
        return(divide(user_input.split('/')))

#print(Calculator())

'''
Task 7: Create a programming langage called Gara_Sathi
Initially the compiler should greet you with Gara_Sathi Developed by: Version no: 
if we type function 'feri_vetaula()' the CLI should end
also create default functions as Joda_Sathi(a,b) returns sum of 2 numbers and displays it 
another default function as vana_sathi(a) returns a and displays it
'''



'''
Lambda Funciton: Anonymous Function
Lambda function can take in any numbers of arguements/parameters but has single expression
x= lambda argument/parameter : expression
now x becomes a function name
'''
x=lambda a,b,c: a+b+c
print(x(1,4,5))


def multiply_till(n):
    return lambda a: a*n

multiply_till_5=multiply_till(5)
print(multiply_till_5(10))

multiply_till_10=multiply_till(10)
print(multiply_till_10(10))

#Do Task 3 using lambda 