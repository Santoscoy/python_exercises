"""
12 ==> 21
513 ==> 531
2017 ==> 2071
nextBigger(num: 12)   // returns 21
nextBigger(num: 513)  // returns 531
nextBigger(num: 2017) // returns 2071
If the digits can't be rearranged to form a bigger number, return -1 (or nil in Swift):

9 ==> -1
111 ==> -1
531 ==> -1
nextBigger(num: 9)   // returns nil
nextBigger(num: 111) // returns nil
nextBigger(num: 531) // returns nil
"""


def next_bigger(n):
    if is_max_number(n):
        return -1

    return next_bigger_calculator(n)


def next_bigger_calculator(n):
    numbers = []
    numbers[:0] = str(n)
    numbers.sort()
    next_numbers = []
    next_numbers[:0] = str(n + 1)
    number = ''

    while next_numbers != numbers:
        n += 1
        next_numbers = []
        next_numbers[:0] = str(n)
        number = ''.join(next_numbers)
        next_numbers.sort()

    return int(number)


def is_max_number(n):
    numbers = []
    numbers[:0] = str(n)
    numbers.sort(reverse=True)
    return int(''.join(numbers)) == n


if __name__ == '__main__':  # noqa
    print(next_bigger(12))  # should return 21
    print(next_bigger(21))  # should return -1
    print(next_bigger(513))  # should return 531
    print(next_bigger(2017))  # should return 2071
    print(next_bigger(414))  # should return 441
    print(next_bigger(144))  # should return 414
    print(next_bigger(441))  # should return -1

