# The equation for the Fibonacci sequence:
# φ0 = 0,  φ1 = 1,  φn = φn−1 + φn−2.
#
# The task is to display all the numbers from start to n of the Fibonacci sequence φn

# Equation:
# F0 = 0
# F1 = 1
# F2 = 1
# Fn = Fn-1 + Fn-2

# Fibonacci sequence 0 1 1 2 3 5 8 13 21 34 55 89


def fibonacci(n):
    fib0 = 0
    fib1 = 1

    if n == 0:
        return fib0
    if n == 1:
        return fib1
    if n > 1:
        for i in range(1, n):
            fib = fib0 + fib1
            fib0 = fib1
            fib1 = fib
        return fib1


print(fibonacci(10))

#  HW: Rewrite code, which will return only needed element of Fib sequence
