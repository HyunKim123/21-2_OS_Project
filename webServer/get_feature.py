import json, requests 

def get_f(region):
    url = requests.get("https://powerful104.pythonanywhere.com/recomm/get_f?region="+region)
    text = url.text
    data = json.loads(text)
    return data['feature']