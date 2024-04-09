"""
Messaging System / Snap chat  
Users can create account if they donot have any 
Users can login using their username and password 
User can search for any other users who are available in the app 
One User can message another user and their messages are stored, do not  save more then 15 conversations 
Any user can delete msg history on their end 
Database handling using json/txt file handling
"""

from art import *
import getpass
import sys


class Messaging_System_Accounts:

    def load_user_data(self):
        try:
            with open("user_data.txt", "r") as f:
                user_data = {}
                for line in f:
                    # Remove whitespaces and split
                    username, password = line.strip().split(",")
                    # Username is key and password is value
                    user_data[username] = password
                return user_data
        # Return empty dictionary if file does not exist
        except FileNotFoundError:
            return {}
        except Exception as e:
            print(f"Error: {e}")

    def sign_up(self):
        self.credential_username = input("Enter username: ")
        self.credential_psw_dont_use = getpass.getpass("Enter password: ")
        user_data = self.load_user_data()

        # Check if username already exists
        if self.credential_username in user_data:
            print("Username already exists. Please choose another username.")
        else:
            with open("user_data.txt", "a") as f:
                f.write(f"{self.credential_username},{self.credential_psw_dont_use}\n")
                print("Signed up successfully!")

    def search_user(self, username, user_data):
        return username in user_data

    def load_chats(self):
        try:
            with open("chats.txt", "r") as f:
                chats_str = f.read()
                chats = chats_str.split("\n")
                return chats
        except FileNotFoundError:
            return []

    def save_chats(self, chats):
        chats_str = "\n".join(chats)
        with open("chats.txt", "w") as f:
            f.write(chats_str)

    def parse_messages(self, message):
        parts = message.split(", ")
        sender = parts[0].split(": ")[1]
        receiver = parts[1].split(": ")[1]
        message_content = parts[2].split(": ")[1]
        return sender, receiver, message_content

    def send_message(self):
        user_data = self.load_user_data()
        receiver = input("Enter username of the recipient: ")
        if self.search_user(receiver, user_data):
            message = input("Enter message: ")
            message_data = f"Sender: {self.credential_username}, Receiver: {receiver}, Message: {message}"
            chats = self.load_chats()
            # Add the new message to chats
            chats.append(message_data)
            # Filter chats for sender-receiver and keep the recent 15 only
            sender_receiver_pair = (
                f"Sender: {self.credential_username}, Receiver: {receiver}"
            )
            sender_receiver_chats = [
                chat for chat in chats if sender_receiver_pair in chat
            ][-15:]

            # Save other chats 
            chats = [chat for chat in chats if sender_receiver_pair not in chat]

            # Recent sender-receiver chats and other chats
            chats += sender_receiver_chats

            self.save_chats(chats)
            print("Message sent successfully!")
        else:
            print("Recipient username not found.")

    def delete_message(self, chats):
        try:
            index_to_delete = int(input("Enter the index of the message to delete: "))
            if index_to_delete < len(chats):                        
                chats.pop(index_to_delete-1)
                print("Message deleted.")
                self.save_chats(chats)
                return
            else:
                print("Invalid message index.")
        except ValueError:
            print("Invalid input! Please enter a valid index.")


    def view_message_history(self):
        user_data = self.load_user_data()
        search_username = input("Enter username to view chat: ")
        if self.search_user(search_username, user_data):
            chats = self.load_chats()
            if chats:
                chat_dict = {}
                for chat in chats:
                    sender_name, receiver_name, message_content = self.parse_messages(chat)
                    # Determine whether the current user sent or received the message
                    if (sender_name == self.credential_username and receiver_name == search_username):
                        target_username = receiver_name
                    elif (sender_name == search_username and receiver_name == self.credential_username):
                        target_username = sender_name
                    # Irrelevant message
                    else:
                        continue

                    # Store message in the dictionary
                    if target_username not in chat_dict:
                        chat_dict[target_username] = []

                    chat_dict[target_username].append(f"Sender: {sender_name}, Receiver: {receiver_name}, Message: {message_content}")

                if chat_dict:
                    print("\nMessage History:")
                    for username, messages in chat_dict.items():
                        print(f"With User: {username}")
                    for i, message in enumerate(messages, 1):
                        sender, _, message_content = self.parse_messages(message)
                        if sender == self.credential_username:
                            print(f"{i}. You: {message_content}")
                        else:
                            print(f"{i}. {sender}: {message_content}")

                    choice = input("Press 1 to delete a message or press enter to continue: ")
                    if choice == "1":
                        self.delete_message(chats)
            else:
                print("No chat history.")
        else:
            print("User not found!")

    def dashboard(self):
        tprint("Dashboard")
        print(f"Currently signed in as: {self.credential_username}")
        while True:
            choice = int(
                input(
                    f"\nMenu Options:\n1. Send a message\n2. View chat history \n3. Quit\nEnter your choice: "
                )
            )
            if choice == 3:
                sys.exit()
            elif choice == 1:
                self.send_message()
            elif choice == 2:
                self.view_message_history()
            else:
                print("Invalid choice. Please enter a valid option.")

    def sign_in(self):
        tprint("Sign in: ")

        input_username = input("Enter username: ")
        input_password = getpass.getpass("Enter password: ")

        user_data = self.load_user_data()

        if input_username in user_data and user_data[input_username] == input_password:
            self.credential_username = input_username
            print("Signed in successfully!")
            self.dashboard()
        else:
            print("Invalid credentials! Try again!")

    def __init__(self):
        while True:
            tprint("Bubble Chat")

            choice = int(
                input(
                    "Menu Options:\n1. Signup\n2. Sign in\n3. Quit\nEnter your choice: "
                )
            )
            if choice == 1:
                self.sign_up()
            elif choice == 2:
                self.sign_in()
            elif choice == 3:
                print("See you later!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")


if __name__ == "__main__":
    Messaging_System_Accounts()
