import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('C:/Users/Administrator/Downloads/movies-train.csv', encoding = 'cp949') #디렉토리를 찾아가기
df1 = pd.read_csv('movies-train.csv', encoding = 'cp949') #동일 Directory에 있으면 간편하게

df1.head() #default는 5개만 가져옴
df1.tail() #default는 5개만 가져옴
df1.tail(10) #숫자를 채워서 지정 가능 

df1.columns #칼럼확인
df1.shape #Data 모양 확인
df1.info()#칼럼별 Info
df1.describe() #숫자 Data 통계

df1['상영등급'].describe() # Case 1 Object 생성 없이 바로 확인
rating = df1['상영등급'] #Case 2 특정 칼럼을 별도의 Data Frame으로
rating.describe() 
rating.value_counts()

df1.isnull().sum() #null값이 들어있는 것을 더해서 보여줌
df2 = df1.dropna() #null 값을 모두 삭제
df2.shape #312개의 Data가 Drop됨
df2 =df1.fillna(1000) #null 값을 모두 1000으로 지정해줌(칼럼 구분없이)
df2['이전평균관객'] #결과 확인

df3 = df2[['관객수','주연','스텝','제작참여영화','상영시간(분)']] #필요한 칼럼만 선택하여 새로운 Data Frame으로
df3.head() #Data확인
df3.columns
df3.columns=['Attendance','MainActor','Steps','M','RunTime'] #칼럼 이름 바꿔주기
df3.head()
df3.corr() #상관관계 
plt.figure(figsize=(6,6))
sns.heatmap(data = df3.corr(), annot=True, fmt = '.2f', linewidths=0.5, cmap='Greens') #시각화
