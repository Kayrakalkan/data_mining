import pandas as pd
import requests
import re

excel_file = 'data.xlsx'
df = pd.read_excel(excel_file)

# Sütun adlarını yazdır
print(df.columns)