from bs4 import BeautifulSoup
from import_feed_for_llama import change_json_to_feed
import requests
import json
import os

def import_content(keyword):
    # '공략' 키워드의 JSON에서 URL들을 가져옴
    urls = change_json_to_feed("공략")
    
    collect_data = {}

    for url in urls:
        response = requests.get(url['url'])
        
        if response.status_code != 200:
            print(f"URL {url['url']}에서 데이터를 가져오는데 실패했습니다.")
            continue
        
        soup = BeautifulSoup(response.text, "html.parser")
        print(f"{url['url']} 가져오는 중")
        
        # 'board_view_con' 클래스가 있는 div 태그 찾기
        content_div = soup.find('div', class_='board_view_con')
        
        if not content_div:
            print(f"'board_view_con' 클래스를 가진 div 태그를 찾을 수 없습니다.")
            continue
        
        contents = []
        
        # 'board_view_con' div 내부의 p 태그에서 조건에 맞는 내용 수집
        for p in content_div.find_all('p'):
            text_content = p.get_text(strip=True)  # p 태그의 텍스트 내용
            if text_content and not text_content.startswith('<br>'):
                contents.append(text_content)
        
        # 수집된 데이터 저장
        collect_data[url['url']] = {"제목": url.get("제목", "제목 없음"), "내용": " ".join(contents)}
    
    # 수집된 데이터를 JSON 파일로 저장
    if collect_data:
        output_path = os.path.join('crawling_data', f'{keyword}.json')
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(collect_data, f, ensure_ascii=False, indent=4)  # JSON 포맷으로 저장
        print(f"파싱 완료. 데이터가 {output_path}에 저장되었습니다.")
    else:
        print("수집된 데이터가 없습니다.")


if __name__ == "__main__":
    keyword = input("키워드 입력: ")
    import_content(keyword)
