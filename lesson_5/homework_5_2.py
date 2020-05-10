# WHILE LOOPS EXERCISES

# Enter a random string in the variable string_1, then enter a character and save it in the variable char_1.
# Write function counter, which will count how many times your character is included in your string

string_1 = 'I love myself'
char_1 = 'm'

def counter(string, char,count=0):
    pass
    for char in string_1:
        if char == char_1:
            count = count + 1
    return count


# Enter a random number and save it in variable number_1. Then create a function number_multiplication
# that will multiply all the digits together and return the result.

number_1 = 123

def number_multiplication(number, result = 1):
    pass
    for char in str(number_1):
        result = result * int(char)
    return result



# Enter a random number and save it in variable number_2. Then create function number_reverse which will return
# a number with digits of number_1 in reverse order

number_2 = 896
def number_reverse(number):
    pass
    num_string = str(number_2)
    index = len(num_string)
    result = ''
    while index > 0:
        result += num_string[index-1]
        index -= 1
    return int(result)