"""
Create a function that will take a string as an input and return the 1st non-unique letter of a string.
“Google” => “l”
“Amazon” => “m”
If there are no unique letters, return an empty string: “xoxoxo” => “”.
How would you test it? How would you handle edge cases?

"""

# def return_uniq_letter(n: str):
#     for i in n.lower():
#         if n.count(i) == 1:
#             return i
#
# print(return_uniq_letter("Google"))

# 2 way
def return_uniq_letter_2(n: str):
    d = {}
    for i in n.lower():
        if i not in d:
            d[i] = 1
        else:
            d[i] += 1
    for k, v in d.items():
        if v == 1:
            return k
