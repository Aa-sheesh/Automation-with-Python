admin = "Aashish"
print("Enter your name")
name = input()


def authenticate(name):
    if name == admin:
        print("Hello, Admin")
        print("Enter your password:")
        password = input()
        if password == "peedhu483":
            print("Welcome Admin")
        else:
            print("Sorry, wrong password")
    else:
        print("Sorry, you are not admin")


authenticate(name)
