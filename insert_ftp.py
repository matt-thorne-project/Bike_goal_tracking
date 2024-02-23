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

print('Year of reading?')
year = int(input())

monthList = [
    inquirer.List(
        'option', 
        message = 'Month of reading?', 
        choices = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'],
        carousel = True
    ),
]

month = (inquirer.prompt(monthList)).get('option')

dayList = [
    inquirer.List(
        'option', 
        message = 'Day of reading?', 
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

print('Time of reading? 24Hr')
time = input()

parsedDate = datetime.strptime(f'{date}', '%Y-%b-%d').date()


print("""Are you entering a) performance or b) bp metrics?
Enter A or B""")
option = input()

if option == "A" or option == "a":
    print('What is your ftp?')
    ftp = int(input())
    print('What is your weight?')
    weight = (float(input()))
    print('What is your BF percentage?')
    body_fat = (float(input()))
    print('Notes?')
    notes = (str(input()))
    sql = f"INSERT INTO t_measurements (date, ftp, weight, body_fat, notes) VALUES (%s, %s, %s, %s, %s);"
    val =(parsedDate, ftp, weight, body_fat)

elif option == "B" or option == "b":
    print('What is your hr?')
    hr = int(input())
    print('What is your systolic?')
    systolic = int(input())
    print('What is your diastolic?')
    diastolic = int(input())
    print('Do you have any notes? Y/N')
    y_n = input()
    if y_n == "Y" or y_n == "y":
        print("Complete your notes")
        notes = input()
        sql = f"INSERT INTO t_blood_pressure (date, hr, systolic, diastolic, notes) VALUES (%s, %s, %s, %s, %s);"
        val =(timestamp, hr, systolic, diastolic, notes)
    else:
        sql = f"INSERT INTO t_blood_pressure (date, hr, systolic, diastolic) VALUES (%s, %s, %s, %s);"
        val =(timestamp, hr, systolic, diastolic)

mycursor.execute(sql, val)
mydb.commit()