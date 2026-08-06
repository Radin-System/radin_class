# Operator -> math
# + - * ** / //
# Operator -> Logical
print(5 > 2)
print(2 < 4)
print(5 >= 2)
print(4 <= 4)

print(5 == 5)
print(5 in [1, 2, 3, 4, '5'])
print(4 is None)

print(True and True)

national_code = input('Enter National Code: ')

# Shart
if bool(national_code) and len(national_code) == 10:
    # Indentation
    print('Hesab Baz Shod')

else:
    print('Code meli eshtebah ast')

account_numbers = [
    1378472,
    1748521,
    1374516,
    1111111,
]

account_number = input('Enter Account Number: ')


if account_number.isdigit():
    if int(account_number) in account_numbers:
        print('Welcome')

    else:
        print('Wrong Account')

else:
    print(f'Invalid integer: {account_number}')

national_code = input('National Code: ')
national_id = input('National ID: ')

if national_id and national_code:
    print('Both are provided')

elif national_id:
    print('National ID is Provided no sign required.')

elif national_code:
    print('Natianal Code is Provided plese sign.')

else:
    print('No Input Detected')

if True:
    # Do this later
    pass

print('Salam')

# Loop --> Halghe
# 1. while  -> shart

x = 0
while x < 10:
    x = x + 1
    if x == 4:
        continue

    print(x)

    if x == 10:
        break

else:
    print('End')


account_numbers = [
    1378472,
    1748521,
    1374516,
    1111111,
]

tries = 0

while tries < 3:
    account_number = input('Enter Account Number: ')
    tries = tries + 1

    if account_number.isdigit():
        if int(account_number) in account_numbers:
            print('Welcome')
            break

        else:
            print('Wrong Account')

    else:
        print(f'Invalid integer: {account_number}')


else:
    print('Please try again later')

# 2. for    -> iterable

names = [
    'Mohammad Heydari',
    'Saeid Heydari',
    'Alireza Bolandi',
    'Parham Khodadad',
    'Amirreza Amini',
]

for name in names:
    if name == 'Parham Khodadad':
        continue

    print(name)

else:
    print('End')


for i in range(10):
    for y in range(10):
        print(f'{i}, {y}')

students_scores = {
    'Mohammad Heydari': (10, 5, 6),
    'Saeid Heydari': (20, 20, 20, 20),
    'Alireza Bolandi': (14, 17, 4, 2),
    'Parham Khodadad': (19, 13, 17, 11, 5, 20),
    'Amirreza Amini': (11, 14, 3, 19, 20),
}

averages = []

for name, scores in students_scores.items():
    scores = students_scores[name]

    score_sum = sum(scores)
    avg = score_sum / len(scores)
    averages.append(avg)
    print(f'{name}: {round(avg, 2)}')

else:
    print(
        'Class Average:',
        round(sum(averages) / len(averages), 2)
    )
