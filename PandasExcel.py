import pandas as pd

maasVerisi = pd.read_excel("Data.xlsx")
#csv formatında gelirse .read_csv yazarsın


result = maasVerisi.dropna(axis = 0)

result.to_excel("YeniData.xlsx")

print(result)

