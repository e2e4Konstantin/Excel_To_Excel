import pandas
import numpy

f = r"C:\Users\kazak.ke\Documents\temp\template_3_68.xlsx"
sheet = "name"
df = pandas.read_excel(io=f, sheet_name=sheet, header=None, dtype="object", nrows=1000, skiprows=13 )
# print(df)
print(df.info(verbose=False, memory_usage=True, show_counts=True))
print(df.head(5))
# print(df.tail(5))
# print(df.shape)
# print(df.index)
# print(df.columns)


m = df.memory_usage(index=True, deep=True).sum()
print(f"память: {m/(1024*1024):_.2f} MB")
print()

cols = [0, 1, 2, 3, 4, 5]
df.drop(df.columns[cols], axis=1, inplace=True)
ab = list(map(chr, range(ord('A'), ord('Z')+1)))
ab.extend([ab[0]+x for x in ab])
# print(len(ab), ab)
print(df.shape)
df.columns = ab[:df.shape[1]]

print(df.info(verbose=False, memory_usage=True, show_counts=True))
print(df.head(5))

# print(df.iloc[0:5, 0:3])
# print(df.iloc[0:5, [0, 1, 3]])
# print(df[df.D > 0].iloc[0:5, [0, 1, 3]])
# print(df[df.D > 0].loc[7:9, ["A", "B", "D"]])
# print(df[df.D > 0].loc[0:15, ["A", "B", "D"]])
print(df[df.D > 0].loc[:, ["A", "B", "D"]].head(7))
print(df["A"].head(7))
print(df.A.head(7))
# print(df.describe())
print(len(df["A"].unique()))

myfilter = lambda x: x['D'] > 1000


print(df[ myfilter].loc[:, ["A", "B", "D"]])




#
# col = df.iloc[:, 56]
# print(f"строк: {len(col)}")
# print(f"пустых значений: {col.isnull().sum() = }")
#
# print(df.iloc[:, 56])
#
# print(f"-->> {col.isna().all() = }")
# print(f"-->> {col.isnull().all() = }")
# print()
# print(f"-->> {col[col.notna()] = }")
#
# c3 = df.iloc[:, 56]
# # print(f"-->>df.iloc[:, 0]: {c3}")
# print(c3)
# print(f"-->> {c3[c3.notna()] = }")
# print(c3.isnull().values.any())
#
# # print(f"-->> {df.iloc[0] = }")
# # df.loc[quotes.df["table"] == table_cod]
# #
#
#
# # for i, value in enumerate(df.iloc[:, 56]):
# #     isNaN = numpy.isnan(value)
# #     print(i, isNaN, value, type(isNaN))
