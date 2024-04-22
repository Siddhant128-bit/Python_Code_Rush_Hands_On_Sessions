import json

class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

class Message:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content

class MessagingSystem:
    def __init__(self):
        self.users = self.load_users()
        self.messages = []

    def load_users(self):
        try:
            with open('users.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return {}

    def save_users(self):
        with open('users.json', 'w') as file:
            json.dump(self.users, file)

    def create_account(self, username, password):
        if username in self.users:
            print("Username already exists. Please choose a different one.")
            return False

        self.users[username] = password
        self.save_users()
        print("Account created successfully!")
        return True

    def login(self, username, password):
        if username not in self.users or self.users[username] != password:
            print("Invalid username or password.")
            return False

        print("Login successful!")
        return True

    def search_users(self, keyword):
        found_users = [user for user in self.users if keyword.lower() in user.lower()]
        print("Found Users:")
        for user in found_users:
            print(user)

    def send_message(self, sender, receiver, content):
        message = Message(sender, receiver, content)
        self.messages.append(message)

        # Maintain only the latest 15 conversations
        if len(self.messages) > 15:
            self.messages = self.messages[-15:]

        print(f"Message sent from {sender} to {receiver}")

    def delete_message_history(self, username):
        self.messages = [msg for msg in self.messages if msg.sender != username and msg.receiver != username]
        print(f"Message history deleted for user {username}")

def main():
    messaging_system = MessagingSystem()

    while True:
        print("\nMessaging System:")
        print("1. Create Account")
        print("2. Login")
        print("3. Search Users")
        print("4. Send Message")
        print("5. Delete Message History")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            messaging_system.create_account(username, password)
        elif choice == '2':
            username = input("Enter your username: ")
            password = input("Enter your password: ")
            messaging_system.login(username, password)
        elif choice == '3':
            keyword = input("Enter keyword to search users: ")
            messaging_system.search_users(keyword)
        elif choice == '4':
            sender = input("Enter sender username: ")
            receiver = input("Enter receiver username: ")
            content = input("Enter message content: ")
            messaging_system.send_message(sender, receiver, content)
        elif choice == '5':
            username = input("Enter your username: ")
            messaging_system.delete_message_history(username)
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
