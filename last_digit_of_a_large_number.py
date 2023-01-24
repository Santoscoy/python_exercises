"""
Define a function that takes in two non-negative integers
a and b and return the last decimal digit of a ^ b.
Note that a and b may be very large!

For example, the last decimal digit of 9^7 is 9 since 9^7 = 4782969
The last decimal digit of (2^200)^2^300, which has over 10^92 decimal digits, is 6. Also, please take 0^0
to be 1.

You may assume that the input will always be valid.

Examples
last_digit(4, 1)                # return 4
last_digit(4, 2)                # return 6
last_digit(9, 7)                # return 9
last_digit(10, 10 ** 10)        # return 0
last_digit(2 ** 200, 2 ** 300)  # return 6
"""
LOOP = {
    0: [0, 0, 0, 0],
    1: [1, 1, 1, 1],
    2: [2, 4, 8, 6],
    3: [3, 9, 7, 1],
    4: [4, 6, 4, 6],
    5: [5, 5, 5, 5],
    6: [6, 6, 6, 6],
    7: [7, 9, 3, 1],
    8: [8, 4, 2, 6],
    9: [9, 1, 9, 1],
}


def last_digit(n1, n2):
    n1_last_digit = int(str(n1)[-1])
    cycle = LOOP[n1_last_digit]
    return 1 if n2 == 0 else cycle[(n2 % 4) - 1]


# alternative solution
def last_digit_alt(n1, n2):
    return pow(n1, n2, 10)


if __name__ == '__main__':  # noqa
    print(last_digit(4, 1))  # should return 4
    print(last_digit(4, 2))  # should return 6
    print(last_digit(9, 7))  # should return 9
    print(last_digit(10, 10 ** 10))  # should return 0
    print(last_digit(2 ** 200, 2 ** 300))  # should return 6
