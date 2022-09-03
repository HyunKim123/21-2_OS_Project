import pymongo as pm
import pandas as pd
import certifi
import regions

#지역명 가져오기
region_list = regions.get_regions()

#클라이언트 연결
client = pm.MongoClient('mongodb+srv://OSSPCOCONUT:coconut123@ossp-cluster.3vu4p.mongodb.net/test?retryWrites=true&w=majority', tlsCAFile=certifi.where())

for region in region_list:
    #지역 데이터프레임생성
    data = pd.read_csv("./2021-2-OSSP2-Coconut-1/Preprocessing/Crawling/Blog_Crawling_Data/" + region + ".csv")
    print(region+" 삽입중")
    #해당지역 DB와 collection 생성
    db = client["crawling_data"]
    col = db[region]

    overlap_check={}
    #해당지역 크롤링 데이터 DB에 삽입
    for row in range(len(data)):
        if data.iloc[row,0] == " ":
            break
        elif data.iloc[row,0] in overlap_check:
            continue
        else:
            overlap_check[data.iloc[row,0]] = 0
        insert_data = {'header':str(data.iloc[row,0]), "contents":str(data.iloc[row,1]), "date":str(data.iloc[row,2])}
        col.insert_one(insert_data)
client.close()
