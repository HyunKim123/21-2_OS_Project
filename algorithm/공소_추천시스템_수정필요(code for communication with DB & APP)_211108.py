import pandas as pd
import numpy as np

############################데이터 DB에서 받아올 부분(수정필요)
#mongodb feature data에서 데이터프레임으로 변환
matrix_231x201=pd.read_csv("2021-2-OSSP2-Coconut-1/algorithm/matrix_231x201_211108.csv", encoding="utf-8")

#############################사용자가 지역명(input)입력하면 input_region으로 받아올 부분(수정필요)
input_region=input("지역명입력:")

select_reg_sorted_T=matrix_231x201[matrix_231x201.region==input_region].T.iloc[range(0,200),:].sort_values(by=[matrix_231x201[matrix_231x201.region==input_region].index[0]],ascending=False)
select_reg_sorted=select_reg_sorted_T.T
#output==top10keywords(list)
top10keywords=select_reg_sorted_T.head(10).index
print(list(top10keywords))

#############################
##!!!!!!!APP으로 top10keywords 보내는 코드 들어갈자라
#############################



#############################APP에서 받아오는 식으로 수정필요
# 사용자 선택 키워드 예시
selected_keywords=['비치', '바다', '동해', '해변']

denom=0

for keyword in selected_keywords:
    denom=denom + select_reg_sorted[keyword].values

weights=[]
for i in range(0,len(selected_keywords)):
    weights.append((select_reg_sorted[selected_keywords[i]].values/denom)[0])
    
matrix_231x201['score']=(matrix_231x201[selected_keywords]*weights).sum(axis=1)

recomm_top5=matrix_231x201.sort_values(by='score',ascending=False).head(5).region.values
#############################
##!!!!!!!APP으로 recomm_top5 보내는 코드 들어갈자리
#############################
