# pip install requests
# pip install bs4

import requests
from bs4 import BeautifulSoup

response = requests.get('https://qiita.com')
soup = BeautifulSoup(response.text, 'html.parser')

# ページ内のh2タグを取得する
for h2 in soup.find_all('h2'):
    print(h2.text)
