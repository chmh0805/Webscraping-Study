import requests
import re
from bs4 import BeautifulSoup
import openpyxl

def find_product(product, pages=5):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.75 Safari/537.36"}

    wb = openpyxl.Workbook()
    sheet = wb.active
    sheet['A1'] = "광고 제품은 제외하고, 평점 4.5 이상, 리뷰수 50개 이상, 로켓배송 상품만 검색합니다."
    sheet.append(["제품명", "가격(단위:원)", "평점", "리뷰수"])

    for page in range(1, pages+1):

        url = "https://www.coupang.com/np/search?q={0}&channel=user&component=&eventCategory=SRP&trcid=&traid=&sorter=scoreDesc&minPrice=&maxPrice=&priceRange=&filterType=&listSize=36&filter=&isPriceRange=false&brand=&offerCondition=&rating=0&page={1}&rocketAll=false&searchIndexingToken=1=4&backgroundColor=".format(product, page)
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        soup = BeautifulSoup(res.text, 'lxml')
        items = soup.find_all("li", attrs={'class': re.compile("^search-product")})

        for item in items:
            # 로켓 배송 상품만(로켓배송이 아니면 제외)
            if not item.find("span", attrs={'class': 'badge rocket'}):
                continue

            # 광고 제품은 제외
            ad_badge = item.find("span", attrs={'class': 'ad-badge-text'})
            if ad_badge:
                continue

            name = item.find("div", attrs={'class': 'name'}).get_text() # 제품명
            
            price = item.find("strong", attrs={'class': 'price-value'}).get_text()# 가격
            
            # 리뷰 50개 이상, 평점 4.5이상 되는 것만 조회
            rate = item.find("em", attrs={'class': 'rating'}) # 평점
            if rate: # rate가 있으면
                rate = rate.get_text()
            else:
                continue
            
            rate_count = item.find("span", attrs={'class': 'rating-total-count'}) # 평점 수
            if rate_count: # 평점 개수가 있으면
                rate_count = rate_count.get_text()[1:-1] # 출력 예 : (26)
            else:
                continue
            
            if (float(rate) >= 4.5) and int(rate_count) >= 50:
                print(name, price, "평점 :", rate, "(" + rate_count + ")")
                sheet.append([name, price, rate, rate_count])
    
    wb.save('{} 검색결과.xlsx'.format(product))

if __name__ == "__main__":
    product = input("쿠팡에 검색할 단어를 입력하세요 : ")
    page = int(input("몇페이지 검색할 건지 입력하세요 : "))
    find_product(product, page)