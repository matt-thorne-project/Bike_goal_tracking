import psycopg2
from matplotlib import pyplot as plt
import pandas as pd
import df2img

connection = psycopg2.connect(
  host = "xxx",
  port = "xxx",
  user = "xxxx",
  password = "xxxx",
  database = "xxxx"
)

cursor = connection.cursor()

sql = "SELECT date, hr, CONCAT (systolic, '/', diastolic, 'mmHg'), notes FROM bikes.t_blood_pressure"

cursor.execute(sql)
results = list(cursor.fetchall())

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