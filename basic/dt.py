import datetime

# now = datetime.datetime.now()
# print("Current date and time:", now)    #dateandtime

# today = datetime.date.today()
# print("Today's Date:", today)             #currentdate

# current_time = datetime.datetime.now().time()    #currenttime
# print("Current Time:", current_time)

now = datetime.datetime.now()

# formatted = now.strftime("%d/%m/%y %H:%M:%S")
# print("Formatted:", formatted)

# import datetime

# now = datetime.datetime.now()

# print(now.strftime("%A, %d %B %Y %I:%M:%S %p"))

# print(now.strftime("%H"))  # Hour (24-hr)
# print(now.strftime("%I"))  # Hour (12-hr)
# print(now.strftime("%p"))  # AM/PM
# print(now.strftime("%M"))  # Minute
# print(now.strftime("%S"))  # Second
# print(now.strftime("%f"))  # Microsecond

# import datetime
# now = datetime.datetime(2025, 9, 19, 15, 45, 30)  # fixed datetime for example

print(now.strftime("%d"))  # Day of month
print(now.strftime("%m"))  # Month number
print(now.strftime("%y"))  # Year (2 digits)
print(now.strftime("%Y"))  # Year (4 digits)
print(now.strftime("%a"))  # Short weekday
print(now.strftime("%A"))  # Full weekday
print(now.strftime("%b"))  # Short month
print(now.strftime("%B"))  # Full month
print(now.strftime("%j"))  # Day of year
print(now.strftime("%w"))  # Weekday (0=Sunday)






