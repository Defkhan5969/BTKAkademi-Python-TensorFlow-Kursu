import numpy as np
import pandas as pd

veri = {"Istanbul":[30,29,np.nan], "Ankara":[20,np.nan,25], "İzmir":[40,39,38]}
havaDurumuDataFrame = pd.DataFrame(veri,index=["Pazartesi","Salı","Çarşamba"])

result = havaDurumuDataFrame.dropna(axis=1) #Nan olan değerli sutün ve satırları siler.




yeniVeri = {"Istanbul":[30,29,np.nan], "Ankara":[20,np.nan,25], "Antalya":[45,np.nan,np.nan]}
yeniDataFrame = pd.DataFrame(yeniVeri)


result = yeniDataFrame.dropna(axis = 1,thresh=2) #thres sınır belirtir

result = yeniDataFrame.loc[1,"Istanbul"]


result =yeniDataFrame

# GROUPBY

maasSozlugu = {"Departmanlar":["Yazilim","Yazilim","Pazarlama","Pazarlama","Hukuk","Hukuk"],
"Çalişan İsmi":["Ahmet","Mehmet","Atil","Burak","Zeynep","Fatma"],
"Maas":[100,150,200,300,400,500]}

maasDataFrame = pd.DataFrame(maasSozlugu)

grupObjesi = maasDataFrame.groupby("Departmanlar")

result = grupObjesi.count()
result = grupObjesi.mean()
result = grupObjesi.max()
result = grupObjesi.min()
result = grupObjesi.describe()


print(result)