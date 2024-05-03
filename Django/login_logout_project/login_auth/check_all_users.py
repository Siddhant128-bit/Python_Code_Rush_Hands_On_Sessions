# Import the User model
from django.contrib.auth.models import User

# Retrieve all users
all_users = User.objects.all()

# Print or process the list of users
for user in all_users:
    print(user.username)  # Example: Print the username of each user
