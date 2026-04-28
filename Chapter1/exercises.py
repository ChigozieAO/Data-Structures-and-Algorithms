# Reinforcement

# R-1.1
# Write a short Python function, is multiple(n, m), that takes
# two integer values and returns True if n is a multiple of m,
# that is, n = mi for some integer i, and False otherwise.


def multiple(n, m):
    if n % m == 0:
        return True
    return False


# R-1.2
# Write a short Python function, is even(k), that takes an integer value and
# returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.


def is_even(k):
    a, b = divmod(k, 2)
    if b == 0:
        return True
    return False


# R-1.3
# Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.


def minmax(data):
    mini = data[0]
    maxi = data[0]
    for i in range(len(data)):
        if data[i] > maxi:
            maxi = data[i]
        elif data[i] < mini:
            mini = data[i]
    return mini, maxi


# R-1.4
# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the positive integers smaller than n.


def sum_square(n):
    squ_sum = sum(k**k for k in range(1, n) if n > 0)
    return squ_sum


# R-1.5
# Give a single command that computes the sum from Exercise R-1.4, relying
# on Python’s comprehension syntax and the built-in sum function.


def sum_squares(n):
    squ_sum = sum(k**k for k in range(1, n) if n > 0)
    return squ_sum


# R-1.6
# Write a short Python function that takes a positive integer n and returns
# the sum of the squares of all the odd positive integers smaller than n.


def sum_odd_square(n):
    squares = []
    if n > 0:
        for k in range(n):
            if k % 2 == 0:
                squares.append(k**k)
    odd_squ = sum(squares)
    return odd_squ


# R-1.7
# Give a single command that computes the sum from Exercise R-1.6, relying
# on Python’s comprehension syntax and the built-in sum function.


def sum_odd_squares(n):
    if n > 0:
        squ_sum = sum(k**k for k in range(1, n) if k % 2 == 0)
    return squ_sum


# R-1.8
# Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for index
# −n≤k<0, what is the equivalent index j ≥0 such that s[j] references
# the same element?

# 0<-1(j<n)

# R-1.9
# What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?

range(50, 90, 10)

# R-1.10
# What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?

range(8, -8, -2)

# R-1.11
# Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].

pow_two = []
