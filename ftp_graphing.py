import mysql.connector
from matplotlib import pyplot as plt
import key_file as key_file 

mydb = mysql.connector.connect(
  host = key_file.DB_HOST,
  user = key_file.DB_USER,
  passwd = key_file.DB_PASSWD,
  database = key_file.DB_DATABASE
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
  
    
plt.figure(figsize = (20, 30))

ax1 = plt.subplot(2, 1, 1)
ax2=ax1.twinx()
lns1 = ax1.plot(dates, ftp, "g-", label="FTP", marker = "o")
lns2 = ax2.plot(dates, weight, "b-", label="Weight", marker = "o")
ax1.set_ylabel("FTP", fontsize = 14)
ax2.set_ylabel("Weight", fontsize = 14)
ax1.tick_params(axis='x', labelrotation = 45)

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=0)
plt.savefig('/var/www/ftp/ftp_weight.png', transparent = True, bbox_inches='tight')


plt.figure(figsize = (20, 30))
ax = plt.subplot(2, 1, 2)
plt.plot(dates, wkg)
ax.set_ylabel("Watts per Kilo", fontsize = 14)
plt.tick_params(axis='x', labelrotation = 45)
plt.legend(["Watt per Kilo"])
plt.savefig('/var/www/ftp/bikeprogress.png', transparent = True, bbox_inches='tight')