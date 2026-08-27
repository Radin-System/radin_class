users = {
    'admin': {'password': 'admin'},
    'user': {'password': 'asd@123'},
}

authorized = False


while True:
    if not authorized:
        username = input('username: ')
        password = input('password: ')

        if username in users and users[username]['password'] == password:
            authorized = True
            print("Access Granted")

        else:
            print("Wrong username or password")

    else:        
        command = input(">>")

        if command == 'exit':
            break

        if command == 'logout':
            authorized = False

        if command == 'add_user':
            username = input('username: ')

            if username in users:
                print('User already exists')
                continue

            password = input('password: ')
            re_password = input('re_password: ')

            if password == re_password:
                users[username] = {'password': password}

            else:
                print(f'Password did not match')

        if command == 'show_users':
            for user in users:
                print(user)
