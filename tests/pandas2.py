import pandas as pd
import numpy as np

print(pd.__version__)
#
# df = pd.read_csv('test_data.csv')
# print(df)
# print()
# print(df['age'])
# print(df['age'][0])
# print((df['age'] == df['age'][0]).all())
#
# print(  df.iloc[2][0]  )
#
# print(  (df.iloc[6] == df.iloc[6][0] ).all()  )
#
# print(f"все значения в столбце 'cats' NaN: {df['cats'].isnull().all()}")

# print(df.isnull())
# print(df.isnull().sum())
# # print(df.isna())
# print(df['point'].isnull())
# print(df['point'].isnull().sum())
# print(df[df['point'].isnull()])

# поиск пустых значений для строки 2
# print(df.iloc[2])
# print(df.iloc[2].isnull())

# print(df.loc[:, df.iloc[2].isnull()])

# remove rows and columns where all values are NaN
# df2 = df.dropna(how='all').dropna(how='all', axis=1)

# удаляет строки в которых все значения NaN
# df2 = df.dropna(how='all')
# print()
# удаляет столбцы в которых все значения NaN
# df2 = df.dropna(how='all', axis='columns')
# print(df2)

df = pd.DataFrame(np.random.randn(10,5), columns=list('abcde'))
df.iloc[:4,0] = np.nan
df.iloc[:3,1] = np.nan
df.iloc[:2,2] = np.nan
df.iloc[:1,3] = np.nan

df.info(verbose = True, memory_usage=True, show_counts=True)
print(df)

def describe_nan(df):
    return pd.DataFrame([(i, df[df[i].isna()].shape[0],df[df[i].isna()].shape[0]/df.shape[0]) for i in df.columns], columns=['column', 'nan_counts', 'nan_rate'])

print(describe_nan(df))