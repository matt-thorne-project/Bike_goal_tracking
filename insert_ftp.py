from datetime  import datetime
import mysql.connector
import inquirer
import key_file as key_file 

mydb = mysql.connector.connect(
  host = key_file.DB_HOST,
  user = key_file.DB_USER,
  passwd = key_file.DB_PASSWD,
  database = key_file.DB_DATABASE
)

mycursor = mydb.cursor()

print('What the date of test?')
year = int(input())

monthList = [
    inquirer.List(
        'option', 
        message = 'What is your month of test?', 
        choices = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
        carousel = True
    ),
]

month = (inquirer.prompt(monthList)).get('option')

dayList = [
    inquirer.List(
        'option', 
        message = 'What is your day of test?', 
        choices = list(range(1,32)),
        carousel = True
    ),
]

day = (str((inquirer.prompt(dayList)).get('option'))).rjust(2, '0')

date = str(f'{year}-{month}-{day}')

#validate entered date by returning true if returns value, a Feb 30 won't return any value and thus exit
try:
    dateTest = bool(datetime.strptime(f'{date}', '%Y-%b-%d').date())
except ValueError:
    dateTest = False
    print("Date entered isn't valid.")
    exit()

parsedDate = datetime.strptime(f'{date}', '%Y-%b-%d').date()

print('What is your ftp?')
ftp = int(input())

print('What is your weight?')
weight = (float(input()))

print('What is your BF percentage?')
body_fat = (float(input()))

sql = f"INSERT INTO t_ftp_measurement (date, ftp, weight, body_fat) VALUES (%s, %s, %s, %s);"
val =(parsedDate, ftp, weight, body_fat)

mycursor.execute(sql, val)
mydb.commit()