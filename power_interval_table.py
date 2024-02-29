import mysql.connector
from matplotlib import pyplot as plt
import pandas as pd
import df2img

mydb = mysql.connector.connect(
  host = "XXXX",
  user = "XXXX",
  passwd = "XXXX",
  database = "XXXX"
)

mycursor = mydb.cursor()

sql = "SELECT date, 60_sec, 5_min, 20_min, 60_min, 90_min FROM t_interval_power_weight WHERE date > CURDATE() - INTERVAL 18 MONTH"

mycursor.execute(sql)
results = list(mycursor.fetchall())

df = pd.DataFrame(results)
df.columns =['Date','60 Second', '5 Min', '20 Min', '60 Min', '90 Min']

fig = df2img.plot_dataframe(
    df,
    print_index=False,
    row_fill_color=("white", "lightgrey"),
    tbl_header=dict(
        align="center",
        fill_color="darkgrey",
        font_color="black",
        font_size=14
    ),
    col_width=[10, 5, 5, 5, 5, 5]
)