# file_variable = open("file.txt", "w")
# user = input("ask for input:")
# file_variable.write(user)
# file_variable.close()


# Approach 2
with open("file.txt", "r") as var:
    var.write('next db')