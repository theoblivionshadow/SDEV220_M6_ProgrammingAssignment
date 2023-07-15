'''13.1 Write the current date as a string to the 
text file today.txt.'''

# import datetime module
from datetime import date

# get current date
currentDate = date.today()

# set string format
stringDate = "%B %d %Y"

# open file
f = open("today.txt", 'w')
# write date as string to file
f.write(currentDate.strftime(stringDate))
#close file
f.close()

'''13.2 Read the text file today.txt into the 
string today_string.'''
# open file
f = open("today.txt", 'r')

# read file and save to var
today_string = f.read()

'''13.3 Parse the date from today_string.'''
# split string
splitString = today_string.split()

# save string components individually
month = splitString[0]
day = splitString[1]
year = splitString[2]

# format for parsed string
parsedString = f"Today is {month} {day}, {year}."

# print parsed string
print(parsedString)