import UPDT_crawl
import UNC_del
import get_regVec
import input_feature
import certifi
import pymongo as pm


#클라이언트 연결
client = pm.MongoClient('mongodb+srv://OSSPCOCONUT:coconut123@ossp-cluster.3vu4p.mongodb.net/test?retryWrites=true&w=majority', tlsCAFile=certifi.where())

#신규데이터 크롤링
UPDT_crawl.crawl(client)

#불필요 데이터 삭제
UNC_del.del_data(client)

#자연어 처리후 특징_값 데이터 얻어오기
feature_data = get_regVec.get(client)

#mongoDB의 특징_값 데이터 최신화
input_feature.input(client, feature_data)

print("Update complete!")