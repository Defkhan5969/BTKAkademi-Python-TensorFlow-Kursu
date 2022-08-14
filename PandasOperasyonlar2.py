import numpy as np
import pandas as pd


sozluk1 = {"İsim":["Ahmet","Mehmet","Zeynep","Atil"],
"Spor":["Koşu","Yüzme","Koşu","Basketbol"],
"Kalori":[100,200,300,400]}

dataFrame1= pd.DataFrame(sozluk1,index=[0,1,2,3])

sozluk2 = {"İsim":["Osman","Levent","Atlas","Fatma"],
"Spor":["Koşu","Yüzme","Koşu","Basketbol"],
"Kalori":[200,150,400,500]}

dataFrame2= pd.DataFrame(sozluk2,index=[4,5,6,7])

sozluk3 = {"İsim":["Ayse","Mahmut","Duygu","Nur"],
"Spor":["Koşu","Yüzme","Badminton","Basketbol"],
"Kalori":[200,600,400,500]}

dataFrame3= pd.DataFrame(sozluk3,index=[8,9,10,11])

#CONCATENATION

result = pd.concat([dataFrame1,dataFrame2,dataFrame3])

#MERGING

mergeSozluk1 = {"Isim": ["Ahmet","Zeynep","Mehmet","Atil"],
"Spor":["Koşu","Yüzme","Koşu","Basketbol"]}

mergeDataFrame1 = pd.DataFrame(mergeSozluk1)

mergeSozluk2 = {"Isim": ["Ahmet","Zeynep","Mehmet","Atil"],
"Kalori":[100,200,300,400]}

mergeDataFrame2 = pd.DataFrame(mergeSozluk2)

result = pd.merge(mergeDataFrame1,mergeDataFrame2,on="Isim") #Liste Yok DİKKAT!!

maasSozluk = {"Isim":["Atil","Zeynep","Mehmet","Ahmet"],
"Departman":["Yazilim","Satis","Pazarlama","Yazilim"],
"Maas":[200,300,400,500]}

def bruttenNete(Maas):
   return Maas*0.66

maasDataFrame = pd.DataFrame(maasSozluk)
result = maasDataFrame
result = maasDataFrame["Departman"].unique() #Benzersiz olanlar gelir
result = maasDataFrame["Departman"].nunique()#Ne kadar
result = maasDataFrame["Departman"].value_counts() #Hangi Departman Kaç Tane
result = maasDataFrame["Maas"].apply(bruttenNete)#Fonksiyonu uygulayacak
result = maasDataFrame[maasDataFrame.isnull()] # nan var mı?


yeniBirVeri = {"Karakter Sınıfı":["South Park","South Park","Simpson","Simpson","Simpson"],
"Karakter İsmi":["Cartman","Kenny","Homer","Bart","Bart"],
"Karakter Yas":[9,10,50,20,10]}


karakterDF = pd.DataFrame(yeniBirVeri)
result = karakterDF.pivot_table(values="Karakter Yas",index=["Karakter Sınıfı","Karakter İsmi"],aggfunc=np.sum)

print(result)

