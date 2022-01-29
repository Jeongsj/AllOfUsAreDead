import json
from datetime import datetime, timedelta


# 기존 json 파일 읽어오기
with open("./data_original.json", 'r', encoding="utf-8") as file:
    data = json.load(file)

chat_data = []
actor_list = ["박지후", "윤찬영", "조이현", "로몬", "유인수", "이유미", "임재혁"]
# 데이터 수정
for i in data:
    for j in i:
        user_id = j["user"]["id"]
        user_name = j["user"]["name"]
        if user_name not in actor_list: continue
        text_id = j["id"]
        time = j["created_at"]
        b = datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%fZ')
        b = b + timedelta(hours=9)
        text = j["text"]
        chat_data.append((b.strftime("%Y-%m-%d %H:%M:%S"), user_name, text))
        print(j["text"])

print(len(chat_data))


# 기존 json 파일 덮어쓰기
with open("./actor.json", 'w', encoding='utf-8') as file:
    json.dump(chat_data, file, indent="\t", ensure_ascii=False)