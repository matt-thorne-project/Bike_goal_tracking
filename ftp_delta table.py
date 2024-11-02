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
    ,  (ftp - LAG(ftp, 1,0) OVER (ORDER BY date)) AS ftpDelta
    ,  LAG(ftp, 1,0) OVER (ORDER BY date) AS previousFtp
FROM 
    bikes.t_measurements
)
SELECT 
    date
    , ftp
    , ftpDelta	
    , ((DIV((ftpDelta::numeric), previousFtp::numeric)) * 100.0) AS percentageDelta
FROM
    delta
WHERE
    delta.ftpDelta != 0
	AND delta.previousFtp != 0
ORDER BY
    date ASC"""

cursor.execute(sql)
results = list(cursor.fetchall())

df = pd.set_option('display.max_rows', 1000)
df = pd.DataFrame(results)
df.columns =['Date','FTP', 'FTP Delta']
blankIndex=[''] * len(df)
df.index=blankIndex
df.head(100)