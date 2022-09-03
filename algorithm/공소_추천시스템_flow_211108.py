#!/usr/bin/env python
# coding: utf-8

# In[18]:


import pandas as pd
import numpy as np

#데이터 DB에서 받아올 부분(수정필요)
matrix_231x201=pd.read_csv("matrix_231x201_211108.csv", encoding="utf-8")
matrix_231x201


# In[19]:


#화면1
##사용자가 지역명(input)입력하면 input_region으로 받아올 부분(수정필요)
input_region=input("지역명입력:")


# In[40]:


matrix_231x201[matrix_231x201.region==input_region]


# In[44]:


#해당지역의 matrix_231x200 행렬 내 index 번호
matrix_231x201[matrix_231x201.region==input_region].index[0]


# In[52]:


#해당 지역의 키워드 계수값 기준으로 정렬해주는 작업
select_reg_sorted_T=matrix_231x201[matrix_231x201.region==input_region].T.iloc[range(0,200),:].sort_values(by=[matrix_231x201[matrix_231x201.region==input_region].index[0]],ascending=False)


# In[53]:


select_reg_sorted_T


# In[67]:


#t지역을 선택한 사용자에게 시각적으로 키워드를 제공할 화면2에서 사용할 해당지역 top10 키워드 리스트(추천시스템 내 output 1)
select_reg_sorted_T.head(10).index


# # 1: input(사용자)to output(어플)

# In[90]:


import pandas as pd
import numpy as np

#!!!!!!!!!!!!데이터  몽고DB에서 받아올 부분(수정필요)
matrix_231x201=pd.read_csv("matrix_231x201_211108.csv", encoding="utf-8")

##!!!!!!!!!!사용자가 지역명(input)입력하면 input_region으로 받아올 부분(수정필요)
input_region=input("지역명입력:")

select_reg_sorted_T=matrix_231x201[matrix_231x201.region==input_region].T.iloc[range(0,200),:].sort_values(by=[matrix_231x201[matrix_231x201.region==input_region].index[0]],ascending=False)
select_reg_sorted=select_reg_sorted_T.T
#output==top10keywords(list)
top10keywords=select_reg_sorted_T.head(10).index
print("returning output1 is succesful\n")


# In[91]:


#1차 아웃풋 확인
top10keywords


# In[ ]:





# In[ ]:





# In[83]:


#사용자의 최소-최대 선택 단어는 몇개로 할 것인지..?


# In[84]:


#최소 1개, 최대 5개라고 가정하고 진행


# In[125]:


#사용자가 선택한 키워드명을 리스트의 형태 ['','', ...]로 받아온다 가정.
# example of selected_keywords
selected_keywords=['비치', '바다', '동해', '해변']


# In[126]:


#선택한 키워드 개수에 따라 각 단어의 가중치(weight) 리스트 weights 를 만들어주는 작업
denom=0

for keyword in selected_keywords:
    denom=denom + select_reg_sorted[keyword].values

weights=[]
for i in range(0,len(selected_keywords)):
    weights.append((select_reg_sorted[selected_keywords[i]].values/denom)[0])
weights


# In[146]:


#각 231 지역의 사용자 선택 키워드에다 가중치작업을 해주었을때의 결과 
matrix_231x201[selected_keywords]*weights


# In[148]:


#matrix_231x201 에 score 변수를 추가하여 추천 점수 부여
matrix_231x201['score']=(matrix_231x201[selected_keywords]*weights).sum(axis=1)
matrix_231x201


# In[151]:


#일단 top 5개의 지역 선별
matrix_231x201.sort_values(by='score',ascending=False).head(5)


# In[152]:


#내림차순 정렬된 5개의 추천 지역명 반환
matrix_231x201.sort_values(by='score',ascending=False).head(5).region.values


# # 2: input(사용자) to output(어플)

# In[155]:


# example of selected_keywords
selected_keywords=['비치', '바다', '동해', '해변']

denom=0

for keyword in selected_keywords:
    denom=denom + select_reg_sorted[keyword].values

weights=[]
for i in range(0,len(selected_keywords)):
    weights.append((select_reg_sorted[selected_keywords[i]].values/denom)[0])
    
matrix_231x201['score']=(matrix_231x201[selected_keywords]*weights).sum(axis=1)

recomm_top5=matrix_231x201.sort_values(by='score',ascending=False).head(5).region.values
print('region recommandation is successful')
print(recomm_top5)


# In[ ]:




