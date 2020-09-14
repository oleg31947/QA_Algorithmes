def sum_of_digital(number):
    summ = 0
    while number > 0:
        summ += number % 10
        number //= 10
    return summ






# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6

# 3 way
def recursion_digital_root(number):
    if number >= 10:
        number = sum_of_digital(number)
        return recursion_digital_root(number)
    else:
        return number
print(recursion_digital_root(942))
