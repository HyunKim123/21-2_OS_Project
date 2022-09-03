import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import datetime
from konlpy.tag import Okt
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
import pymongo as pm
import certifi
import regions

def get_regVec(client):
    
    region_list = regions.get_regions()
    
    matrix_231x2 = []
    for region in region_list:
        #해당지역 DB와 collection 생성
        db = client["crawling_data"]
        col = db[region]
        print(region+" 추출중")
        all_sentence = ''
        for data in col.find():
            all_sentence+=data['contents']
        matrix_231x2.append([region,all_sentence])
        
    #한문장으로 만들기
    matrix_231x2 = pd.DataFrame(data= matrix_231x2, columns=['region', 'sentences'])

    #231X(region,sentences)받아오는 코드 들어갈자리
    #정규표현식을 이용해 한글만 남겨주는 작업
    matrix_231x2['sentences'] = matrix_231x2['sentences'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")
    
    while(1):
        
        db = client["stopword"]
        col = db['main']
        stopword = []
        for word in col.find({}):
            stopword.append(word["word_name"])
        
        #형태소 분석

        twitter = Okt() 
        morphs = []
        num=0
        tokenized_data = []
        for sentense in matrix_231x2.iloc[:,1]:
            morphs = []
            morphs.append(twitter.pos(sentense))
            noun_list=[] 
            for sentence in morphs : 
                for word, tag in sentence : 
                    if (tag in ['Noun'] and word not in stopword):
                        noun_list.append(word)
                tokenized_data.append(noun_list)
            s=" ".join(noun_list)
            matrix_231x2.iloc[num,1]=s
            num=num+1
        ################

        tfidfv = TfidfVectorizer(max_features=200,min_df=0.3,analyzer='word').fit(matrix_231x2.sentences)
        X=tfidfv.transform(matrix_231x2.sentences)
        print(tfidfv.vocabulary_.keys())
        while(1):
            plus_stopword = input("불용어 처리 할 키워드를 입력해주세요(이번 단계에 아예 없다면 x 입력,이번 단계의 마지막 입력일시 그냥 enter) \n =>")
            if plus_stopword=='x':
                need_update=0
                break
            if plus_stopword=='':
                break
            insert_data = {"word_name":str(plus_stopword)}
            col.insert_one(insert_data)
        if need_update==0:          
            tfidf_dict = tfidfv.get_feature_names()
            data_array = X.toarray()
            tfidf_df=pd.DataFrame(data=data_array,columns=tfidf_dict)
            tfidf_df['region']=matrix_231x2.region
            return tfidf_df