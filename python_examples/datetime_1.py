import datetime

# This code finds the difference between two dates
d1 = datetime.date(1991, 7, 17)
d2 = datetime.date(1991, 9, 4)

delta = d2 - d1
print(delta.days)
print(delta.total_seconds()) 


"""Date formatting - Full weekday, Full month, Day with zero padded number, Year with century
as a decimal number"""
#the old way
leo_dob = datetime.date(1991, 7, 17)
print(leo_dob.strftime("%A, %B %d, %Y"))


#This is a more modern way - Pass the format into a message
message = "Leo was born on {:%A, %B %d, %Y}."
print(message.format(leo_dob))

message2 = "Leo was born on {:%D}."
print(message2.format(leo_dob))

# Create objects using all three classes of date, time and datetime in the datetime module
#SPACEX LAUNCH DATE
launch_date = datetime.date(2017, 3, 30) # the three arguments are year, month and day
launch_time = datetime.time(22, 27, 0) # the three arguments are hours, minutes and seconds
launch_datetime = datetime.datetime(2017, 3, 30, 22, 27, 0)
print(launch_date)
print(launch_time)
print(launch_datetime)


#Getting the now time
now = datetime.datetime.today()
print(now)