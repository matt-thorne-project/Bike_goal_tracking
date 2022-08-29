import mysql.connector
from matplotlib import pyplot as plt

mydb = mysql.connector.connect(
  host="localhost",
  user="matt",
  passwd="MySQLPassword1!",
  database='cycling_stats'
)

mycursor = mydb.cursor()

sql = "SELECT date, ftp, weight FROM t_ftp_measurement WHERE date > '2021-01-01'"

mycursor.execute(sql)
results = list(mycursor.fetchall())

dates = []
ftp = []
weight = []
wkg = []

for i in results:
    dates.append(i[0])
    ftp.append(i[1])
    weight.append(i[2])
    wkg.append(i[1]/i[2])
  
    
plt.figure(figsize = (15, 20))

ax1 = plt.subplot(2, 1, 1)
ax2=ax1.twinx()
lns1 = ax1.plot(dates, ftp, "g-", label="FTP")
lns2 = ax2.plot(dates, weight, "b-", label="Weight")
ax1.set_ylabel("FTP", fontsize = 14)
ax2.set_ylabel("Weight", fontsize = 14)
ax1.tick_params(axis='x', labelrotation = 45)

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=0)

ax3 = plt.subplot(2, 1, 2)
ax3.plot(dates, wkg)
ax3.set_ylabel("Watts per Kilo", fontsize = 14)
ax3.tick_params(axis='x', labelrotation = 45)
plt.legend(["Watt per Kilo"])


plt.show()