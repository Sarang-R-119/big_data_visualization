from data_process import *

file_path = input("Enter the file path of the time-series dataset!")
timestamp_col_name = input("Enter timestamp column name!")

df = feed_csv(file_path.replace('\\', '\\\\'))

plot(df=df, timestamp_col_name=timestamp_col_name)