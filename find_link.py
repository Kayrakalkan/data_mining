import pandas as pd
import requests
import re
import math

excel_file = 'data.xlsx'
df = pd.read_excel(excel_file)

success_count = 0

for index, row in df.iterrows():
    company_name = row['company_name_test']
    
    if pd.isna(company_name) or not isinstance(company_name, str):
        continue
    
    clean_company_name = re.sub(r'[-.() * inc ınc ltd]', '', company_name.lower())
    
    url = f"http://www.{clean_company_name}.com"
    
    try:
        response = requests.get(url)
        
        if response.status_code == 200:
            success_count += 1
        else:
            print(f" unsuccesfull request: {url} - Status Code: {response.status_code}")
    
    except requests.exceptions.RequestException as e:
        print(f" error : {url} - {e}")

print(f"counter: {success_count}")
