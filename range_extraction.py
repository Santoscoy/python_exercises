# A format for expressing an ordered list of integers is to use a comma separated list of either
#
# individual integers
# or a range of integers denoted by the starting integer separated from the end integer in the range by a dash,  '-'.
# The range includes all integers in the interval including both endpoints. It is not considered a range unless it spans
# at least 3 numbers. For example "12, 13, 15-17"
# Complete the solution so that it takes a list of integers in increasing order and returns a correctly formatted string
# in the range format.
#
# Example:
#
# solution([-10,  -9,  -8,  -6,  -3,  -2,  -1,  0,  1,  3,  4,  5,  7,  8,  9,  10,  11,  14,  15,  17,  18,  19,  20])
# returns "-10--8, -6, -3-1, 3-5, 7-11, 14, 15, 17-20"

def solution(args):
    exclude_list_numbers = [
        args[index + 1]
        for index, n in enumerate(args)
        if index + 2 < len(args) and n + 2 == args[index + 2]
    ]

    sequences = []
    reference = exclude_list_numbers.copy()
    while reference:
        chunk = []
        exclude_list_numbers = reference.copy()
        for index, n in enumerate(exclude_list_numbers):
            if index + 1 < len(exclude_list_numbers) and exclude_list_numbers[index + 1] == n + 1:
                chunk.append(exclude_list_numbers[index])
                reference.pop(0)

            elif exclude_list_numbers[index - 1] == n - 1:
                chunk.append(exclude_list_numbers[index])
                reference.pop(0)
                break

            else:
                chunk.append(n)
                reference.pop(0)
                break

        sequences.append(chunk)

    string_args = [str(n) for n in args]
    string = ",".join(string_args)

    string_list = [",".join([str(n) for n in string_chunk]) for string_chunk in sequences]

    for chunk_string in string_list:
        string = string.replace(f",{chunk_string},", "-")

    return string


def chat_gpt_solution(lst):
    ranges = []
    start = lst[0]
    end = lst[0]
    for i in range(1, len(lst)):
        if lst[i] == end + 1:
            end = lst[i]
        else:
            if end - start >= 2:
                ranges.append(str(start) + "-" + str(end))
            else:
                ranges.extend([str(num) for num in range(start, end + 1)])
            start = lst[i]
            end = lst[i]
    if end - start >= 2:
        ranges.append(str(start) + "-" + str(end))
    else:
        ranges.extend([str(num) for num in range(start, end + 1)])
    return ",".join(ranges)


if __name__ == "__main__":
    print(solution([-6, -3, -2, -1, 0, 1, 3, 4, 5, 7, 8, 9, 10, 11, 14, 15, 17, 18, 19, 20]))  # '-6, -3-1, 3-5, 7-11, 14, 15, 17-20')
    print(solution([-3, -2, -1, 2, 10, 15, 16, 18, 19, 20]))  # '-3--1, 2, 10, 15, 16, 18-20')
