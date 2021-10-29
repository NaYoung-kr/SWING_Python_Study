import urllib.request
from bs4 import BeautifulSoup

web = urllib.request.urlopen('http://www.swu.ac.kr/www/swuniversity.html')
soup = BeautifulSoup(web, 'html.parser')
tmp = soup.findAll('li')

print("*** 서울여자대학교 학과 및 홈페이지 정보 ***\n")
print("학과\t\t\t\t홈페이지")

for p in tmp:
    if str(p).find('학과') != -1 or str(p).find('전공') != -1:
        print(p.text, end="\t\t")

        web2 = urllib.request.urlopen('http://www.swu.ac.kr' + p.find("a")['href'])
        soup2 = BeautifulSoup(web2, 'html.parser')
        tmp2 = soup2.find('div', {"style": "text-align: center; margin-top: 45px;"})

        if str(tmp2).find('홈페이지') != -1 and str(tmp2).find('<!--') == -1:
            print(tmp2.find("a")['href'])
        else:
            print("홈페이지 없음")