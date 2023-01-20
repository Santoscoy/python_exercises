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
    minutes = seconds // 60
    hours = minutes // 60
    days = hours // 24
    years = days // 365

    if years >= 1:
        days = days - (years * 365)
        if years == 1:
            year_msg = '1 year'
        else:
            year_msg = f'{years} years'
    else:
        year_msg = ''

    if days >= 1:
        hours = hours - (days * 24)
        if days == 1:
            day_msg = '1 day'
        else:
            day_msg = f'{days} days'
    else:
        day_msg = ''

    if hours >= 1:
        minutes = minutes - (hours * 60) - (days * 1440) - (years * 525600)
        if hours == 1:
            hour_msg = '1 hour'
        else:
            hour_msg = f'{hours} hours'
    else:
        hour_msg = ''

    if minutes >= 1:
        remain_seconds = seconds - (minutes * 60) - (hours * 3600) - (days * 86400) - (years * 31536000)
        if minutes == 1:
            minute_msg = '1 minute'
        else:
            minute_msg = f'{minutes} minutes'
    else:
        minute_msg = ''

    if remain_seconds >= 1:
        if remain_seconds == 1:
            second_msg = '1 second'
        else:
            second_msg = f'{remain_seconds} seconds'
    else:
        second_msg = 'now'

    MSG_LIST = [year_msg, day_msg, hour_msg, minute_msg, second_msg]

    msg_list = []
    for msg in MSG_LIST:
        if msg:
            msg_list.append(msg)

    return msg_list
            
            




if __name__ == '__main__': # noqa
    print(format_duration(1))  # should return a srt "1 second"
    print(format_duration(62))  # should return a srt "1 minute and 2 seconds"
    print(format_duration(120))  # should return a srt "2 minutes"
    print(format_duration(3600))  # should return a srt "1 hour"
    print(format_duration(3662))  # should return a srt "1 hour, 1 minute and 2 seconds"

