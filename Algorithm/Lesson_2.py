
# TODO: HW: Rewrite code, which will return only needed element of Fib sequence
def fibonacci(n):
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
print(fibonacci(8))

# TODO Use datetime library to solve problem Seconds to Date
def sec_to_hms(seconds):
    # hours = seconds // 3600
    minutes = seconds // 60
    seconds = seconds - minutes * 60
    # return f'{hours}:{minutes}:{seconds}'
    return seconds
print(sec_to_hms(63))



# # 1450 -> 145
print(1450 // 10)

# # 960000 -> 96
print(96000 // 1000)

# # 1050 -> 105
print(1050 // 10)

# # -1050 -> -105
print(-1050 //10)


# Digital root is the recursive sum of all the digits in a number.

# Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# This is only applicable to the natural numbers.

# 16  -->  1 + 6 = 7
def sum_of_digital(number):
    summ = 0
    while number > 0:
        summ += number % 10
        # k += p
        number //= 10
    return summ


def digital_root(number):
    while number > 10:
        number = sum_of_digital(number)
    return number

print(digital_root(942))

# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6

# 3 way
def recursion_digital_root(number):
    if number >= 10:
        number = sum_of_digital(number)
        return recursion_digital_root(number)
    else:
        return number

x = str(942)
r = 0
while len(x) > 1:
    r = 0
    for i in range(len(x)):
        r = r + int(x[i])
    x = str(r)
print(r)

# second way


# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

str_n = str(493193)
n = 0
while len(str_n) > 1:
    n = sum(int(x) for x in str_n)
    str_n = str(n)
print(n)



