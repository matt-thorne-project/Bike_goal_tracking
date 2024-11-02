import psycopg2
import pandas as pd

connection = psycopg2.connect(
  host = "xxx",
  port = "xxx",
  user = "xxx",
  password = "xxx",
  database = "xxx"
)

cursor = connection.cursor()

sql = """
WITH delta AS (
SELECT 
    date
    , ftp
    ,(ftp - LAG(ftp, 1,0) OVER (ORDER BY date))AS delta
    , LAG(ftp, 1,0) OVER (ORDER BY date) AS previous_ftp
FROM 
    bikes.t_measurements
)
SELECT 
    date
    , ftp
    , delta AS watt_delta
FROM
    delta
WHERE
    delta.delta != 0
ORDER BY
    date ASC;"""

cursor.execute(sql)
results = list(cursor.fetchall())

df = pd.set_option('display.max_rows', 1000)
df = pd.DataFrame(results)
df.columns =['Date','FTP', 'FTP Delta']
blankIndex=[''] * len(df)
df.index=blankIndex
df.head(100)