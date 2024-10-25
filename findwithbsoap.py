import requests
from bs4 import BeautifulSoup
import pandas as pd

input_file = "data.xlsx"  
df = pd.read_excel(input_file)

companies = df['company_name_test'].tolist()

data = []

def search_company_on_ddg(company_name):
    search_query = f"{company_name} website"
    search_url = f"https://duckduckgo.com/html?q={search_query}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')

    result = soup.find('a', class_='result__url')
    if result:
        return result.text.strip()
    return None


for company in companies:
    website = search_company_on_ddg(company)
    print(f"Company: {company}, Website: {website}")  
    data.append({
        "Company": company,
        "Website": website if website else "Not Found"
    })

output_file = "company_websites_ddg.xlsx"
df_output = pd.DataFrame(data)
df_output.to_excel(output_file, index=False)

