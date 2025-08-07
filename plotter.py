import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter
import math
import os 
import sys
import pandas as pd
from openpyxl import load_workbook
import json
settings_path = "settings/settings.json"
excel_path = "data/20250707Glass12_witharray.xlsx"

def get_sheetnames(Filepath):
    wb = load_workbook(Filepath, read_only=True, keep_links=False)
    return wb.sheetnames

def get_settings_file(Settings_path):
    with open(Settings_path,'r') as f:
        return json.load(f)

def get_excel_file(Excel_path, Sheet_name):
    file = pd.read_excel(Excel_path, sheet_name = Sheet_name,header=0, skiprows=[1,2])
    mask = file.map(lambda x: isinstance(x, str)).any(axis=1)
    file = file[~mask].reset_index(drop=True)
    return file


settings = get_settings_file(settings_path)
plt.style.use(settings["plotstyle"])

sheetnames = get_sheetnames(settings["input_file"])
del sheetnames[:settings["skip_sheets"]]
print(sheetnames)


processed_data = []

for sheet in sheetnames:
    fig, ax = plt.subplots(figsize=(12,5))
    ax2 = ax.twinx()
    ax3 = ax.twinx()
    ax3.spines.right.set_position(("axes",1.1))
    
    
    





