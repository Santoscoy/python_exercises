"""
Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds,
 in a human-friendly way.

The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise,

the duration is expressed as a combination of years, days, hours, minutes and seconds.

It is much easier to understand with an example:

* For seconds = 62, your function should return
    "1 minute and 2 seconds"
* For seconds = 3662, your function should return
    "1 hour, 1 minute and 2 seconds"
For the purpose of this Kata, a year is 365 days and a day is 24 hours.

Note that spaces are important.

Detailed rules
The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of
the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.

The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ",
just like it would be written in English.

A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not
correct, but 1 year and 1 second is.

Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.

A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it
should be just 1 minute.

A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1
minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more
significant unit of time.
"""


def format_duration(seconds):
    if seconds == 0:
        return 'now'

    remain_seconds, minutes = time_calculator(seconds, 60)
    remain_minutes, hours = time_calculator(minutes, 60)
    remain_hours, days = time_calculator(hours, 24)
    remain_days, years = time_calculator(days, 365)

    year_msg = str_builder(years, 'year')
    day_msg = str_builder(remain_days, 'day')
    hour_msg = str_builder(remain_hours, 'hour')
    minute_msg = str_builder(remain_minutes, 'minute')
    second_msg = str_builder(remain_seconds, 'second')

    return msg_builder([year_msg, day_msg, hour_msg, minute_msg, second_msg])


def time_calculator(time, divisor):
    int_time = time // divisor
    remain = time % divisor
    return remain, int_time


def str_builder(time, denomination):
    if time >= 1:
        if time == 1:
            msg = f'1 {denomination}'
        else:
            msg = f'{time} {denomination}s'
    else:
        msg = ''
    return msg


def msg_builder(str_list):
    msg_list = []
    for msg in str_list:
        if msg:
            msg_list.append(msg)

    string = ''
    if len(msg_list) > 2:
        last_msg = msg_list.pop()
        for item in msg_list:
            string = string + item + ', '

        string = string[:-2] + f' and {last_msg}'
        return string

    elif len(msg_list) == 2:
        return ' and '.join(msg_list)

    else:
        return msg_list[0]


if __name__ == '__main__': # noqa
    print(format_duration(1))  # should return a srt "1 second"
    print(format_duration(62))  # should return a srt "1 minute and 2 seconds"
    print(format_duration(120))  # should return a srt "2 minutes"
    print(format_duration(3600))  # should return a srt "1 hour"
    print(format_duration(3662))  # should return a srt "1 hour, 1 minute and 2 seconds"
