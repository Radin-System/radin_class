
username_correct = "admin"
password_correct = "1234"

attempts = 3

while attempts > 0:
    username = input("Username: ")
    password = input("Password: ")
    
    if username == username_correct and password == password_correct:
        print("\n Wellcome")
        break
    else:
        attempts -= 1
        if attempts > 0:
            print(f" wronge password {attempts} one more chance\n")
        else:
            print("\n system lock")
