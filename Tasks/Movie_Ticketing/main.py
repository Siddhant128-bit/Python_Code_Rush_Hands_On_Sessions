"""
Movie Ticketing System: 
Users can sign up without any account.
Each user has a unique username, and the system ensures uniqueness.
User history of all previous movies watched is recorded.
After logging in, users can book tickets for available movies.
Users can select seats based on availability.
Once a seat is booked, it becomes unavailable for other users.
Database handling using json/txt file handling 
"""

from art import *
import getpass
import sys


class Movie_Ticketing_Accounts:
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

    def load_movie_data(self):
        try:
            with open("movie_data.txt", "r") as f:
                movies = {}
                for line in f:
                    # Split and store data from file
                    parts = line.strip().split(";")
                    title = parts[0].split(":")[1].strip()
                    available_seats = int(parts[1].split(":")[1].strip())
                    booked_seats = parts[2].split(":")[1].strip().split(",") 

                    movies[title] = {"title": title, "available_seats": available_seats, "booked_seats": booked_seats}
                return movies
        except FileNotFoundError:
            return {}
        except Exception as e:
            print(f"Error loading movie data: {e}")
            return {}

    def save_movie_data(self, movies):
        try:
            with open("movie_data.txt", "w") as f:
                for movie in movies.values():
                    f.write(f"Title: {movie['title']}; Available Seats: {movie['available_seats']}; Booked Seats: {','.join(movie['booked_seats'])}\n")
        except Exception as e:
            print(f"Error saving movie data: {e}")

    def load_booking_history(self):
        try:
            with open("booking_history.txt", "r") as f:
                user_booking_history = {}
                for line in f:
                    # Assign first item in file to username and the rest to movies (using *)
                    username, *movies = line.strip().split(",")
                    user_booking_history[username] = movies
                return user_booking_history
        except FileNotFoundError:
            print("Booking history file not found.")
            return {}
        except Exception as e:
            print(f"Error loading booking history: {e}")
            return {}

    def save_booking_history(self, user_booking_history):
        try:
            with open("booking_history.txt", "w") as f:
                for username, movies in user_booking_history.items():
                    f.write(f"{username},{','.join(movies)}\n")
        except Exception as e:
            print(f"Error saving booking history: {e}")

    def view_watch_history(self):
        user_booking_history = self.load_booking_history()
        if self.credential_username in user_booking_history:
            print("\nMy Watch History: ")
            for movie in user_booking_history[self.credential_username]:
                print(movie)
        else:
            print("\nNo Watch history available.")

    def book_tickets(self):
        movies = self.load_movie_data()
        print("Available movies: ")
        for title in movies:
            print(title)

        movie_title = input("Enter the movie title: ")
        if movie_title not in movies:
            print("Movie not found.")
            return

        movie = movies[movie_title]
        if movie['available_seats'] == 0:
            print("No seats available for this movie.")
            return

        self.display_seats(movie)

        num_seats = int(input("How many seats would you like to book? "))
        if num_seats > movie['available_seats']:
            print("Not enough seats available.")
            return

        for _ in range(num_seats):
            seat_number = input("Enter the seat number (eg A1): ").upper()
            if seat_number not in movie['booked_seats']:
                movie['booked_seats'].append(seat_number)
                movie['available_seats'] -= 1
            else:
                print("Seat already booked. Please choose another one.")
                return
        # Save the updated movie data
        self.save_movie_data(movies)

        user_booking_history = self.load_booking_history()
        if self.credential_username not in user_booking_history:
            user_booking_history[self.credential_username] = [movie_title]
        else:
            user_booking_history[self.credential_username].append(movie_title)
        self.save_booking_history(user_booking_history)
        print("Tickets booked successfully!")

    def display_seats(self, movie):
        tprint(f"Seats for {movie['title']}")
        rows = ["A", "B", "C", "D", "E", "F", "G", "H"]
        columns = range(1, 9)

        print("   ", end="")
        for col in columns:
            print(f"{col} ", end="")
        print()
        for row in rows:
            print(f"{row} ", end="")
            for col in columns:
                seat = f"{row}{col}"
                if seat in movie['booked_seats']:
                    print(" X", end="")
                else:
                    print(" O", end="")
            print()

    def dashboard(self):
        tprint("Dashboard")
        while True:
            choice = int(
                input(
                    f"\nMenu Options:\n1. Book Tickets\n2. View watch history\n3. Quit\nEnter your choice: "
                )
            )
            if choice == 3:
                sys.exit()
            elif choice == 1:
                print("Book Tickets")
                self.book_tickets()
            else:
                self.view_watch_history()

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
            tprint("Q's cinemas")

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
    Movie_Ticketing_Accounts()
