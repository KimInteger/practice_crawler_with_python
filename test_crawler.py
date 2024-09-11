import requests
from bs4 import BeautifulSoup 

# naver는 /요청에 대한 크롤링은 허용함.
url = "https://www.naver.com"
response = requests.get(url)

# response확인 이게 객첸지 뭔지 알아야지.
print(response)

"""
    HTML의 구문 분석
    xhr을 사용할 때 응답된 객체에서 text 객체를 가져오는 것.
"""
soup = BeautifulSoup(response.text,'html.parser')

title = soup.find('h1')
if title :
    print("페이지의 h1태그", title)
else :
    print("h1태그가 없는데용?")