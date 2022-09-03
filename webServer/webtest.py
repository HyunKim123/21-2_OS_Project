import requests
userdata = {"name" : '박종길', "student_id": 2018166432}
resp = requests.post("http://osspcoconut.dothome.co.kr/test.php", data = userdata)
print(resp.text)