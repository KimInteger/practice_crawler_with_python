import requests
from bs4 import BeautifulSoup
import json

def fetch_titles(page_number,keyword):
    url = f'https://cyphers.nexon.com/article/free?page={page_number}'
    response = requests.get(url)
    print(f"{page_number}페이지 시작")
    
    if response.status_code != 200:
        print(f"Failed to retrieve page {page_number}")
        return []
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    titles = []
    
    # 모든 <a> 태그에서 title 속성 수집
    for link in soup.find_all('a', title=True):  # title 속성 있는 <a> 태그만
        if keyword in link['title'] :
            titles.append(link['title'])
            
        # 키워드가 포함된 타이틀이 있을 경우 페이지 종료 메시지 출력
    if titles:
        print(f"{page_number}페이지 종료 - {len(titles)}개의 제목이 발견되었습니다.")
    else:
        print(f"{page_number}페이지 종료 - 제목이 발견되지 않았습니다.")
    
    return titles

def save_to_md(data,keyword):
    # .md 파일로 저장
    with open(f'./crawling_data/{keyword}.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)  # JSON 포맷으로 다듬어 저장


def main(start,end,keyword):
    collected_data = {}
    
    # 예를 들어, 페이지 1부터 10까지 수집 (필요에 따라 범위 변경)
    for page in range(start, end):
        titles = fetch_titles(page,keyword)
        collected_data[page] = titles
    
    save_to_md(collected_data,keyword)
    print(f"Titles have been saved to '{keyword}.json'.")

if __name__ == "__main__":
    start = input("몇페이지부터 ?:")
    end = input("몇페이지 까지?")
    keyword = input("무슨 키워드로 ? :")
    main(int(start),int(end),keyword)