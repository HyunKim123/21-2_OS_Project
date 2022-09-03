import json, requests 
import certifi

def get_r(features):
    features = '-'.join(features)
    url = requests.get("https://powerful104.pythonanywhere.com/recomm/get_r?features="+features, verify = certifi.where())
    text = url.text
    data = json.loads(text)
    return data['regions']

"""
print(get_r(['강원_강릉시','바다', '동해', '해변']))
"""