def time_conversion(s: str) -> str:
    time: str = s[:-2]
    period: str = s[-2:]
    hour, minute, second = time.split(':')
    if period == 'PM' and hour != '12':
        hour = str(int(hour) + 12)
    if hour == '24' or hour == '12' and period == 'AM':
        hour = '00'
    return f'{hour}:{minute}:{second}'
