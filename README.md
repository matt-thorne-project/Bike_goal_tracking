# Bike Goals and Health Stats Tracking
Project to using Python and MySQL to allow for viewing longterm changes in my cycling performance and some health statistics.

## Requirements
+ **MySQL Database** - this can be locally hosted or remotely
+ **Python3** - the `requirements.txt` will cover the pip packages required by Python
+ **Anaconda or jupyter notebook** - if you want to view the results locally
+  **SQL Admin Software**

## Initial Setup
1. Create your database and connect it to your admin tool.
2. Run `weight db tables.sql` to create the tables required.
3. Update `key_file.py` with your database connection details, this will be used for the Python scripts to access the database.

## Adding Stats
You can either run the python files to add readings interactively or run the inserts manually in your SQL Admin tool

## Viewing Your Perfomance Changes in Anaconda
The open `ftp_graphing.py` and `blood_pressure_tables.py` and copy the scripts into jupyter notebook to view the graphs of your changes. 
You will need to include the database connection inforamtion.