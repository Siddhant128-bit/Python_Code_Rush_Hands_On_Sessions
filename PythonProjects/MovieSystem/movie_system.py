'''
Task 1:
Movie Ticketing System
Functionality:
● Users can sign up without any account.
● Each user has a unique username, and the system ensures
uniqueness.
● User history of all previous movies watched is recorded.
● After logging in, users can book tickets for available movies.
● Users can select seats based on availability.
● Once a seat is booked, it becomes unavailable for other users.
● Database handling using json/txt file handling
'''
import json
class MovieTicketSystem:
    def __init__(self):
        print("\nWelcome to the Movie Ticketing System!!\n")
        try:
            with open('user.json', 'r') as file:
                self.users = json.load(file)
        except FileNotFoundError:
            self.user = {}

        with open('movies.json', 'r') as read_file2:
            self.movies = json.load(read_file2)
            # print(self.movies)
    
    def save_data(self):
        with open('user.json', 'w') as save_file:
            json.dump(self.users, save_file, indent=4)

    def save_movie(self):
        with open('movies.json', 'w') as save_file2:
            json.dump(self.movies, save_file2, indent=4)
            
    def sign_up(self):
        username = input("Enter your username")
        if username in self.users:
            print("username already exists.")
            self.sign_up()
        self.users[username] = {"movie":{}}
        self.save_data()
        print("New user added")
    
    def menu_after_login(self,username):
        print("1. Book Seat\n2. History\n3. Exit")
        choice2 = input("Enter your choice:")  
        if choice2 == "1":
            self.book_seats(username)
        elif choice2 == "2":
            self.load_history(username)
        else:
            return
    
    def login(self):
        username = input("Enter your username")
        if username in self.users:
            print("You successfully logged in!")
            self.menu_after_login(username)
            return
        else:
            print("User not found")

        
    def book_seats(self,username):
        print("Available movies:\n")
        for movie in self.movies:
            print(movie)
        movie = input("\nEnter the movie you want to see")
        if movie in self.movies:
            print(f"Available seats: {self.movies[movie]}")
            seat = input("Enter seat from available seat")
            if seat in self.movies[movie]:
                print("Your seat is booked.")
                self.movies[movie].remove(seat)
                self.users[username]['movie'][movie] = seat
                self.save_data()

                # print(self.movies[movie])
                self.save_movie()
                print(f"Ticket Booked Successfullly for {seat}")
            else:
                print("seat is not available")
                self.book_seats(username)
        else:
            print("movie not available")
            self.book_seats(username)
        
    def load_history(self, username):
        for history in self.users[username]["movie"]:
            print(history, self.users[username]["movie"][history],'\n')
        self.menu_after_login(username) 

movie_system = MovieTicketSystem()
while True:
    print("1. Sign up\n2. Login\n3. Exit\n")
    choice = input("Enter your choice: ")
    if choice == "1":
        movie_system.sign_up()
    elif choice == "2":
        movie_system.login()
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid choice. Please try again.")
print("Thank You for visiting our System!!")


