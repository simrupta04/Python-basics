#15 Calender module
import calendar
m, d, y = map(int, input("input the month,date,year").strip().split())
print(calendar.day_name[calendar.weekday(y, m, d)].upper())
