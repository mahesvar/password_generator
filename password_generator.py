import string
import random


def pass_gen(n):
    password = ''
    num = round(n / 2)
    # first letter capitalized
    x = random.randint(36, 61)
    password += string.printable[x]

    # first half characters are capitalized letter
    for i in range(num - 1):
        x = random.randint(10, 24)
        password += string.printable[x]

    # second half characters are numbers and spl characters
    for j in range(num):
        y = random.randint(0, 94)
        password += string.printable[y]

    return password


print(pass_gen(12))
