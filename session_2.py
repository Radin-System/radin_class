# Array

# tak bakhshi
# list
# 1. Tartib Dare --> Tartib moheme
# 2. Mishe Meghdare Tekrari Dakhelesh Gozash
# 3. mutable --> Ghabel Taghir
# 4. iterable
numbers_list = [1, 2, 3, 4, 4, 1, 3, 5]
#               0  1  2  3  4  5  6  7
#              -8 -7 -6 -5 -4 -3 -2 -1

# Tuple
# 1. Tartib Dare
# 2. mitoone Takrari
# 3. Immutable --> Taghir Nemikone
# 4. iterable
numbers_tuple = (1, 2, 3, 4, 5, 6)
#                0  1  2  3  4  5
#               -4 -5 -4 -3 -2 -1

# Set
# 1. Tartib Nadare
# 2. Tekrari Nadare
# 3. Mutable
# 4. iterable
numbers_set = {1, 2, 3, 4, 5, 6, 2, 1, 4}


# do bakhshi
# Dict
# key: value
# 1. Tartib Dare
# 2. Tekrari Nadare
# 3. Mutable
student = {
    'name': 'ali',
    'last_name': 'alavi',
    'age': 18,
    'phone': '9195612345'
}

books = {
    1: 'Dini',
    3: 'riyazi',
    146328: 'Azmayeshgah',
}

conditions = {
    True: 'It is ok',
    False: 'Not OK'
}


print(numbers_list[1:3])
print(numbers_tuple[0])
print(numbers_set)
print(student['last_name'])
print(books[3])
print(conditions[True])

# Hichi
null = None


# Method --> Ghaeliyate yek Var
name = 'mohammad heydari'

print(4 + 2)
print(4 - 2)
print(4 * 2)
print(4 ** 2)
print(4 / 2)
print(4 // 2)
print(5 % 2)
print((1+2)*3)
print([1, 2] + [2, 4])
print((1, 2) + (3, 4))
print({1, 2}.union({2, 3}))

# type --> Tabdil
# type conversion
int()
float()
bool()
str()
bytes()
list()
tuple()
set()
dict()

number = int('43')
# print(type(number))

is_ok = bool()
print(is_ok)

name = 'Mohammad'
name_letters = dict(
    [
        ('name', 'ali'),
        ('family', 'alavi'),
    ]
)


print(name_letters)
