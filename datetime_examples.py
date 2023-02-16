from datetime import date, datetime, timedelta

# https://www.geeksforgeeks.org/python-datetime-module/

# initializing constructor
# and passing arguments in the
# format year, month, date
my_date = date(1996, 12, 11)

print("Date passed as argument is", my_date)

# Uncommenting my_date = date(1996, 12, 39)
# will raise an ValueError as it is
# outside range

# uncommenting my_date = date('1996', 12, 11)
# will raise a TypeError as a string is
# passed instead of integer


today = date.today()

print("Today's date is", today)

print("Current year:", today.year)
print("Current month:", today.month)
print("Current day:", today.day)


date_time = datetime.fromtimestamp(1887639468)
print("Datetime from timestamp:", date_time)


today_iso = date.isoformat(today)
print("String Representation", today_iso)


dt = date.fromisoformat('2030-08-01')

print("dt month:", dt.month)

a = '2030-08-01' > '2029-09-01'
b = '01-08-2030' < '01-09-2029'

print(dt.isoweekday())


# Getting current date and time
now = datetime.now()
print("Without formatting", now)

# Example 1
s = now.strftime("%A %m %Y")
print('\nExample 1:', s)

# Example 2
s = now.strftime("%a %m %y")
print('\nExample 2:', s)

# Example 3
s = now.strftime("%I %p %S")
print('\nExample 3:', s)

# Example 4
s = now.strftime("%H:%M:%S")
print('\nExample 4:', s)

# strptime



date1 = datetime(2020, 1, 3)
date2 = datetime(2020, 2, 3)

# difference between dates
diff = date2 - date1
print("Difference in dates:", diff)

# Adding days to date1
date1 += timedelta(days=4)
print("Date1 after 4 days:", date1)

# Subtracting days from date1
date1 -= timedelta(15)
print("Date1 before 15 days:", date1)
