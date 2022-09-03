import json, requests
import certifi

def get_lm(region):
    
    url = requests.get("https://powerful104.pythonanywhere.com/recomm/get_lm?region="+region, verify = certifi.where())
    text = url.text
    data = json.loads(text)
    return data['landmarks']

'''
print(get_lm("경기_오산시"))
'''