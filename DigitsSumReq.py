# Given n, take the sum of the digits of n.
# If that value has more than one digit, continue reducing in this way until a single-digit number is produced.
# This is only applicable to the natural numbers.

# 16  -->  1 + 6 = 7
# 942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2

n = 493193


def digital_root(n):
    length = len(str(n))

    while length != 1:
        sum = 0
        for i in range(0, length):
            sum += n % 10
            n = n // 10
        length = len(str(sum))
        n = sum

    return n


print(digital_root(n))
