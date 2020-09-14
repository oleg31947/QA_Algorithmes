"""
in class
"""
from random import randint

length = int(input(f"Enter a list length "))
array_1 = []

for i in range(length):
    item = randint(-100, 100)
    array_1.append(item)


def find_max_item_and_its_index_in_list(array):
    maximum = array[0]
    max_index = 0
    index = 0
    while index < len(array):
        if array[index] > maximum:
            maximum = array[index]
            max_index = index
        index += 1
    return {
        "maximum": maximum,
        "max_index": max_index,
        "array": array
    }


print(find_max_item_and_its_index_in_list(array_1))

"""
1.Last problem from slides (Sum of odd numbers)
2.When given a list, the program should return a list of all the elements that are below the arithmetical mean of the original list.  The arithmetical mean is the sum of all elements divided by the number of elements.
3.When given a list of elements find the two lowest elements. They can be equal to each other or different.
4.https://www.hackerrank.com/domains/python

"""