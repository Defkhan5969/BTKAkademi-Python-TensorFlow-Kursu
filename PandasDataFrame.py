from matplotlib.pyplot import axes, axis
from mysqlx import Row
import numpy as np
import pandas as pd

data = np.random.randn(4,3)
dataFrame = pd.DataFrame(data) #Pandas serilerinin bir araya gelmesi
yeniDataFrame = pd.DataFrame(data,index=["Atil","Zeynep","Atlas","Mehmet"],columns=["Maas","Yas","Calisma Saati"])


result = yeniDataFrame["Yas"]
result = yeniDataFrame["Calisma Saati"]
result = yeniDataFrame[["Maas","Yas"]]
result = yeniDataFrame.loc["Atil"]
result = yeniDataFrame.loc["Zeynep"]
result = yeniDataFrame.iloc[1] #İndex bazlı gidiş

yeniDataFrame["EmeklilikYasi"] = yeniDataFrame["Yas"]+ yeniDataFrame["Yas"]

yeniDataFrame.drop(columns="EmeklilikYasi",inplace=True)
yeniDataFrame.drop("Mehmet",axis=0,inplace = True)

result = yeniDataFrame.loc["Atlas","Yas"]

result = yeniDataFrame[yeniDataFrame<0]

result = yeniDataFrame[yeniDataFrame["Calisma Saati"]<0]



result = yeniDataFrame.reset_index()
yeniIndexListesi = ["Ati","Zey","Atl"]

yeniDataFrame["Yeni İndeks"] = yeniIndexListesi
result = yeniDataFrame.set_index("Yeni İndeks",inplace=True)
result = yeniDataFrame.loc["Ati"]

result = yeniDataFrame
ilkIndeksler = ["Simpson","Simpson","Simpson","South Park","South Park","South Park"]
içIndeksler = ["Homer","Bart","Curde","Cartman","Kenny","Kyle"]


birlesmisIndeks = list(zip(ilkIndeksler,içIndeksler)) # Zip sözlük oluşturdu
result = birlesmisIndeks


birlesmisIndeks = pd.MultiIndex.from_tuples(birlesmisIndeks)
result = birlesmisIndeks

benimCizgiFilmListe = [[40,"A"],[30,"B"],[10,"C"],[50,"D"],[45,"E"],[11,"F"]]
cizgiFilmNumpyDizisi = np.array(benimCizgiFilmListe)

cizgiFilmDataFrame = pd.DataFrame(cizgiFilmNumpyDizisi,index=birlesmisIndeks,columns=["Yas","Meslek"])



result = cizgiFilmDataFrame.loc["Simpson"]
result = cizgiFilmDataFrame.loc["South Park"]
result = cizgiFilmDataFrame.loc["South Park"].loc["Kenny"]

cizgiFilmDataFrame.index.names = ["Film Adı","İsim"]
result = cizgiFilmDataFrame
print(result)
#print(yeniDataFrame)