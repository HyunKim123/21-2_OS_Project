import json, requests

def get_lm_info(region,landmark):
    
    url = requests.get("https://powerful104.pythonanywhere.com/recomm/get_lm_info?region="+region+"&landmark="+landmark)
    text = url.text
    data = json.loads(text)
    return [data['info'],data['address']]

"""
print(get_lm_info("경기_군포시","반월호수"))

관광지 정보와 주소 반환
"""