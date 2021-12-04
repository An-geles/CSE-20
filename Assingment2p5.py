
input_month = input()
input_day = int(input())
months = ('January','February','March','April','May','June','July','August','September','October','November','December')
days31 = ('January','March','May','July','August','October','December')
days30 = ('April','June','September','November')
days28 = ('February')
# Parameter for output to be None before code goes through and changes to Season
output = None

# Statements to check whether month inputted falls into any of the Seasons
if input_month in ('March','April','May','June'):
    output = 'Spring'
elif input_month in ('June','July','August','September'):
    output = 'Summer'
elif input_month in ('September','October','November','December'):
    output = 'Autumn'
elif input_month in ('December','January','February','March'):
    output = 'Winter'

# Program to check that input is valid for program
if input_month not in months:
    output = 'Invalid'
elif input_day > 31:
    output = 'Invalid'
elif input_day < 1:
    output = 'Invalid'
elif input_month in days30:
    if input_day > 30:
        output = 'Invalid'
elif input_month in days28:
    if input_day > 28:
        output = 'Invalid'


# Main program that decided specific dates for seasons

def my_function():
    if (input_month == 'March') and (31 > input_day > 19):
        output = 'Spring'
    elif (input_month == 'June') and (30 > input_day > 20):
        output = 'Summer'
    elif (input_month == 'September') and (30 > input_day > 21):
        output = 'Autumn'
    elif (input_month == 'September') and (input_day > 30):
        output = 'Invalid'
    elif input_month == 'December' and (31 > input_day > 20):
        output = 'Winter'



print(output)
