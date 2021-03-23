import pandas as pd

#1. 00_data/olist_customers_dataset.csv 파일 pandas dataframe 으로 읽어오기 (데이터프레임 변수 이름은 doc 로 하기로 함)
doc = pd.read_csv('00_data/olist_customers_dataset.csv', encoding='utf-8-sig')
doc.head()

#전체 record 수(행 수) 확인하기
doc.shape

#전체 열의 수 확인하기
doc.info()
#인덱스 확인하기
doc.index
doc.describe()


#데이터프레임 중 일부를 선택 후, 조작하면 해당 데이터프레임도 변경
#copy() 를 통해, 복사본을 만들어서 조작하여, 원본 데이터프레임은 보존 가능
doc2 = doc[['customer_zip_code_prefix','customer_city','customer_state']].copy()
doc2.head()

#customer_city 가 sao paulo 인 레코드(행)만 가져오기 (데이터프레임 변수 이름은 doc3 으로 하기로 함) 레코드(행) 수 확인도 해보기 
doc3=doc[doc['customer_city']=='sao paulo'].copy()
doc3.shape

#customer_city 기준으로 행의 갯수를 확인해보세요  doc2에 value_counts() 를 써보세요 (value_counts() 는 Series 에만 적용 가능합니다.) 
doc2['customer_city'].value_counts()

#1. groupby 를 써서 customer_city 를 기준으로 행의 갯수를 count 하세요 (새로운 데이터프레임 변수 이름은 doc4로 하기로 함)
#2. doc4를 통해 customer_city 수도 확인해보세요 (데이터프레임 레코드(행) 수를 확인해보면 됩니다.)
doc4 = doc.groupby(['customer_city']).count()
doc4.shape

#doc4에서 가장 레코드(행)의 수가 많은 customer_city 를 확인해보세요  doc4의 customer_id 를 기준으로 정렬하고, 가장 상단의 한 행만 출력하기
doc4.sort_values(by='customer_id', ascending=False).head(1)
#doc4['customer_id'].sort_values(ascending=False).head(1)


# doc 에서 customer_city 를 인덱스로 만들고, 알파벳 순으로 인덱스를 정렬해보세요
doc.set_index('customer_city').sort_index()

# doc2에서 customer_state 기준으로 행의 갯수를 확인해보세요 / doc2에 value_counts() 를 써보세요 (value_counts() 는 Series 에만 적용 가능합니다.) 
doc2['customer_state'].value_counts()

#doc2에서 customer_state 갯수를 확인해보세요 
len(doc2['customer_state'].unique()) 

