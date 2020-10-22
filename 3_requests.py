import requests

res = requests.get("http://google.com")
#res2 = requests.get("http://nadocoding.tistory.com")

print('응답코드 :', res.status_code) # 200이면 정상
#print('응답코드 :', res2.status_code)

if res.status_code == requests.codes.ok:
    print("정상입니다.")
else:
    print("문제가 생겼습니다. [에러코드 {}]".format(res.status_code))

print(len(res.text))
print(res.text)

with open("mygoogle.html", 'w', encoding='utf-8') as f:
    f.write(res.text)