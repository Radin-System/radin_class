users = {
    "mammad": "1234",
    "akbar": "1111",
    "asghar": "2222",
    "yaser": "3333"
}

attempts = 0

while attempts < 3:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username in users and users[username] == password:
        print("\nLogin successful!")
        print("Welcome to the system.")
        break
    else:
        attempts += 1
        print("\nInvalid username or password.")
        print(f"Remaining attempts: {3 - attempts}")

if attempts == 3:
    print("\nYou have entered incorrect information 3 times.")
    print("Program terminated.")