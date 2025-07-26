# 📊 Big Data Visualization

This repository contains Python functions to plot structured huge, raw time-series datasets using Plotly for interactive visualizations and analysis.

## 🚀 Features
- 📈 Plots every other column (or selected columns)

- 🎨 Uses Plotly for clean and interactive visuals

- 🧼 Clean modular code with reusable functions

## 📁 Data Format
Your data should be in CSV format, like:

```csv
timestamp,sensor1,sensor2,sensor3,sensor4
2023-01-01 06:09:00.200, 1, 2, 3, 4
2023-01-02 06:09:00.300, 2, 3, 4, 5
...
```

## 🧠 Example Usage
```python 
from data_process import *

file_path = "data.csv"
timestamp_col_name = "timestamp"

# Retain the Dataframe.
df = feed_csv(file_path)

# Plot dataset against timestamps.
plot(df=df, timestamp_col_name=timestamp_col_name)
```