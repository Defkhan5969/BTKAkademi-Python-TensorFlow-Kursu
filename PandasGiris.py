from asyncio import as_completed
import pandas as pd
import numpy as np

##SERIES/SERİLER
#Sözlükten seri
benimSozluğum = {"Atil" : 50, "Zeynep": 40, "Mehmet": 34}
result = pd.Series(benimSozluğum)

#Listelerden seri
benimYaslarım = [50,40,30]
benimİsimlerim = ["Atil","Zeynep","Mehmet"]
result = pd.Series(index=benimİsimlerim,data=benimYaslarım)

#Numpy dizisinden seri
numpyDizisi = np.array([50,40,30])
result = pd.Series(numpyDizisi)

result = pd.Series(["Atil","Atlas","Osman"],index=[1,2,3])

result = yarismaSonucu1 = pd.Series([10,5,1],["Atil","Atlas","Osman"])
result = yarismaSonucu2 = pd.Series([20,10,8],["Atil","Atlas","Osman"])
result = yarismaSonucu2["Atlas"]
result = yarismaSonucu1+ yarismaSonucu2



farkliSeries = pd.Series([20,30,40,50],["a","b","c","d"])
farkliSeries2 = pd.Series([10,5,3,1],["a","c","f","g"])
result = farkliSeries +farkliSeries2



print(result)
