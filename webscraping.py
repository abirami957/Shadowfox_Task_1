import requests
import pandas as pd
from bs4 import BeautifulSoup

Page_num = 1
datas = []

while True:
    url = f'https://www.scrapethissite.com/pages/forms/?page_num={Page_num}&per_page=100'
    res = requests.get(url)
    soup = BeautifulSoup(res.content, 'lxml')
    trs = soup.find_all('tr', {'class': 'team'})  # Corrected 'trs' to 'tr'
    
    if trs:
        for tr in trs:
            data = {td.get('class')[0]: td.text.strip() for td in tr.find_all('td')}
            datas.append(data)
        Page_num += 1
    else:
        break

df = pd.DataFrame(datas)
df.to_excel('pagination1.xlsx', index=False)
