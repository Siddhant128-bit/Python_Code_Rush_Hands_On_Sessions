# file_variable = open("file.txt", "r")
# database_txt=file_variable.read()
# file_variable.close()
# print(database_txt)

#approach 2
with open("file.txt", "w") as var:
    var=var.read()