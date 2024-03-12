import mysql.connector
from matplotlib import pyplot as plt
import pandas as pd



mydb = mysql.connector.connect(
  host = "XXXX",
  user = "XXXX",
  passwd = "XXXX",
  database = "XXXX"
)

mycursor = mydb.cursor()

sql = "SELECT date, hr, CONCAT (systolic, '/', diastolic, 'mmHg'), notes FROM t_blood_pressure"

mycursor.execute(sql)
results = list(mycursor.fetchall())

df = pd.DataFrame(results)
df.columns =['Date','HR per min', 'Diastolic/Systolic', 'Notes']

display(df)
