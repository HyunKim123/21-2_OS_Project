import pymongo as pm
import certifi
import regions

def del_UNC(client):
    #지역명 가져오기
    region_list = regions.get_regions()

    #클라이언트 연결
    client = pm.MongoClient('mongodb+srv://OSSPCOCONUT:coconut123@ossp-cluster.3vu4p.mongodb.net/test?retryWrites=true&w=majority', tlsCAFile=certifi.where())

    for region in region_list:
        #해당지역 DB와 collection 생성
        db = client["crawling_data"]
        col = db[region]

        # date가 '**시간전'과 같은 데이터 모두 삭제
        print(region+" 불필요 데이터 삭제중")
        col.delete_many({'date':{'$regex': '시간'}})