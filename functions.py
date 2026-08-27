PI = 3.14

def average(numbers, float_digits = 2):
    for number in numbers:
        if number > 20 or number < 0:
            print('Error: numbers should be between 0-20')
            return 'Error'

    result = round(sum(numbers) / len(numbers), float_digits)
    return result
