from random import randint

# n = randint(100, 999)
# print(n)

# 1. Sum of 3 modifiedhttp:
# TODO: Homework: Rewrite a program with any number of digits.
#  Instead of  3 digits, you should sum digits up from n digits number,
#  Where  User enters n manually. n > 0

i = int(input("Enter 3 digit number "))

ones= i % 10

tens = i // 10 % 10

hundreds = i // 100

i = ones + tens + hundreds

print(f'Amount of this numbers is: {i}')


# Find max number from 3 values, entered manually from a keyboard


j = input("Enter 3 values:  ")

b = j.split(',')

numbers = list(map(int, b))

numbers.sort()


print(f'Max number of 3 is: {numbers[-1]}')


# Count odd and even numbers.  Count odd and even digits of the whole number. E.g, if entered number 34560, then 3 digits will be even (4, 6, and 0)  and  2 odd digits (3 and 5).

j = input("Enter your long number ")

c = ' '.join(j).split()

print(c)

odd = []

even = []

for i in c:
    if int(i) % 2 ==0:
        even.append(i)
    else:
        odd.append(i)

print('All odd numbers are: ' + str(','.join(odd)))
print(f'All even numbers are: {even}')

# second way

j = int(input("Enter your long number "))

odd = []
even = []

while j > 0:

    rem = j % 10

    if rem % 2 == 0:

        even.append(rem)

    else:

        odd.append(rem)

    j //= 10
print(f'All even numbers are: {even}')
print(f'All odd numbers are: {odd}')

# Codewars.com (3-4 problems)

