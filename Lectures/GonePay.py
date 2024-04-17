'''
Licence info: 
GonePay is our banking app developed in CodeRush.
All the intellectual property belongs to us Engineers.

Personal information: 
    username: 
    password /biometrics:
    total balance: XXX.XXX
    withdraw: total_balance - withdrawn_amount 
    deposit: total_balance + depost_amount
'''
from art import *
import getpass


class Gone_Pay_Accounts: 
    def __init__(self,user_name,password,total_balance):
        tprint('GonePay')
        self.credetentials_1=user_name
        self.credetentials_password_dont_use=password
        self.total_bank_balance=total_balance
    
    def display_information_in_dashboard(self):
        tprint('Dashboard')
        print(f'Username:{self.credetentials_1} \t Total Balance: {self.total_bank_balance} \n ')
        if self.total_bank_balance<=500:
            print('Main Gareeb Hoon ')
        elif self.total_bank_balance>500 and self.total_bank_balance<=10000:
            print('Middle class lago ka dard')
        else: 
            print('Rich Kid')

    def authenticate_information(self,input_username,input_password):
        if input_password==self.credetentials_password_dont_use and input_username==self.credetentials_1:
            print('Successfully logged in')
            self.display_information_in_dashboard()
        else: 
            print('Vag yaha se !')

    def depost_amount(self,deposited_amount):
        self.total_bank_balance+=deposited_amount
        print('After Deposit')

        self.display_information_in_dashboard()

    def withdraw_amount(self,withdrawn_amount):
        self.total_bank_balance-=withdrawn_amount
        print('After withdraw')

        self.display_information_in_dashboard()


laxmi_account=Gone_Pay_Accounts('Laxmi Kumari Joseph','laxmirocks',20)
garib_kumar_account=Gone_Pay_Accounts('Garib Kumar Waiwa','GaribiRocks',5000000)
all_acounts=[laxmi_account,garib_kumar_account]

user_name=input('Enter username: ')
password=getpass.getpass('Enter password: ')

# O(n) complexity try to reduce this to O(1) if possible
# for obj in all_acounts:
#     obj.authenticate_information(user_name,password)

laxmi_account.authenticate_information(user_name,password)
laxmi_account.depost_amount(15000)

garib_kumar_account.display_information_in_dashboard()



         
