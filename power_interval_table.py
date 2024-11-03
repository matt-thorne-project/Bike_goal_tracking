import psycopg2
from matplotlib import pyplot as plt
import pandas as pd
import df2img

connection = psycopg2.connect(
  host = "xxx",
  port = "xxx",
  user = "read_only",
  password = "read_only",
  database = "Bike_goal"
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
ORDER BY
    date DESC
"""

cursor.execute(sql)
results = list(cursor.fetchall())

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