import pandas as pd
import plotly.express as px  # For quick charts
import plotly.graph_objects as go  # For custom/complex charts
import os.path as path
import os

def feed_csv(file_path = ''):
    """
        Extract csv data.

        Parameters:
                    file_path (str) : CSV file path.
        
        Returns:
                    data_frame (pandas.df) : Data frame data.
        
        Exception:

    """
    try:
        # Check if the file exists.
        if not path.exists(file_path):
            raise RuntimeError('File does not exist!')

        # Read the csv data.
        df = pd.read_csv(file_path)

        return df
    
    except Exception:
        raise 

def add_plot_properties(title, y_axis, x_axis):
    

def plot(df : pd.DataFrame, timestamp_col_name = "time_s"):
    
    # Convert date column
    df["Date"] = pd.to_datetime(df[timestamp_col_name])

    # Line plot
    fig = px.line(df, x="Date", y="Value", title="Simple Line Chart")
    fig.show()

