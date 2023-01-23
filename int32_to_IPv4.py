"""
Take the following IPv4 address: 128.32.10.1

This address has 4 octets where each octet is a single byte (or 8 bits).

1st octet 128 has the binary representation: 10000000
2nd octet 32 has the binary representation: 00100000
3rd octet 10 has the binary representation: 00001010
4th octet 1 has the binary representation: 00000001
So 128.32.10.1 == 10000000.00100000.00001010.00000001

Because the above IP address has 32 bits, we can represent it as the unsigned 32 bit number: 2149583361

Complete the function that takes an unsigned 32 bit number and returns a string representation of its IPv4 address.

EXAMPLES:

    2149583361 ==> "128.32.10.1"

    32         ==> "0.0.0.32"

    0          ==> "0.0.0.0"
"""


def int32_to_ip(int32):
    bin_num = decimal_to_binary(int32)
    byte_list = ip_builder(bin_num)
    return ipv4_builder(byte_list)


def ipv4_builder(byte_list):
    num_list = []
    for byte in byte_list:
        power = len(byte)
        num = 0
        for dig in byte:
            power = power - 1
            num = num + (int(dig) * (2 ** power))
        num_list.append(str(num))
    return '.'.join(num_list)


def ip_builder(bin_num):
    count = 1
    bin_IP = ''
    for dig in bin_num:
        bin_IP = bin_IP + dig
        if count % 8 == 0 and len(bin_IP) < 32:
            bin_IP = bin_IP + '.'
        count += 1
    return bin_IP.split('.')


def decimal_to_binary(decimal):
    bin_num = []
    while len(bin_num) < 32:
        if decimal != 0:
            bin_num.append(str(decimal % 2))
            decimal = decimal // 2
        else:
            bin_num.append('0')

    bin_num.reverse()
    string = ''.join(bin_num)
    return string


if __name__ == '__main__':  # noqa
    print(int32_to_ip(2154959208))  # should return"128.114.17.104"
    print(int32_to_ip(0))  # should return"0.0.0.0"
    print(int32_to_ip(2149583361))  # should return"128.32.10.1"
    print(int32_to_ip(20))
