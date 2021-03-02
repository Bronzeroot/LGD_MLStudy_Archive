import pandas as pd
import json

#path = '실제 파일 path'
with open(path, 'r', encoding='utf-8-sig') as json_file:
    json_data = json.load(json_file)
    print (json_data.keys())

doc0 = pd.read_csv('파일명0',encoding='utf-8-sig')
doc1 = pd.read_csv('파일명1', encoding='utf-8-sig') #cp949 encoding 사용 필요할 수 있음 

doc0 = doc0[['Year','Quarter','Gaming','Product Category','Region','Product','Brand','Units']]
doc1 = doc1[['Year','Quarter','Product Category','Vendor','Region','Units']]

def brand_name_convert(row):
    if row['Brand'] in json_data:
        row['Brand'] =json_data[row['Brand']]
    return row
  
doc0 = doc0.apply(brand_name_convert, axis=1)
doc0.rename(columns ={'Brand': 'Vendor'}, inplace = True)

doc0 = doc0[['Year','Quarter','Product Category','Vendor','Region','Units']]
doc2 = pd.concat([doc0,doc1])

#doc2.to_csv('결과파일이름.csv',index = False)
