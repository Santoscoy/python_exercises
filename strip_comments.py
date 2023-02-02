"""
Complete the solution so that it strips all text that follows any of a set of comment markers passed in. Any whitespace
at the end of the line should also be stripped out.

Example:

Given an input string of:

apples, pears # and bananas
grapes
bananas !apples
The output expected would be:

apples, pears
grapes
bananas
"""


def strip_comments(string, markers):
    lines = string.split('\n')
    chunks = []
    for line in lines:
        new_string = ''
        for char in line:
            if char in markers:
                break
            new_string += char
        if new_string and (new_string[-1] == ' ' or new_string == '\t'):
            chunks.append(new_string[:-1])
        else:
            chunks.append(new_string)
    return '\n'.join(chunks)


if __name__ == '__main__':
    print(strip_comments('apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']))  # should return 'apples, pears\ngrapes\nbananas')
    # print(strip_comments('a #b\nc\nd $e f g', ['#', '$']))  # should return 'a\nc\nd')
    # print(strip_comments(' a #b\nc\nd $e f g', ['#', '$']))  # should return ' a\nc\nd')
