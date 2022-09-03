import json, requests
import certifi

def get_fstv_info(region,festival):
    
    url = requests.get("https://powerful104.pythonanywhere.com/recomm/get_fstv_info?region="+region+"&festival="+festival,  verify = certifi.where())
    text = url.text
    data = json.loads(text)
    return [data['place'],data['address']]

'''
test = get_fstv_info("전남_진도군", "제42회 진도신비의 바닷길축제")
'''


