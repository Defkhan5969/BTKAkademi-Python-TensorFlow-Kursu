import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sbn

result = dataFrame = pd.read_excel("merc.xlsx")
# print(dataFrame.head(10))
result = dataFrame.describe() # Veriyi genel olarak inceliyoruz
"""
null veri var mı diye bir bakmak lazım. Sileriz ya da işleriz.

""" 

result = dataFrame.isnull().sum() #null var mı diye kontrol ettik sum ile toplama baktık.


# sbn.displot(dataFrame["price"])
# sbn.countplot(dataFrame["year"]) #Yıllara göre dağılımını çizdirdik
# sbn.scatterplot(x="mileage",y="price",data = dataFrame)
result = dataFrame.corr()["price"].sort_values()
result = dataFrame.sort_values("price",ascending=False).head(20)#Çoktan aza
result = dataFrame.sort_values("price",ascending=True).head(20)#Azdan çoka
result = len(dataFrame)
result = len(dataFrame)*0.01 #En pahalı arabaları listeden çıkarmak gerek.

result = yuzdeDoksanDokuzDataFrame = dataFrame.sort_values("price",ascending=False).iloc[131:] # En yüksek fiyatlılar geldi.
result = yuzdeDoksanDokuzDataFrame.describe()

# sbn.displot(yuzdeDoksanDokuzDataFrame["price"]) #Artık fiyatlar çok dağılmıyor.
result = dataFrame.groupby("year").mean()["price"]
result = yuzdeDoksanDokuzDataFrame.groupby("year").mean()["price"]
result = dataFrame[dataFrame.year !=1970].groupby("year").mean()["price"]

#1970 yılındaki gereksiz veriyi attık
dataFrame = yuzdeDoksanDokuzDataFrame
result = dataFrame.describe()
dataFrame = dataFrame[dataFrame.year !=1970]
result = dataFrame.groupby("year").mean()["price"]
dataFrame = dataFrame.drop("transmission",axis=1)
result = dataFrame

#EĞİTİME BAŞLADIK
y = dataFrame["price"].values #Sonucum
x = dataFrame.drop("price",axis=1).values#Diğer tüm değerler #Values dizi yapmak için

#X ve Y dizilerini test ve eitim dizisi olarak ayırıyoruz
from sklearn.model_selection import train_test_split

x_train ,x_test, y_train, y_test = train_test_split(x,y,test_size=0.30,random_state=15)#Yüzde 30' olarak ayırdık
result = len(x_train)
result = len(x_test)

#boyutlarını ayarlamamız gerekiyor
#Ulaşmak istenen yer boyulanduruluyor diğer değerleri değil
from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
x_train = scaler.fit_transform(x_train)
x_test  = scaler.fit_transform(x_test)

#İşleme başlıyor

from keras.models import Sequential
from keras.layers import Dense
result = x_train.shape

#Model oluştu
model = Sequential()
#Model katmanları oluştu
model.add(Dense(12,activation="relu"))#Norön
model.add(Dense(12,activation="relu"))#Norön
model.add(Dense(12,activation="relu"))#Norön
model.add(Dense(12,activation="relu"))#Norön
#Çıkış katmanı
model.add(Dense(1))

model.compile(optimizer="adam",loss="mse")

model.fit(x=x_train,y=y_train,
validation_data = (x_test,y_test),batch_size=250,epochs=300)

from sklearn.metrics import mean_absolute_error,mean_squared_error

tahminDizisi = model.predict(x_test)
result = mean_absolute_error(y_test,tahminDizisi)

plt.scatter(y_test,tahminDizisi)
plt.plot(y_test,y_test,"g-")

yeniArabaSeries = dataFrame.drop("price",axis=1).iloc[2]
yeniArabaSeries = scaler.transform(yeniArabaSeries.values.reshape(-1,5))
result = model.predict(yeniArabaSeries)

plt.show(block=True)
print(result)


