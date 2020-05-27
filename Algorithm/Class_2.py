"""
1.Ask the user to enter their name and then display their name three times.
"""
i = input("What's your name? ")
print(i.capitalize().split( ) * 3)

"""
2.Alter program 1 so that it will ask the user to enter their name 
and a number and then display their name that number of times. 
"""
i = input("What's your name? ")
j = int(input("What's your number? "))
print(i.capitalize()*j)

"""
3.Ask the user to enter their name and display each letter in their name on a separate line. 
"""
i = input("What's your name? ")
for j in i:
    print(j.capitalize())


"""
4.Change program 3 to also ask for a number. Display their name (one letter at a time on each line) 
repeat this for the number of times they entered. 
"""
name = input("What's your name? ")
numbers = int(input("What's your number? "))
# k = [j*letter for letter in i]
repeat = 0
while repeat < numbers:
    index = 0
    while index < len(name):
        print(name[index].capitalize())
        index +=1
    repeat +=1

"""
5.Ask the user to enter their name and a number. If the number is less than 10, 
then display their name that number of times; otherwise display the message “Too high” three times. 
"""
i = input("What's your name? ")
if 10 > len(i):
    print(i.capitalize()*len(i))
else:
    print(f'Too high {i*3}')
print(len(i))


"""
6. Set a variable called total to 0. Ask the user to enter five numbers and after each input ask them
if they want that number included. If they do, then add the number to the total. If they do not want it included,
don’t add it to the total.
After they have entered all five numbers, display the total.
"""
j = input('Please enter five numbers: ')
d = input("Do you want to that number included?(y/n) ")
while d.lower() != "y":
    j = input('Please enter five numbers: ')
    d = input('Do you want to that number included? ')
else:
    b = 0
    index = 0
    while index < len(j):
        b += int(j[index])
        index += 1
    print(b)


"""
7.Ask which direction the user wants to count (up or down). If they select up,
then ask them for the top number and then count from 1 to that number.
If they select down, ask them to enter a number below 20 and then count down from 20 to that number.
If they entered something other than up or down, display the message “I don’t understand.
"""
a = 0
i = input("Do you want to count (up or down)? ")
if i.lower() == "up":
    j = int(input("Please choose the top number "))
    for k in range(1, j+1):
        a = k
        print(a, end='')
elif i.lower() == "down":
    j = int(input("Please enter a number below 20 "))
    for k in reversed(range(j, 21)):    # second way range(20, j-1, -1)
        a = k
        print(a, end='')
else:
    print("I don’t understand")


"""
8.Ask how many people the user wants to invite to a party. 
If they enter a number below 10, ask for the names and after each name display “[name] has been invited”. 
If they enter a number which is 10 or higher, display the message “Too many people”. 
"""
i = int(input("How many people the user wants to invite to a party? "))
p = 0
if i<10:
    while p < i:
        j = input("What is his(her) name? ")
        print(j.capitalize() + " has been invited!")
        p += 1
else:
    print("Too many people")

"""
9.Set the total to 0 to start with. While the total is 50 or less, ask the user to input a number. 
Add that number to the total and print the message “The total is… [total]”. 
Stop the loop when the total is over 50. 
"""
i = int(input("Could you enter a number? "))
while i <= 50:
    i = int(input("Could you enter a number? "))
else:
    print("The total is " + str(i))


"""
10.Ask the user to enter a number. Keep asking until they enter 
a value over 5 and then display the message “The last number you entered was a [number]” and stop the program.
"""
i = int(input("Could you enter a number? "))
while i <= 5:
    i = int(input("Could you enter a number? "))
else:
    print(f'The last number you entered was a {i}')

"""
11.Ask the user to enter a number and then enter another number. 
Add these two numbers together and then ask if they want to add another number. 
If they enter “y", ask them to enter another number and keep adding numbers until they do not answer “y”. 
Once the loop has stopped, display the total. 
"""

i = input("Please, enter your number: ")
j = input("Please, enter another number: ")
sum = int(i) + int(j)
print("Total number is: " + str(sum))
k = input("Would you like to add another number?(y/n). ")
while k.lower() == "y":
    i = input("Please, enter your number: ")
    j = input("Please, enter another number:  ")
    sum = int(i) + int(j)
    print("Total number is: " + str(sum))
    k = input("Would you like to add another number?(y/n). ")

"""
12.Ask for the name of somebody the user wants to invite to a party. 
After this, display the message “[name] has now been invited” and add 1 to the count. 
Then ask if they want to invite somebody else.
Keep repeating this until they no longer want to invite anyone else to the party and 
then display how many people they have coming to the party. 
"""
p = 0
i = input("Could you give me your friend's name to invite his(her) to a party? ")
print(i.capitalize() + " has now been invited.")
p += 1
j = input("Would you like to invite to the party someone else?(y/n)? ")
# if j.lower() == "y":
while j.lower() == "y":
    i = input("Could you give me your friend's name to invite his(her) to a party? ")
    print(i.capitalize() + " has now been invited.")
    p += 1
    j = input("Would you like to invite to the party someone else?(y/n)? ")
    print("Total guests" + str(p))

"""
13.Ask the user to enter a number between 10 and 20. If they enter a value under 10, 
display the message “Too low” and ask them to try again. If they enter a value above 20, 
display the message “Too high” and ask them to try again. Keep repeating this until they 
enter a value that is between 10 and 20 and then display the message “Thank you”. 
"""
i = int(input("Can you give me a number between 10 and 20? "))
while i < 10:
    print("Too low.")
    i = int(input("Can you give me enter a number between 10 and 20? "))
while i > 20:
    print("Too high")
    i = int(input("Can you give me enter a number between 10 and 20? "))
else:
    print("Thank you.")

"""
14.Write a Python program to sum all the items in a list.
"""
sum = 0
i = [2,7,9,19]
for j in i:
    sum += j
print(sum)

# second way
j = 0
sum = 0
i = [2,7,9,19]
while j < len(i):
    sum += i[j]
    j += 1
print(sum)

"""
15.Write a Python program to multiplies all the items in a list.
"""
multiplied = 1
j = [5,8,12,6]   # j = list(range(4))
for i in j:
    multiplied *= i
print(multiplied)

"""
16.Write a Python program to get the largest number from a list.
"""

j = [2,2,6,8,12]
max = j[0]
for i in j:
   if max < i:
    max = i
print(max)

"""
17.Write a Python program to get the smallest number from a list.
"""
j = list(range(8))
smallest = j[0]
for i in j:
    if i < smallest:
        i = smallest
print(smallest)

"""
18.Write a Python program to remove duplicates from a list.
"""
j = [2,5,7,2,8,7]
print(set(j))

# second way
j = [2,5,7,2,8,7]
none_repeatable = []
for i in j:
    if i not in none_repeatable:
        none_repeatable.append(i)
print(none_repeatable)

"""
19.Write a Python program to check a list is empty or not.
"""
j = [2,3]
if len(j) == 0:
    print ("The list is empty")
else:
    print("The list is not empty")

"""
20.Write a Python function that takes two lists and returns True if they have at least one common member.
"""

p = [1,6,8,9,4,2]
v = [3,6,12,75,89,0]
result = False
for i in p:
        for j in v:
            if i == j:
                 result = True
print(result)

"""
21.Write a Python program to get unique values from a list.
"""

p = ['Andrey', 'Ilya', 'Oleg', 'Valentin', 'Petr', 'Ilya', 'Oleg']
unique_value = []
for i in p:
    if i not in unique_value:
        unique_value.append(i)
print(unique_value)

"""
22.Write a Python program to select the odd items of a list.
"""
odd = []
v = [3,6,12,75,89,0]
for i in v:
    if i % 2 != 0:
        odd.append(i)
print(odd)

"""
23.Write a Python program to concatenate elements of a list.
"""
v = input("Dial some numbers ")
j = []
for i in v:
    j.append(i)
print(','.join(j))
print(type(j))

