# module

## 1. built-in
## 2. User defined
## 3. 3rd Party
import os
import sys
import datetime

from datetime import date
from sys import exit

from functions import average

from helpers import create_database_string
from helpers import create_path
print(create_database_string("127.0.0.1", 8081))

import requests

response = requests.get(url='http://google.com')
print(response)

# Packing & Unpacking

name = 'mohammad'
last_name = 'heydari'
age = 27


name, last_name, age = ('mohammad', 'heydari', 27)

students = [
    ('Mohammad', 'Heydari'),
    ('Reza', 'Rezayi'),
    ('Ali', 'Alavi'),
]

for name, last_name in students:
    print(name, last_name)


def my_func(*names):
    print(names)

    for name in names:
        print(name)


my_func('mohammad', 'reza', 'ali')

students = {
    '1234': {
        'first_name': 'mohmmad',
        'last_name': 'heydari',
    },
    '4321': {
        'first_name': 'ali',
        'last_name': 'alavi',
    }
}


for code, student in students.items():
    print(f"{code}, {student["first_name"]} {student["last_name"]}")
