import pandas as pd
import os.path as path
import os

def feed_csv(file_path = ''):
    """
        Extract csv data.

        Parameters:
                    file_path (str) : CSV file path.
        
        Returns:

        
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

