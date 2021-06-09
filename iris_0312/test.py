import pandas as pd #판다스 임포트
#iris파일을 읽어 데이터프레임으로 변환
df = pd.read_csv('iris.csv')
print(df.head(3))
print(df.tail(3))

species = df['종류'].unique() #종류 열로부터 중복이 없는 데이터 추출(시리즈)
print(species)
species_count = df['종류'].value_counts() #데이터 출현 횟수 카운트
print(species_count)

print(df.isnull()) # 결손값 유무를 확인

print(df.isnull().any(axis=0))  #열단위 결손값 확인 True가 문제가 있다는것

print(df.sum()) #각 열의 합계 값을 계산