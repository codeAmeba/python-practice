import requests
from bs4 import BeautifulSoup

indeed_result = requests.get(
    "https://www.indeed.com/jobs?q=javascript&limit=50")

# requests library를 사용하여 웹페이지 정보를 가져오기
# status_code를 확인하여 제대로 작동하는 지 확인

# html을 파싱할 수 있는 beautifulsoup library 설치 및 임포트
# https://www.crummy.com/software/BeautifulSoup/bs4/doc.ko/

indeed_soup = BeautifulSoup(indeed_result.text, "html.parser")

pagination = indeed_soup.find("div", {"class": "pagination"})

links = pagination.find_all("a")
pages = []
for link in links[:-1]:
    pages.append(int(link.string))

max_page = pages[-1]
