import pandas as pd
import os

# Dictionary to manage filenames
DATA_FILES = {
    "benin": "benin-malanville.csv",
    "sierraleone": "sierraleone-bumbuna.csv",
    "togo": "togo-dapaong_qc.csv"
}

# Get full path for 
def get_file_path(file_key):
    current_dir = os.getcwd()
    return os.path.join(current_dir, "../data", DATA_FILES[file_key])

# Data loader class
class CSVData:
    def __init__(self, file_path):
        self.file_path = file_path

    def load_data(self):
        return pd.read_csv(self.file_path)
