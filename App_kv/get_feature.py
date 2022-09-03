import json, requests 
import certifi

def get_f(region):
    url = requests.get("https://powerful104.pythonanywhere.com/recomm/get_f?region="+region, verify = certifi.where())
    text = url.text
    data = json.loads(text)
    return data['features']

"""
print(get_f("강원_강릉시"))
"""