"""
1.Write a Python function, which will count how many times a character (substring) is included in a string.
DON’T USE METHOD COUNT
2.Find and replace a substring in a string for another substring. User enter from a keyboard a string and both substrings.
DON’T USE METHOD REPLACE
3.* TODO: Write a function for decompressing string “a4b3c2d”
4.Recursion for Fib, factorial, digital root
"""

def counter(n: str):
    d = {}

    for i in n.lower():
        if i not in d:
            d[i] = 1
        else:
            d[i]+=1
    return d
print(counter("Good morning America"))


def recursion_fibonacci(n):
    if n <= 2:
        return 1
    else:
        return recursion_fibonacci(n-1) + recursion_fibonacci(n-2)

print(recursion_fibonacci(8))


