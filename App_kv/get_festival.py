import json, requests
import certifi

def get_fstv(region):
    
    url = requests.get("https://powerful104.pythonanywhere.com/recomm/get_fstv?region="+region, verify = certifi.where())
    text = url.text
    data = json.loads(text)
    return data['festivals']

'''
test = get_fstv("강원_동해시")
print(test[0])
'''