'''
    Using the calendar module to get a specific date
    More information on the problem can be found here: https://www.hackerrank.com/challenges/calendar-module/problem
'''
import calendar

if __name__ == '__main__':
    user_input = list(map(int, input("Enter in a date in MM DD YYYY format: ").split()))
    month, day, year = user_input[0], user_input[1], user_input[2]
    the_day = calendar.weekday(year, month, day)
    print(calendar.day_name[the_day].upper())
