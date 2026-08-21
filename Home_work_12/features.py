def plus(a,b):
    с = a+b
    return с




def convert_to_24_hour(time_str: str):

    if type(time_str) == list:
        raise TypeError

    if type(time_str) == dict:
        raise ValueError

    parts = time_str.split()
    if len(parts) != 2:
        raise ValueError('Time format is not a `hh:mm period`')
    time, period = parts
    hours, minutes = map(int, time.split(':'))
    if period.lower() == 'pm' and hours != 12:
        hours += 12
    elif period.lower() == 'am' and hours == 12:
        hours = 0
    return f'{hours:02}:{minutes:02}'

