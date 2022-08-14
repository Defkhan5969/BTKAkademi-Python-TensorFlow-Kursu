from cgi import test
import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib.pyplot as plt

dataFrame = pd.read_excel("bisiklet_fiyatlari.xlsx")
# print(dataFrame.head())

# sbn.pairplot(dataFrame)

# plt.show(block=True)


##VERİYİ TEST/TRAİN OLARAK İKİYE AYIRMAK

from sklearn.model_selection import train_test_split

#train_test_split.
#y=wx+b
#y --label
y = result = dataFrame["Fiyat"].values

#x--feature(özellik)
x = dataFrame[["BisikletOzellik1","BisikletOzellik2"]].values

x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.33,random_state=15)

result = x_train
result = x_train.shape
result = y_train.shape

#SCALİNG--Boyut İşlemleri

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
scaler.fit(x_train)

result = x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(4,activation="relu"))
model.add(Dense(4,activation="relu"))
model.add(Dense(4,activation="relu"))

model.add(Dense(1))

model.compile(optimizer="rmsprop",loss="mse")
model.fit(x_train,y_train,epochs=250)

loss=model.history.history["loss"]
sbn.lineplot(x=range(len(loss)),y=loss)


trainLoss = model.evaluate(x_train,y_train,verbose=0)
testLoss = model.evaluate(x_train,y_train,verbose=0)


testTahminleri = model.predict(x_test)
print(testTahminleri)

tahminDf = pd.DataFrame(y_test,columns=["Gerçek Y"])
testTahminleri = pd.Series(testTahminleri.reshape(330,))

tahminDf = pd.concat([tahminDf,testTahminleri],axis=1)
tahminDf.columns = ["Gerçek Y","Tahmin Y"]

sbn.scatterplot(x="Gerçek Y",y="Tahmin Y",data=tahminDf)
plt.show(block=True)

from sklearn.metrics import mean_absolute_error,mean_squared_error

mean_absolute_error(tahminDf["Gerçek Y"],tahminDf["Tahmin Y"])
yeniBisikletOzellikleri = [[1760,1758]]
yeniBisikletOzellikleri = scaler.transform(yeniBisikletOzellikleri)
model.predict(yeniBisikletOzellikleri)

from keras.models import load_model
model.save("bisiklet_modeli.h5")

sonradanCagirilanModel = load_model("bisiklet_modeli.h5")
# print(result)