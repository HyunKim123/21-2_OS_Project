import json, requests

def get_fstv(region):
    
    url = requests.get("https://powerful104.pythonanywhere.com/recomm/get_fstv?region="+region)
    text = url.text
    data = json.loads(text)
    return data['festivals']

"""
print(get_fstv("경기_군포시"))
"""