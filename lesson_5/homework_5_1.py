# FOR LOOPS EXERCISES

# Enter your name, save it in name variable and create function print_name_three_times which returns
# value that is equal to your name three times

name_1 = 'Anastasiia'

def print_name_three_times(name):
    pass
    return name_1 * 3


# Modify your previous program so that it will enter your name (save it in variable  name_2) and a number
# (save in variable number) and then display their name that number of times. Each time add your name to result
# variable

name_2 = 'Anastasiia'
number_1 = 3

def print_name_number_times(number, name):
    pass
    return name_2 * number_1


# Enter a random string, which includes only digits. Write function sum_digits which find a sum of digits in this string

string_number_1 = '123456789'

def sum_digits(string, result=0):
    pass
    for char in string_number_1:
       result += int(char)
    return result


# Create function which sums up all even numbers between 2 and 100 (include 100)

def sum_even_numbers():
    pass
    numbers = range(2,101)
    result = 0
    for number in numbers:
        if number % 2 == 0:
            result += number
    return result