# Write two functions that convert a roman numeral to and from an integer value. Multiple roman numeral values will be
# tested for each function.
#
# Modern Roman numerals are written by expressing each digit separately starting with the left most digit and skipping
# any digit with a value of zero. In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC. 2008
# is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.
#
# Input range : 1 <= n < 4000
#
# In this kata 4 should be represented as IV, NOT as IIII (the "watchmaker's four").
#
# Examples
# to roman:
# 2000 -> "MM"
# 1666 -> "MDCLXVI"
# 1000 -> "M"
#  400 -> "CD"
#   90 -> "XC"
#   40 -> "XL"
#    1 -> "I"
#
# from roman:
# "MM"      -> 2000
# "MDCLXVI" -> 1666
# "M"       -> 1000
# "CD"      -> 400
# "XC"      -> 90
# "XL"      -> 40
# "I"       -> 1
# Help
# Symbol	Value
# I	1
# IV	4
# V	5
# X	10
# L	50
# C	100
# D	500
# M	1000


ROMAN_COMPOSE_NUM_MAP = {
    "IV": 4,
    "IX": 9,
    "XL": 40,
    "XC": 90,
    "CD": 400,
    "CM": 900,
}


ROMAN_SINGLE_NUM_MAP = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000,
}


def converter_to_roman(char_1: str, char_2=None, char_3=None, val=None) -> str:
    roman_val = ""
    if val <= 3:
        for count in range(val):
            roman_val += char_1

    elif val == 4:
        roman_val = char_1 + char_2

    elif val <= 8:
        roman_val = char_2
        for count in range(val - 5):
            roman_val += char_1

    elif val == 9:
        roman_val = char_1 + char_3

    return roman_val


def converter_to_decimal(dict_map: dict, roman_num: str) -> (list, str):
    roman_string = roman_num
    num_list = []
    for key in dict_map.keys():
        if key in roman_num:
            count = roman_string.count(key)
            roman_string = roman_string.replace(key, "")
            for i in range(count):
                num_list.append(dict_map[key])

    return num_list, roman_string


class RomanNumerals:
    @staticmethod
    def to_roman(val):
        num_list = [item for item in str(val)]

        roman_thousands = ""
        if len(num_list) == 4:
            thousands = int(num_list.pop(0))
            roman_thousands = converter_to_roman(char_1="M", val=thousands)

        roman_hundred = ""
        if len(num_list) == 3:
            hundred = int(num_list.pop(0))
            roman_hundred = converter_to_roman(char_1="C", char_2="D", char_3="M", val=hundred)

        roman_tens = ""
        if len(num_list) == 2:
            tens = int(num_list.pop(0))
            roman_tens = converter_to_roman(char_1="X", char_2="L", char_3="C", val=tens)

        roman_ones = ""
        if len(num_list) == 1:
            ones = int(num_list.pop(0))
            roman_ones = converter_to_roman(char_1="I", char_2="V", char_3="X", val=ones)

        return roman_thousands + roman_hundred + roman_tens + roman_ones

    @staticmethod
    def from_roman(roman_num):
        num_list, roman_num = converter_to_decimal(ROMAN_COMPOSE_NUM_MAP, roman_num)
        num_list2, roman_num = converter_to_decimal(ROMAN_SINGLE_NUM_MAP, roman_num)

        return sum(num_list + num_list2)


if __name__ == "__main__":
    print(RomanNumerals.to_roman(1000))  # expected output  'M', '1000 should == "M"'
    print(RomanNumerals.to_roman(3290))  # expected output  'MMMCCXC', '3290 should == "MMMCCXC"'
    print(RomanNumerals.to_roman(4))  # expected output  'IV', '4 should == "IV"'
    print(RomanNumerals.to_roman(1))  # expected output  'I', '1 should == "I"'
    print(RomanNumerals.to_roman(1999))  # expected output  'MCMXC', '1990 should == "MCMXC"'
    print(RomanNumerals.to_roman(2008))  # expected output  'MMVIII', '2008 should == "MMVIII"'
    print(RomanNumerals.from_roman('XXI'))  # expected output 21, 'XXI should == 21'
    print(RomanNumerals.from_roman('I'))  # expected output 1, 'I should == 1'
    print(RomanNumerals.from_roman('IV'))  # expected output 4, 'IV should == 4'
    print(RomanNumerals.from_roman('MMVIII'))  # expected output 2008, 'MMVIII should == 2008'
    print(RomanNumerals.from_roman('MDCLXVI'))  # expected output 1666, 'MDCLXVI should == 1666'
    print(RomanNumerals.from_roman('MMCMLXXV'))  # expected output 1666, 'MDCLXVI should == 2975'
