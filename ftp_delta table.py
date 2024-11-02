import psycopg2
import pandas as pd
# from IPython.display import HTML

connection = psycopg2.connect(
  host = "localhost",
  port = "5432",
  user = "read_only",
  password = "read_only",
  database = "Bike_goal"
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
    , round((ftpDelta::numeric / previousFtp::numeric * 100.00), 1)  AS percentageDelta
FROM
    delta
WHERE
    delta.ftpDelta != 0
	AND delta.previousFtp != 0
    AND date > CURRENT_DATE - INTERVAL '24 MONTH'
ORDER BY
    date ASC"""

cursor.execute(sql)
results = list(cursor.fetchall())

df = pd.set_option('display.max_rows', 1000)
df = pd.DataFrame(results)
df.columns =['Date','FTP', 'FTP Delta', 'Delta Percentage']
df.style.format({'Delta Percentage': '{:.0%}'})
blankIndex=[''] * len(df)
df.index=blankIndex
df.head(100)