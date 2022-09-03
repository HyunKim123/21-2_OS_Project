import json, requests
import certifi

def get_lm_info(region,landmark):
    
    url = requests.get("https://powerful104.pythonanywhere.com/recomm/get_lm_info?region="+region+"&landmark="+landmark, verify = certifi.where())
    text = url.text
    data = json.loads(text)
    return [data['info'],data['address']]

'''
test= get_lm_info("경기_군포시","반월호수")


cnt = 0
len = len(test[0])
for i in range(len):
    if test[0][i] == " " and cnt > 15:
       L = list(test[0])
       L[i] = "\n"
       test[0]=''.join(L)
       cnt = 0
    else:
        cnt+=1



print(test[0])'''