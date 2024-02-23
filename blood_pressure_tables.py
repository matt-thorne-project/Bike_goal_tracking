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

sql = "SELECT date, hr, CONCAT (systolic, '/', diastolic, 'mmHg'), notes FROM t_blood_pressure"

mycursor.execute(sql)
results = list(mycursor.fetchall())

df = pd.DataFrame(results)
df.columns =['Date','HR per min', 'Diastolic/Systolic', 'Notes']

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
    col_width=[3, 2, 3, 9]
)
