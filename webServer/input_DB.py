import pandas as pd

data = pd.read_csv("./2021-2-OSSP2-Coconut-1/algorithm/matrix_231x201.csv")

for row in range(len(data)):
    
    for col in range(len(data.iloc[0])-2):
        len(data.iloc[row])
print(data.iloc[0,1])