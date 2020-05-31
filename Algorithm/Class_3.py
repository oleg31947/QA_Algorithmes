"""
1.Create a tuple containing the names of five countries and display the whole tuple.
Ask the user to enter one of the countries that have been shown to them and then display the index number
(i.e. position in the list) of that item in the tuple.
"""
countries = ('Russia', 'USA', 'Ukraina', 'Litva', 'Germany')
i = input("Pl. choose a country from 'countries': ")
index_your_counrty = countries.index(i)
print("Index of your country is: " + str(index_your_counrty))

"""
2.Add to the previous program to ask the user to enter a number and display the country in that position. 
"""
j = int(input("Pl. enter a number from 0 to 4: "))
country = countries[j]
print("Your country is: " + country)

"""
3.Write a Python script to add a key to a dictionary.
Sample Dictionary : {0: 10, 1: 20}
Expected Result : {0: 10, 1: 20, 2: 30}
"""
i = {0: 10, 1: 20}
i[2] = 30
print(i)

"""
4.Write a Python program to iterate over dictionaries using for loops. 
"""
j = {0: 10, 1: 20, 2: 30}
for kay, value in j.items():
    print(kay, value)

"""
Write a Python script to merge two Python dictionaries.
"""
j = {0: 10, 1: 20, 2: 30}
i = dict(car = "Mersedess", driver = "Misha", sity = "Seattle")
j.update(i)
print(j)

"""
Write a Python program to remove duplicates from the Dictionary. 
"""
j = {0: 10, 1: 20, 2: 30, 0:10, 3:45, 4:50, 5:50}
i = {}
for key, value in j.items():
    if value != i.values():    # second way : value not in v.values():
        i[key]= value
print(i)

"""
Write a Python program to remove spaces from dictionary keys. 
"""
j = {'P 0': 10, 'S  1': 20, 'DF   2': 30, 'U 3':45, 'LI4':50, 'CDD   5':50}
i = {k.replace(' ', ''): v for k, v in j.items()}
print(i)

"""
Write a Python program to get the maximum and minimum value in a dictionary.
"""
j = {0: 10, 1: 20, 2: 30, 3:45, 4:50, 5:50}
print(max(j.values()))
print(min(j.values()))

"""
Write a Python program to check a dictionary is empty or not. 
"""
j = {0: 10, 1: 20, 2: 30, 3:45, 4:50, 5:50}
if len(j) == 0:
    print("Dictionary is empty")
else:
    print("Dictionary is not empty")


"""
Write a Python program to combine two dictionary adding values for common keys. 
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})
"""
sum = {}
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
for k,v in d1.items():
    for k1,v1 in d2.items():
        if k == k1:
            sum[k] = (v + v1)
print(sum)

"""
Write a Python program to print a dictionary line by line.  
"""
j = {0: 10, 1: 20, 2: 30, 3:45, 4:50, 5:50}
for k,v in j.items():
    print({k:v})



