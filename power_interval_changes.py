from matplotlib import pyplot as plt
import mysql.connector


mydb = mysql.connector.connect(
  host = "xxx",
  user = "xxx",
  passwd = "xxx",
  database = "xxx"
)

mycursor = mydb.cursor()

sql = "SELECT date, 60_sec, 5_min, 20_min, 60_min, 90_min FROM t_interval_power_weight WHERE date > CURDATE() - INTERVAL 18 MONTH"

mycursor.execute(sql)
results = list(mycursor.fetchall())

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
  
# Naming x-axis, y-axis
plt.xlabel("Month") 
plt.ylabel("W/kg") 

plt.legend() 
plt.gca().xaxis.set_major_locator(locator)
plt.gca().xaxis.set_major_formatter(fmt)
plt.show()

plt.figure(figsize = (20, 30))

plt.step(date, twenty_min, color='b', label='20m') 
plt.step(date, sixty_min, color='y', label='60m') 
plt.step(date, ninety_min, color='r', label='90m') 

# Naming x-axis, y-axis
plt.xlabel("Month") 
plt.ylabel("W/kg") 

plt.legend() 
plt.gca().xaxis.set_major_locator(locator)
plt.gca().xaxis.set_major_formatter(fmt)
plt.show()