'''
Task 2:
Messaging System / Snap chat
Functionality:
● Users can create account if they don’t have any
● Users can login using their username and password
● User can search for any other users who are available in the app
● One User can message another user and their messages are
stored, don’t save more then 15 conversations
● Any user can delete msg history on their end
● Database handling using json/txt file handling
'''
import json

class MessageApp:
    def __init__(self):
        print("\nWelcome to the Messaging System!!\n")
        try:
            with open('user.json', 'r') as file:
                file_content = file.read()
                if file_content:
                    self.users = json.loads(file_content)
                else:
                    self.users = {}
        except FileNotFoundError:
            self.users = {}
    
    def save_data(self):
        with open('user.json', 'w') as save_file:
            json.dump(self.users, save_file, indent=4)
    
    def create_account(self):
        self.username = input("Enter your username")
        password = input("Enter your password")
        user_data = {'password': password, 'message': {}}
        self.users[self.username] = user_data 
        self.save_data()
    
    def login(self):
        user_name = input("Enter your username: ")
        if user_name in self.users:
            self.username = user_name
            password = input("Enter your password: ")
            if self.users[user_name]['password'] == password:
                print("Successfully Logged in")
            else:
                print("Wrong password")
        else:
            print("Username does not exist")
    
    def search_users(self):
        print("Available users:")
        for user in self.users:
            print(user)
            
        
    def send_message(self):
        self.search_users()
        recipient = input("Enter the recipient's username: ")
        if recipient not in self.users:
            print("Recipient does not exist.")
            return
        message_content = input("Enter your message: ")

        if recipient not in self.users[self.username]['message']:
            self.users[self.username]['message'][recipient] = []
        if self.username not in self.users[recipient]['message']:
            self.users[recipient]['message'][self.username] = []

        message = {
            "sender": self.username,
            "chat": message_content
        }
        if len(self.users[self.username]['message'][recipient]) >= 15:
            self.users[self.username]['message'][recipient].pop(0)
        self.users[self.username]['message'][recipient].append(message)
        self.users[recipient]['message'][self.username].append(message)
        self.save_data()
        print("Message sent successfully.")
        
    def delete_message_history(self):
        recipient = input("Enter the recipient's username to delete message: ")
        if recipient in self.users[self.username]['message']:
            del self.users[self.username]['message'][recipient]
            self.save_data()
            print("Message history deleted successfully.")
        else:
            print("No message history found.") 
    
system = MessageApp()
while True:
    print("\n1.Signup\n2.Login\n3.Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        system.create_account()
    elif choice == "2":
        system.login()
        while True:
            print("\n1.Search Users\n2.Send Message\n3.Delete message History\n4.Back")
            ch = input("Enter your choice: ")
            if ch == "1":
                system.search_users()
            elif ch == "2":
                system.send_message() 
            elif ch == "3":
                system.delete_message_history()
            elif ch == "4":
                break
    elif choice == "5":
        print("Exiting...")
        break
    else:
        print("Invalid choice.")
