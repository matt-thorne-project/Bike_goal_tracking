import mysql.connector
import pandas as pd

mydb = mysql.connector.connect(
  host = "XXXX",
  user = "XXXX",
  passwd = "XXXX",
  database = "XXXX"
)

mycursor = mydb.cursor()

sql = """
WITH delta AS (
SELECT 
    date
    , ftp
    ,(ftp - LAG(ftp, 1,0) OVER (ORDER BY date))AS delta
    , LAG(ftp, 1,0) OVER (ORDER BY date) AS previous_ftp
FROM 
    t_measurements
)
SELECT 
    date
    , ftp
    , delta AS watt_delta
    , (((ftp / previous_ftp) * 100)-100) AS percentage_delta
FROM
    delta
WHERE
    delta.delta != 0
ORDER BY
    date ASC;"""

mycursor.execute(sql)
results = list(mycursor.fetchall())

df = pd.set_option('display.max_rows', 1000)
df = pd.DataFrame(results)
df.columns =['Date','FTP', 'FTP delta', 'Delta percentage']
display(df)