import requests

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}
url = "http://nadocoding.tistory.com"

res = requests.get(url, headers=headers)
# res.raise_for_status()

with open("nadocoding.html", 'w', encoding='utf8') as f:
    f.write(res.text)