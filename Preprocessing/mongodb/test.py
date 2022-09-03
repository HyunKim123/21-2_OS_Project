import pymongo as pm
import certifi
import regions

#지역명 가져오기
region_list = regions.get_regions()

#클라이언트 연결
client = pm.MongoClient('mongodb+srv://OSSPCOCONUT:coconut123@ossp-cluster.3vu4p.mongodb.net/feature_data?retryWrites=true&w=majority', tlsCAFile=certifi.where())

db = client["feature_data"]
col = db['서울_종로구']

for data in col.find().sort([('feature_value',-1)]).limit(10):
    print(data['feature_name'], end=" ")