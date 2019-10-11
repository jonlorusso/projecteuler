#!/usr/bin/env python

# Counting Sundays

# Problem 19
# You are given the following information, but you may prefer to do some research for yourself.

# 1 Jan 1900 was a Monday.
# Thirty days has September,
# April, June and November.
# All the rest have thirty-one,
# Saving February alone,
# Which has twenty-eight, rain or shine.
# And on leap years, twenty-nine.
# A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
# How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

def isleap(year):
    if year % 4 == 0:
        if year % 100 == 0 and year % 400 != 0:
            return False
        return True
    return False

def thirtyone(year):
    return 31

def thirty(year):
    return 30

def february(year):
    return 29 if isleap(year) else 28

class Date:
    def __init__(self, day, month, year, day_of_week):
        self.day = day
        self.month = month
        self.year = year
        self.day_of_week = day_of_week

days_of_week = {
    1: 'Monday',
    2: 'Tuesday',
    3: 'Wednesday',
    4: 'Thursday',
    5: 'Friday',
    6: 'Saturday',
    7: 'Sunday'
}

month_lengths = {
    1: thirtyone,
    2: february,
    3: thirtyone,
    4: thirty,
    5: thirtyone,
    6: thirty,
    7: thirtyone,
    8: thirtyone,
    9: thirty,
    10: thirtyone,
    11: thirty,
    12: thirtyone
}

def issunday(date):
    return True

def days(start_date):
    d = start_date

    while True:
        yield d
        d.day += 1

        if d.day_of_week == 7:
            d.day_of_week = 1
        else:
            d.day_of_week += 1

        if d.day > month_lengths[d.month](d.year):
            d.day = 1

            if d.month == 12:
                d.month = 1
                d.year += 1
            else:
                d.month += 1

start_date = Date(1, 1, 1900, 1)

sundays = 0
for d in days(start_date):
    if d.year > 2000:
        break
    if d.year > 1900:
        if d.day == 1 and d.day_of_week == 7:
            sundays += 1

print(sundays)
