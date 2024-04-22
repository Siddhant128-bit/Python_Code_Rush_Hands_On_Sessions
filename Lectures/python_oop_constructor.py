#Animal example using constructor.
class Animal: 
    def __init__(self,number_of_legs,can_speak,is_a_baby):
        self.legs_var=number_of_legs
        self.speak_var=can_speak
        self.baby_var=is_a_baby
        print(f'Metadata: \nlegs: {self.legs_var}\nSpeak: {self.speak_var}\nBaby: {self.baby_var}')
        print('=='*25)
    def species_classification(self):
        if self.legs_var==2 and self.speak_var==True:
            return 'Human'
        elif self.baby_var==True:
            return 'Baby'
        else: 
            return "Not Human"


 
object_1=Animal(4,False,False)
print(object_1.species_classification())

object_2=Animal(2,True,False)
print(object_2.species_classification())

object_3=Animal(4,False,True)
print(object_3.species_classification())

'''
Task 2: Create a class named vehicle, based on number of wheels, Presence of engine
and presense of sterring wheel assign weather its a car, motorbike and cycle (bike) 
do it with constructor
'''
