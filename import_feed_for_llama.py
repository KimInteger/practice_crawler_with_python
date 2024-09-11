import json
import os

def change_json_to_feed(feed, output_file_name=None):
    # JSON 파일 경로 설정
    change_feed = os.path.join(os.path.dirname(__file__), "crawling_data", f"{feed}.json")
    
    # JSON 파일 읽기
    with open(change_feed, 'r', encoding='utf-8') as f:
        try:
            data = json.load(f)  # JSON 파일을 딕셔너리로 파싱
        except json.JSONDecodeError as e:
            print(f"JSON 파일을 파싱하는데 실패했습니다: {e}")
            return []

    # 데이터가 리스트 형태인지 확인
    if not isinstance(data, dict):
        print("데이터 형식이 올바르지 않습니다. 딕셔너리 형태여야 합니다.")
        return []

    # URL 리스트 추출
    urls = []
    for key, value in data.items():
        if isinstance(value, list):  # 각 페이지의 데이터가 리스트로 저장된 경우
            for item in value:
                if 'url' in item:
                    urls.append({"url": item['url']})
    
    # 추출한 URL들을 output 파일에 저장
    if output_file_name != None :
        with open(output_file_name, "w", encoding="utf-8") as f:
            for url in urls:
                f.write(f"{url},\n")  # URL을 파일에 기록
    else :
        print("파일 생성은 안해용")
    return urls

if __name__ == "__main__":
    # 사용자로부터 입력 받기
    file_name = input("어느 파일? (파일명만 입력): ")
    output = input("출력 파일 이름은? (파일명만 입력): ")
    
    # 출력 파일 경로 설정
    output_file_name = os.path.join(os.path.dirname(__file__), "crawling_data", "llama_data", f"{output}.jsonl")
    
    # URL 추출 및 파일 저장 함수 호출
    urls = change_json_to_feed(file_name, output_file_name)
    
    print("추출된 URL 목록:")
    for url in urls:
        print(url['url'])
