import numpy as np 
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sbn

result = dataFrame = pd.read_excel("maliciousornot.xlsx")
result = dataFrame.info() #Nonnull vs bakabiliriz.
result = dataFrame.describe()
result = dataFrame.corr()["Type"].sort_values() #Tipe göre diğer özelliklerin değişimleri

# sbn.countplot(x="Type",data=dataFrame)#0 ve 1 oranları
y = dataFrame["Type"].values
x=dataFrame.drop("Type",axis=1).values

from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.30,random_state=15)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler()
scaler.fit(x_train)
x_train = scaler.transform(x_train)
x_test = scaler.transform(x_test)

import tensorflow as tf
from keras.models import Sequential
from keras.layers import Dense,Activation,Dropout
from keras.callbacks import EarlyStopping

result = x_train.shape

# model = Sequential()
# model.add(Dense(units=30,activation="relu"))
# model.add(Dense(units=15,activation="relu"))
# model.add(Dense(units=15,activation="relu"))
# model.add(Dense(units=1,activation="sigmoid"))

# model.add(Dense(1))

# model.compile(loss="binary_crossentropy",optimizer="adam")
# model.fit(x=x_train,y=y_train,epochs=700,
# validation_data=(x_test,y_test),verbose=1)

# model.history.history

# modelKaybi = pd.DataFrame(model.history.history)
# modelKaybi.plot()



model = Sequential()
model.add(Dense(units=30,activation="relu"))
model.add(Dense(units=15,activation="relu"))
model.add(Dense(units=15,activation="relu"))
model.add(Dense(units=1,activation="sigmoid"))

model.add(Dense(1))

model.compile(loss="binary_crossentropy",optimizer="adam")

earlyStopping = EarlyStopping(monitor="val_loss",mode="min",verbose=1,patience=25)

model.fit(x=x_train,y=y_train,epochs=700,validation_data=(x_test,y_test),verbose=1,callbacks=[earlyStopping])

modelKaybi = pd.DataFrame(model.history.history)
modelKaybi.plot()



plt.show(block=True)
print(result)
