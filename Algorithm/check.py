
i = "LoVE my PyTHon"
low = []
up = []
for j in i:
    if j.isupper():
        up.append(j)
    else:
        low.append(j)
print(''.join(low))
print(''.join(up))
