import mysql.connector
from matplotlib import pyplot as plt

mydb = mysql.connector.connect(
  host = "XXXX",
  user = "XXXX",
  passwd = "XXXX",
  database = "XXXX"
)

mycursor = mydb.cursor()

sql = "SELECT date, ftp, weight FROM t_measurements WHERE date > '2021-01-01'"

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
plt.gca().xaxis.set_major_locator(locator)
plt.gca().xaxis.set_major_formatter(fmt)

lines, labels = ax1.get_legend_handles_labels()
lines2, labels2 = ax2.get_legend_handles_labels()
ax2.legend(lines + lines2, labels + labels2, loc=0)


plt.figure(figsize = (20, 30))
ax = plt.subplot(2, 1, 2)
plt.plot(dates, wkg)
ax.set_ylabel("Watts per Kilo", fontsize = 14)
plt.tick_params(axis='x', labelrotation = 45)
plt.gca().xaxis.set_major_locator(locator)
plt.gca().xaxis.set_major_formatter(fmt)
plt.legend(["Watt per Kilo"])


plt.figure(figsize = (20, 30))
ax = plt.subplot(2, 1, 2)
plt.fill_between(dates, weight, color="grey" , alpha=0.4)
plt.plot(dates, weight, "darkgrey")
plt.grid(color='lightgrey', linestyle='-', linewidth=0.5)
ax.set_ylabel("Kilos", fontsize = 14)
plt.tick_params(axis='x', labelrotation = 45)
plt.gca().xaxis.set_major_locator(locator)
plt.gca().xaxis.set_major_formatter(fmt)
plt.legend(["Kilos"])
plt.ylim(ymax = 72, ymin = 62)