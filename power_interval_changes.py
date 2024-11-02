from matplotlib import pyplot as plt
import psycopg2
import matplotlib.dates as mdates
import numpy as np
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
SELECT 
	date
	, "1_min"
	, "5_min"
	, "20_min"
	, "60_min"
	, "90_min"
FROM 
	bikes.t_interval_power_weight 
WHERE 
	date > CURRENT_DATE - INTERVAL '24 MONTH'
"""

cursor.execute(sql)
results = list(cursor.fetchall())

date = []
sixty_sec = []
five_min = []
twenty_min = []
sixty_min = []
ninety_min = []

for i in results:
    date.append(i[0])
    sixty_sec.append(i[1])
    five_min.append(i[2])
    twenty_min.append(i[3])
    sixty_min.append(i[4])
    ninety_min.append(i[5])
  
    
plt.figure(figsize = (20, 30))

# Plotting all the intervals
plt.step(date, sixty_sec, color='r', label='60s')
plt.step(date, five_min, color='g', label='5m')
plt.step(date, twenty_min, color='b', label='20m')

# Naming x-axis, y-axis
plt.xlabel("Month") 
plt.ylabel("W/kg") 

plt.legend() 
plt.show()

plt.figure(figsize = (20, 30))
 
plt.step(date, sixty_min, color='y', label='60m') 
plt.step(date, ninety_min, color='r', label='90m') 

# Naming x-axis, y-axis
plt.xlabel("Month") 
plt.ylabel("W/kg") 

plt.legend() 
plt.show()
