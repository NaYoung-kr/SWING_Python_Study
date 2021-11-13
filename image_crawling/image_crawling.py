import os
import urllib.request
from bs4 import BeautifulSoup

# 오프너 객체를 생성해 헤더를 추가
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/36.0.1941.0 Safari/537.36')]
urllib.request.install_opener(opener)

# 웹툰 폴더 생성 및 이동
os.mkdir("청춘 블라썸")
os.chdir("청춘 블라썸")

# 웹툰 회차 목록 페이지 크롤링
web = urllib.request.urlopen('https://comic.naver.com/webtoon/list?titleId=746834&page=3')
soup = BeautifulSoup(web, 'html.parser')
tmp = soup.findAll('td', {"class":"title"})

for p in tmp:
    # 회차 제목에 있는 ':' 제거
    string = p.find("a").text
    string = string.replace(':', "")

    # 회차 별 폴더 생성 및 이동
    os.mkdir(string)
    os.chdir(string)

    # 회차 별 페이지 크롤링
    web2 = urllib.request.urlopen('https://comic.naver.com' + p.find("a")['href'])
    soup2 = BeautifulSoup(web2, 'html.parser')
    tmp2 = soup2.find('div', {"class": "wt_viewer"})

    # 회차 별 이미지 저장
    index = 1
    for img in tmp2.findAll('img'):
        urllib.request.urlretrieve(img['src'], str(index)+".jpg")
        index += 1

    # 이전 폴더로 이동
    os.chdir("..")
