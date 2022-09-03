import pymongo as pm
import certifi
import regions

def del_data(client):
    #지역명 가져오기
    region_list = regions.get_regions()
    
    for region in region_list:
        #해당지역 DB와 collection 생성
        db = client["crawling_data"]
        col = db[region]

        # date가 '**시간전'과 같은 데이터 모두 삭제
        print(region+" 불필요 데이터 삭제중")
        col.delete_many({'date':{'$regex': '시간'}})