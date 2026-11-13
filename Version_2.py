#In line 2 it will import the date from the library of datetime
from datetime import date

#The user will have to input the event and date 
event_title = input("Enter event title: ")
year = int(input("Enter year: "))
month = int(input("Enter month: "))
day = int(input("Enter day: "))

#in line 11 it will structure the inputs into the correct structure
event_date = date(year, month, day)

#this will print the correctly formatted and structured inputs.
print("Formatted Output:")
print("Event:", title.upper())
print("Date:", event_date.strftime("%B %d, %Y"))
print("Year:", event_date.year)
print("Month:", event_date.strftime("%B"))
print("Day:", event_date.day)
print("Weekday:", event_date.strftime("%A"))
