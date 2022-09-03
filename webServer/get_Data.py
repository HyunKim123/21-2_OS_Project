import json, requests 

url = requests.get("http://osspcoconut.dothome.co.kr/get_Json.php")
text = url.text
data = json.loads(text)
for i in data:
    print(i)

"""
http://osspcoconut.dothome.co.kr/get_Json.php내에서 json 형식으로 출력된 DB 값을 받아서 출력한다.
"""