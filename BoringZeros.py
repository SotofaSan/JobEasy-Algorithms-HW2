# Zeros not for Heros
# Numbers ending with zeros are boring.
# They might be fun in your world, but not here.
# Get rid of them. Only the ending ones.
#
# 1450 -> 145
# 960000 -> 96
# 1050 -> 105
# -1050 -> -105
# Zero alone is fine, don't worry about it. Poor guy anyway

n = int(input('Please enter the number:   '))


def boring_zero(number):

    if len(str(number)) > 1:
        n = str(abs(number))[::-1]
        n = int(n)
        n = str(n)[::-1]
    else:
        n = number

    return n if number >= 0 else ('-' + n)


print(boring_zero(n))
