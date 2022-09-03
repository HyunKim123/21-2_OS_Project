import pymongo as pm
import pandas as pd
import certifi

def input(client, data):

    for row in range(len(data)):
        
        region = data.iloc[row]['region']
        print(region+" 삽입중")
        
        #해당지역 DB와 collection 생성
        db = client["feature_data"]
        collec = db[region]
        collec.remove({})

        #해당지역 특성값 데이터 DB에 삽입
        for col in range(len(data.columns)-1):
            insert_data = {"feature_name":str(data.columns[col]), "feature_value": float(data.iloc[row][data.columns[col]])}
            collec.insert_one(insert_data)