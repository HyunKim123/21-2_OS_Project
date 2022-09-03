import pymongo as pm
import pandas as pd
import certifi

#클라이언트 연결
client = pm.MongoClient('mongodb+srv://OSSPCOCONUT:coconut123@ossp-cluster.3vu4p.mongodb.net/test?retryWrites=true&w=majority', tlsCAFile=certifi.where())

#feature data 불러오기
data = pd.read_csv("./2021-2-OSSP2-Coconut-1/algorithm/matrix_231x201_211108.csv")

for row in range(len(data)):
    
    region = data.iloc[row]['region']
    print(region+" 삽입중")
    
    #해당지역 DB와 collection 생성
    db = client["feature_data"]
    collec = db[region]

    #해당지역 특성값 데이터 DB에 삽입
    for col in range(len(data.columns)-1):
        insert_data = {"feature_name":str(data.columns[col]), "feature_value": float(data.iloc[row][data.columns[col]])}
        collec.insert_one(insert_data)
client.close()
