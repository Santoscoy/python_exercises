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

class RomanNumerals:
    @staticmethod
    def to_roman(val):
        num_dict = {}
        count = 0
        for digit in str(val):
            count += 1
            num_dict[count] = digit



        return num_dict

    @staticmethod
    def from_roman(roman_num):
        ...


if __name__ == "__main__":
    print(RomanNumerals.to_roman(1000))  # expected output  'M', '1000 should == "M"'
    print(RomanNumerals.to_roman(4))  # expected output  'IV', '4 should == "IV"'
    print(RomanNumerals.to_roman(1))  # expected output  'I', '1 should == "I"'
    print(RomanNumerals.to_roman(1990))  # expected output  'MCMXC', '1990 should == "MCMXC"'
    print(RomanNumerals.to_roman(2008))  # expected output  'MMVIII', '2008 should == "MMVIII"'
    # print(RomanNumerals.from_roman('XXI'))  # expected output 21, 'XXI should == 21'
    # print(RomanNumerals.from_roman('I'))  # expected output 1, 'I should == 1'
    # print(RomanNumerals.from_roman('IV'))  # expected output 4, 'IV should == 4'
    # print(RomanNumerals.from_roman('MMVIII'))  # expected output 2008, 'MMVIII should == 2008'
    # print(RomanNumerals.from_roman('MDCLXVI'))  # expected output 1666, 'MDCLXVI should == 1666'
