from datetime import date, datetime, timedelta
'''This is a terrible config, ill get a better solution later'''

today = date.today()
# print("Today's date:", today)

# // TIME STUFF
day = today.strftime("%d")
# print("day =", day)
month = today.strftime("%B")
# print("month =", month)
year = today.strftime("%y")

# print("year =", year)