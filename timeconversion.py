def timeConversion(s):
    hour = int(s[:2])
    minute = int(s[3:5])
    second = int(s[6:8])
    am_or_pm = (s[8:])
    if am_or_pm == "PM" and hour != 12:
        convert_hour = hour + 12
        return "{:>02d}:{:>02d}:{:>02d}".format(convert_hour, minute, second)
    elif am_or_pm == "PM" and hour == 12:
        return "{:>02d}:{:>02d}:{:>02d}".format(hour, minute, second)
    elif am_or_pm == "AM" and hour != 12:
        return "{:>02d}:{:>02d}:{:>02d}".format(hour, minute, second)
    else:
        convert_hour = hour - 12
        return "{:>02d}:{:>02d}:{:>02d}".format(convert_hour, minute, second)