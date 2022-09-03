#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


# In[75]:


region_list=['서울_종로구',
'서울_중구',
'서울_용산구',
'서울_성동구',
'서울_광진구',
'서울_동대문구',
'서울_중랑구',
'서울_성북구',
'서울_강북구',
'서울_도봉구',
'서울_노원구',
'서울_은평구',
'서울_서대문구',
'서울_마포구',
'서울_양천구',
'서울_강서구',
'서울_구로구',
'서울_금천구',
'서울_영등포구',
'서울_동작구',
'서울_관악구',
'서울_서초구',
'서울_강남구',
'서울_송파구',
'서울_강동구',
'부산_중구',
'부산_서구',
'부산_동구',
'부산_영도구',
'부산_부산진구',
'부산_동래구',
'부산_남구',
'부산_북구',
'부산_해운대구',
'부산_사하구',
'부산_금정구',
'부산_강서구',
'부산_연제구',
'부산_수영구',
'부산_사상구',
'부산_기장군',
'대구_중구',
'대구_동구',
'대구_서구',
'대구_남구',
'대구_북구',
'대구_수성구',
'대구_달서구',
'대구_달성군',
'인천_중구',
'인천_동구',
'인천_미추홀구',
'인천_연수구',
'인천_남동구',
'인천_부평구',
'인천_계양구',
'인천_서구',
'인천_강화군',
'인천_옹진군',
'광주_동구',
'광주_서구',
'광주_남구',
'광주_북구',
'광주_광산구',
'대전_동구',
'대전_중구',
'대전_서구',
'대전_유성구',
'대전_대덕구',
'강원_춘천시',
'강원_원주시',
'강원_강릉시',
'강원_동해시',
'강원_태백시',
'강원_속초시',
'강원_삼척시',
'강원_홍천군',
'강원_횡성군',
'강원_영월군',
'강원_평창군',
'강원_정선군',
'강원_철원군',
'강원_화천군',
'강원_양구군',
'강원_인제군',
'강원_고성군',
'강원_양양군',
'울산_중구',
'울산_남구',
'울산_동구',
'울산_북구',
'울산_울주군',
'세종_세종시',
'경기_수원시',
'경기_성남시',
'경기_의정부시',
'경기_안양시',
'경기_부천시',
'경기_광명시',
'경기_평택시',
'경기_동두천시',
'경기_안산시',
'경기_고양시',
'경기_과천시',
'경기_구리시',
'경기_남양주시',
'경기_오산시',
'경기_시흥시',
'경기_군포시',
'경기_의왕시',
'경기_하남시',
'경기_용인시',
'경기_파주시',
'경기_이천시',
'경기_안성시',
'경기_김포시',
'경기_화성시',
'경기_광주시',
'경기_양주시',
'경기_포천시',
'경기_여주시',
'경기_연천군',
'경기_가평군',
'경기_양평군',
'충북_청주시',
'충북_충주시',
'충북_제천시',
'충북_보은군',
'충북_옥천군',
'충북_영동군',
'충북_진천군',
'충북_괴산군',
'충북_음성군',
'충북_단양군',
'충북_증평군',
'충남_천안시',
'충남_공주시',
'충남_보령시',
'충남_아산시',
'충남_서산시',
'충남_논산시',
'충남_계룡시',
'충남_당진시',
'충남_금산군',
'충남_연기군',
'충남_부여군',
'충남_서천군',
'충남_청양군',
'충남_홍성군',
'충남_예산군',
'충남_태안군',
'전북_전주시',
'전북_군산시',
'전북_익산시',
'전북_정읍시',
'전북_남원시',
'전북_김제시',
'전북_완주군',
'전북_진안군',
'전북_무주군',
'전북_장수군',
'전북_임실군',
'전북_순창군',
'전북_고창군',
'전북_부안군',
'전남_목포시',
'전남_여수시',
'전남_순천시',
'전남_나주시',
'전남_광양시',
'전남_담양군',
'전남_곡성군',
'전남_구례군',
'전남_고흥군',
'전남_보성군',
'전남_화순군',
'전남_장흥군',
'전남_강진군',
'전남_해남군',
'전남_영암군',
'전남_무안군',
'전남_함평군',
'전남_영광군',
'전남_장성군',
'전남_완도군',
'전남_진도군',
'전남_신안군',
'경북_포항시',
'경북_경주시',
'경북_김천시',
'경북_안동시',
'경북_구미시',
'경북_영주시',
'경북_영천시',
'경북_상주시',
'경북_경산시',
'경북_군위군',
'경북_의성군',
'경북_청송군',
'경북_영양군',
'경북_영덕군',
'경북_청도군',
'경북_고령군',
'경북_성주군',
'경북_칠곡군',
'경북_예천군',
'경북_봉화군',
'경북_울진군',
'경북_울릉도',
'경남_창원시',
'경남_마산시',
'경남_진주시',
'경남_진해시',
'경남_통영시',
'경남_사천시',
'경남_김해시',
'경남_밀양시',
'경남_거제시',
'경남_양산시',
'경남_의령군',
'경남_함안군',
'경남_창녕군',
'경남_고성군',
'경남_남해군',
'경남_하동군',
'경남_산청군',
'경남_함양군',
'경남_거창군',
'경남_합천군',
'제주도_제주시',
'제주도_서귀포시']


# In[120]:


#최종_지역sum_code

#빈 데이터프레임 생성
matrix_231x2 = pd.DataFrame(index=range(0,231), columns=['region', 'sentences']) 
#행 카운팅할 row변수생성
row=0
#반복(각 지역에 대해)
for region in region_list:
    region_data=pd.read_csv(region + ".csv",encoding="utf-8")
    
    matrix_231x2.iloc[row,0]=region
    matrix_231x2.iloc[row,1]=region_data.iloc[0,0]+region_data.iloc[0,1]
    
    #반복(각 지역의 크롤링 데이터 1050행에 대해)
    for i in range(1,1050):
        if ( region_data.iloc[i,0] in list(region_data.iloc[range(0,i),0]) ):
            break
        
        matrix_231x2.iloc[row,1]=matrix_231x2.iloc[row,1] + region_data.iloc[i,0] + region_data.iloc[i,1]
    
    #matrix_231x2 다음행으로 row 업데이트        
    row += 1

#데이터확인
print(matrix_231x2.head())
print(matrix_231x2.tail())
#행렬 csv파일로 저장
#matrix_231x2.to_csv("matrix_231x2.csv",encoding='utf-8-sig',index=True,header=True, sep=',')


# In[115]:


matrix_231x2


# In[121]:


#정규표현식을 이용해 한글만 남겨주는 작업
matrix_231x2['sentences'] = matrix_231x2['sentences'].str.replace("[^ㄱ-ㅎㅏ-ㅣ가-힣 ]","")
matrix_231x2


# In[122]:


#형태소 분석

from konlpy.tag import Twitter 
from collections import Counter

twitter = Twitter()
morphs = []
num=0
tokenized_data = []
for sentense in matrix_231x2.iloc[:,1]:
    morphs = []
    morphs.append(twitter.pos(sentense))
    noun_list=[] 
    for sentence in morphs : 
        for word, tag in sentence : 
            if (tag in ['Noun'] and ("것" not in word) and ("내" not in word)and ("나" not in word)and ("수"not in word) and("게"not in word)and("말"not in word) and ("등" not in word) and ("제" not in word) and ("륙" not in word)and ("끼" not in word)and ("인천" not in word)and ("강원" not in word)and ("충북" not in word)and ("충남" not in word)and ("충청" not in word)and ("전북" not in word)and ("전남" not in word)and ("전라" not in word)and ("경북" not in word)and ("경남" not in word)and ("경상" not in word)and ("도" not in word)and ("대전" not in word)and ("대구" not in word)and ("광주" not in word)and ("부산" not in word)and ("울산" not in word)and ("여행" not in word)and ("추천" not in word)and ("일차" not in word)and ("전국" not in word)and ("근처" not in word)and ("박일" not in word)and ("소개" not in word)and ("시간" not in word)and ("오늘" not in word)and ("후기" not in word)and ("정보" not in word)and ("인생" not in word)and ("타고" not in word)and ("빌라" not in word)and ("베스트" not in word)and ("비대" not in word)and ("택트" not in word)and ("최고" not in word)and ("위치" not in word)and ("방문" not in word)and ("주차" not in word)and ("가기" not in word)and ("서울" not in word) and ("생각" not in word) and ("다음" not in word) and ("여기" not in word) and ("명소" not in word) and ("가장" not in word) and ("문화" not in word) and
                ("사람" not in word) and ("주소" not in word) and ("지역" not in word) and ("테마" not in word) and ("코스" not in word) and ("이야기" not in word) and ("거리" not in word) and ("매일" not in word) and ("시작" not in word) and ("기분" not in word) and ("통영" not in word) and ("메뉴" not in word) and ("한번" not in word) and ("지금" not in word) and ("한국" not in word) and ("요즘" not in word) and ("월요일" not in word) and ("운영" not in word) and ("바로" not in word) and ("때문" not in word) and ("주변" not in word) and ("보고" not in word) and ("평일" not in word) and ("차로" not in word) and ("전문" not in word) and ("보시" not in word) and ("경우" not in word) and ("선택" not in word) and ("진자" not in word) and ("센터" not in word) and ("정식" not in word) and ("배달" not in word) and ("기준" not in word) and ("시기" not in word) and ("작년" not in word) and ("포함" not in word) and ("신상" not in word) and ("계속" not in word) and ("터미널" not in word) and ("단계" not in word) and ("안심" not in word) and ("반찬" not in word) and ("시시" not in word) and ("밥상" not in word) and ("더욱" not in word) and ("일단" not in word) and ("외관" not in word) and ("또한" not in word) and ("현지" not in word) and ("작성" not in word) and ("곡리" not in word) and ("자단" not in word) and ("동반" not in word) and ("태국" not in word) and
                ("가시" not in word) and ("영업" not in word) and ("전화번호" not in word) and ("입구" not in word) and ("느낌" not in word) and ("이번" not in word) and ("호텔" not in word) and ("장소" not in word) and ("문의" not in word) and ("숙소" not in word) and ("입장료" not in word) and ("무료" not in word) and ("세종" not in word) and ("우리" not in word) and ("예약" not in word) and ("휴무" not in word) and ("가능" not in word) and ("마음" not in word) and ("전화" not in word) and ("이용" not in word) and ("위해" not in word) and ("날씨" not in word) and ("매매" not in word) and ("완전" not in word) and ("남편" not in word) and ("뉴스" not in word) and ("생생" not in word) and ("맞이" not in word) and ("상품" not in word) and ("상황" not in word) and ("인스타" not in word) and ("기념" not in word) and ("여러" not in word) and ("롯데" not in word) and ("바퀴" not in word) and ("소식" not in word) and ("예정" not in word) and ("환영" not in word) and ("그램" not in word) and ("머리" not in word) and ("선물" not in word) and ("출장" not in word) and ("세트" not in word) and ("자락" not in word) and ("지구" not in word) and ("솔직" not in word) and ("관광객" not in word) and ("구매" not in word) and ("랜드" not in word) and ("타운" not in word) and
                ("강릉" not in word) and ("근교" not in word) and ("경기" not in word) and ("계획" not in word) and ("로번" not in word)and ("하루" not in word) and ("중앙" not in word) and ("지난" not in word) and ("오후" not in word) and ("처음" not in word) and ("공간" not in word) and ("모습" not in word) and ("출처" not in word) and ("홈페이지" not in word) and ("자리" not in word) and ("입장" not in word) and ("중구" not in word) and ("어디" not in word) and ("버스" not in word) and ("오전" not in word) and ("포스팅" not in word) and ("아침" not in word) and ("블로그" not in word) and ("건물" not in word) and ("다시" not in word) and ("세계" not in word) and ("가격" not in word) and ("세상" not in word) and ("매력" not in word) and ("스카이" not in word) and ("생방송" not in word) and ("투어" not in word) and ("찍기" not in word) and ("회관" not in word) and ("최초" not in word) and ("공항" not in word) and ("시국" not in word) and ("아빠" not in word) and ("절기" not in word) and ("기사" not in word) and ("공유" not in word) and
                ("마지막" not in word) and ("가지" not in word) and ("저희" not in word) and ("점심" not in word) and ("모두" not in word) and ("네이버" not in word) and ("시설" not in word) and ("대한" not in word) and ("학교" not in word) and ("이후" not in word) and ("가야" not in word) and ("호선" not in word) and ("사이" not in word) and ("식당" not in word) and ("원래" not in word) and ("마무리" not in word) and ("레이스" not in word) and ("탐방" not in word) and ("설치" not in word) and ("판매" not in word) and ("규모" not in word) and ("주민" not in word) and ("대해" not in word) and ("이유" not in word) and ("기간" not in word) and ("모든" not in word) and ("음식점" not in word) and ("선생" not in word) and ("현장" not in word) and ("월일" not in word) and ("서로" not in word) and ("온라인" not in word) and ("목적" not in word) and ("하니" not in word) and ("일찍" not in word) and ("곳곳" not in word) and ("소재" not in word) and ("일대" not in word) and ("별로" not in word) and ("태국" not in word) and ("부터" not in word) and
                ("조금" not in word) and ("주문" not in word) and ("고기" not in word) and ("대표" not in word) and ("진짜" not in word) and ("검색" not in word) and ("준비" not in word) and ("저녁" not in word) and ("가득" not in word) and ("영상" not in word) and ("발견" not in word) and ("리스트" not in word) and ("기행" not in word) and ("거의" not in word) and ("기록" not in word) and ("식사" not in word) and ("최대" not in word) and ("시대" not in word) and ("최근" not in word) and ("오시" not in word) and ("해외" not in word) and ("정자" not in word) and ("항상" not in word) and ("서이추" not in word) and ("추가" not in word) and ("마스크" not in word) and ("홍보" not in word) and ("상호" not in word) and ("방송" not in word) and ("객실" not in word) and
                ("참고" not in word) and ("연중" not in word) and ("출발" not in word) and ("사업" not in word) and ("번길" not in word) and ("갈비" not in word)and ("먼저" not in word) and ("아주" not in word) and ("아래" not in word) and ("사실" not in word) and ("다른" not in word) and ("오픈" not in word) and ("이상" not in word) and ("가면" not in word) and ("생활" not in word) and ("선정" not in word) and ("공사" not in word) and ("보기" not in word) and ("연락처" not in word) and ("구이" not in word) and ("이름" not in word) and ("일정" not in word) and ("남해" not in word) and ("포장" not in word) and ("마감" not in word) and ("이동" not in word) and ("번호" not in word) and ("방향" not in word) and ("중국" not in word) and ("그대로" not in word) and
                ("당일" not in word) and ("횟집" not in word) and ("자주" not in word) and ("번지" not in word) and ("조성" not in word) and ("기억" not in word) and ("대한민국" not in word) and ("인근" not in word) and ("시민" not in word) and ("예전" not in word) and ("그냥" not in word) and ("라면" not in word) and ("출구" not in word) and ("지정" not in word) and ("직접" not in word) and ("현재" not in word) and ("방법" not in word) and ("동안" not in word) and ("국가" not in word) and ("체크" not in word) and ("역시" not in word) and ("길이" not in word) and ("확인" not in word) and ("요금" not in word) and ("서포터즈" not in word) and ("휴가" not in word) and ("종합" not in word) and
                ("브레이크" not in word) and ("타임" not in word) and ("가성" not in word) and ("리뷰" not in word) and ("할인" not in word) and ("입실" not in word) and ("퇴실" not in word) and ("진행" not in word) and ("관련" not in word) and ("모임" not in word) and ("통해" not in word) and ("멀리" not in word) and ("여러분" not in word) and ("잠시" not in word) and ("화장실" not in word) and ("정상" not in word) and ("현대" not in word) and ("하늘" not in word) and ("밥집" not in word) and ("피자" not in word) and ("중심" not in word) and ("주택" not in word) and ("일상" not in word) and ("마루" not in word) and ("테이블" not in word) and ("김밥" not in word) and ("만들기" not in word) and
                ("화요일" not in word) and ("얼마" not in word) and ("아파트" not in word) and ("베트남" not in word) and ("사용" not in word) and ("마치" not in word) and ("경주" not in word) and ("국밥" not in word) and ("지원" not in word) and ("인테리어" not in word) and ("사회" not in word) and ("택시" not in word) and ("방역" not in word) and ("일본" not in word) and ("프로그램" not in word) and ("단지" not in word) and ("전주" not in word) and ("짬뽕" not in word) and ("업체" not in word) and ("미리" not in word) and ("정리" not in word) and ("전문점" not in word) and  ("간다" not in word) and ("스타" not in word) and  
                ("엄마" not in word) and ("영어" not in word) and ("성인" not in word) and ("매장" not in word) and ("관리" not in word) and ("랜선" not in word) and ("사장" not in word) and ("이웃" not in word) and ("지번" not in word) and ("숙박" not in word) and ("서비스" not in word) and ("오션" not in word) and ("하우스" not in word) and ("올해" not in word) and ("돼지" not in word) and ("본점" not in word) and ("기자" not in word) and ("만원" not in word) and ("월월" not in word) and ("두기" not in word) and ("지인" not in word) and ("오토" not in word) and ("천리" not in word) and ("가든" not in word) ) : 
                noun_list.append(word)
        tokenized_data.append(noun_list)
    s=" ".join(noun_list)
    matrix_231x2.iloc[num,1]=s
    num=num+1
    
matrix_231x2


# In[83]:


#지역별 명사 총합 길이 확인

length_list = list(range(0, 231))
for i in range(0,231):
    length_list[i]=len(matrix_231x2.iloc[i,1])
    


# In[94]:


np.mean(length_list)


# In[84]:


##barplot 테스트
import matplotlib.pyplot as plt
plt.figure(figsize=(20,10))
plt.bar(range(0,231),length_list)
plt.box(length_list)


# In[85]:


##boxplot 테스트
plt.boxplot(length_list)


# In[123]:


################
#사이킷런 안의 TF-IDF 벡터화 알고리즘을 이용한 키워드 탐색 max_features, min_df 값을 변경시켜가며 최적의 결과 탐색 해야함
################
from sklearn.feature_extraction.text import TfidfVectorizer

tfidfv = TfidfVectorizer(max_features=200,min_df=0.3,analyzer='word').fit(matrix_231x2.sentences)
X=tfidfv.transform(matrix_231x2.sentences)
print(tfidfv.vocabulary_) 


# In[124]:


tfidfv.vocabulary_.keys()


# In[125]:


#지역-키워드231*200 df생성
tfidf_dict = tfidfv.get_feature_names()
data_array = X.toarray()
tfidf_df=pd.DataFrame(data=data_array,columns=tfidf_dict)
tfidf_df['region']=matrix_231x2.region
tfidf_df


# In[138]:


print("서울종로구\n")
print(tfidf_df.iloc[0,:-1].sort_values(ascending=False).head(20))


# In[127]:


#걸러진 키워드들로 만들어진 matrix를 토대로 Kmeans cluster(군집화) 를 진행할시
#몇개의 군집이 가장 적절한지 판단하는
# elbow_기법 코드
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
def elbow(data1, length):
    sse = [] # sum of squre error 오차제곱합
    for i in range(1, length):
        kmeans = KMeans(n_clusters=i)
        kmeans.fit(data1)
        # SSE 값 저장
        sse.append(kmeans.inertia_)
    plt.plot(range(1, length), sse, 'bo-')
    plt.title("elbow method")
    plt.xlabel("number of clusters")
    plt.ylabel("SSE")
    plt.show()
elbow(X, 10)


# In[128]:


# K-means로 6개 군집으로 문서 군집화시키기
from sklearn.cluster import KMeans

kmeans = KMeans(n_clusters=6, max_iter=1000, random_state=101)
# 비지도 학습이니 feature로만 학습시키고 예측
cluster_label = kmeans.fit_predict(X)

# 군집화한 레이블값들을 df 에 추가하기
matrix_231x2['cluster_label'] = cluster_label
print(matrix_231x2.sort_values(by=['cluster_label']))


# In[129]:


matrix_231x2.cluster_label.value_counts()


# In[47]:


centers = kmeans.cluster_centers_
vocabs = [vocab for vocab, idx in sorted(tfidfv.vocabulary_.items(), key=lambda x:x[1])]


# In[48]:


from soyclustering import proportion_keywords
keywords = proportion_keywords(
    centers,
    labels=cluster_label,
    index2word=vocabs)


# In[49]:


for i in  [0,1,2,3,4,5]:
    print(keywords[i])
    print("\n")


# In[ ]:




