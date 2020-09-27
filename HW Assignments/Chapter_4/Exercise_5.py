#(Find future dates) Write a program that prompts the user to enter an integer for
#today’s day of the week (Sunday is 0, Monday is 1, ..., and Saturday is 6). Also
#prompt the user to enter the number of days after today for a future day and display
#the future day of the week. Here is a sample run:

todayInt = eval(input("Enter today's day(Sunday is 0, Monday is 1, ..): "))
days = eval(input("Enter the number of days elapsed since today: "))
futureDay = ''
if ((todayInt + days) % 7) == 0:
    futureDay = 'Sunday'
elif ((todayInt + days) % 7) == 1:
    futureDay = 'Monday'
elif ((todayInt + days) % 7) == 2:
    futureDay = 'Tuesday'
elif ((todayInt + days) % 7) == 3:
    futureDay = 'Wednesday'
elif ((todayInt + days) % 7) == 4:
    futureDay = 'Thursday'
elif ((todayInt + days) % 7) == 5:
    futureDay = 'Friday'
elif ((todayInt + days) % 7) == 6:
    futureDay = 'Saturday'
today = ''
if (todayInt  % 7) == 0:
    today = 'Sunday'
elif (todayInt % 7) == 1:
    today = 'Monday'
elif (todayInt % 7) == 2:
    today = 'Tuesday'
elif (todayInt % 7) == 3:
    today = 'Wednesday'
elif (todayInt % 7) == 4:
    today = 'Thursday'
elif (todayInt % 7) == 5:
    today = 'Friday'
elif ((todayInt + days) % 7) == 6:
    today = 'Saturday'

print('Today is ' + today + ' and the future day is ' + futureDay)