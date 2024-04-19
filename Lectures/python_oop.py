'''
Everything is an object for python.

class -> superset consisting of varoius instances
object -> Various unique instances of class

oop is used to give unique instance to various different profiles.

In python we create a class using follwing syntax: 

class class_name: 
    def function_1():
        pass
        
    def function_2():
        pass
        
    

'''

#Class is defined
class Animal:
    def species_selection(self,number_of_legs,can_speak,is_a_baby):
        if number_of_legs==2 and can_speak==True:
            return 'Human'
        elif number_of_legs==4 and can_speak==False and is_a_baby==True:
            return 'Human Baby'
        else: 
            return 'Not Human'




object_1=Animal()
obj_1_output=object_1.species_selection(2,True,True)
print(obj_1_output)

object_2=Animal()
obj_2_output=object_2.species_selection(4,False,False)
print(obj_2_output)

object_3=Animal()
obj_3_output=object_3.species_selection(4,False,True)
print(obj_3_output)


'''
Task 1: Create a calculator app using class and object
'5 + 5', '5 - 5', '5 * 5'
Create 2 instances of calculator app, both instances should have their own history 
when user wants to see the history display the history 
'''
class calculator: 
    def preprocess(self,string_val):
        #Seperate a and b
        if '+' in string_val:
            return string_val.split('+')[0],string_val.split('+')[1]
        elif '-' in string_val:
            return string_val.split('-')[0],string_val.split('-')[1]

    def save_history(self,list_val,op,flag):
        list_val.append(f'{flag} {op}')
        return list_val

    def add(self,input_text,list_val):
        a,b=self.preprocess(input_text)
        op=a+b
        list_val=self.save_history(list_val,op,'SUM')
        return  op,list_val


    def subtract(self,input_text,list_val):
        a,b=self.preprocess(input_text)
        op=a-b
        list_val=self.save_history(list_val,op,'Sub')
        return  op,list_val
    
    def multiply(self,input_text,list_val):
        a,b=self.preprocess(input_text)
        op=a*b
        list_val=self.save_history(list_val,op,'Mul')
        return  op,list_val



calculator_instance_1=calculator()
list_val_instance_1=[]
print('Calculator Instance 1: ')
while True: 
    choice=input('Do want to quit (Y/N): ')
    if choice=='Y':
        break

    input_text=input('>>')
    if '+' in input_text: 
        op,list_val_instance_1=calculator_instance_1.add(input_text,list_val_instance_1)
        print(op)
    


print(list_val_instance_1)
#calculator_instance_2=calculator()

'''
Task 2: Create a class named vehicle, based on number of wheels, Presence of engine
and presense of sterring wheel assign weather its a car, motorbike and cycle (bike) 
'''



