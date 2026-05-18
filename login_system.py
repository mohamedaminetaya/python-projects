username = "AMINE22"
password = "Amine@2007"

success = False

for i in range(1, 4):

    user__name = input("Enter username: ")
    pass__word = input("Enter password: ")

    if user__name == username and pass__word == password:
        print("Login successful")
        success = True
        break

    else:
        print("Incorrect informations")

if success == False:
    print("Account locked")
