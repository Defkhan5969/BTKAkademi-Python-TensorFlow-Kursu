from turtle import color
import numpy as np
import matplotlib.pyplot as plt

yas = [10,20,30,30,30,40,50,60,70,75]
kilo = [20,60,80,85,86,87,70,90,95,90]


numpyYas = np.array(yas)
numpyKilo = np.array(kilo)

# plt.plot(numpyYas,numpyKilo,"y")#x,y,renk

# plt.xlabel("Yas")
# plt.ylabel("Kilo")
# plt.title("Kilo'nun Yaşa Göre Değişim Grafiği")


result = numpyDizi = np.linspace(0,10,20)
result = numpyDizisi2 = numpyDizi**3

# plt.plot(numpyDizi,numpyDizisi2,"b--")

# plt.subplot(1,2,1)
# plt.plot(numpyDizi,numpyDizisi2,"r*-")
# plt.subplot(1,2,2) # 1 sıra olacak 2 kolon olacak 2. çiziyorum.
# plt.plot(numpyDizisi2,numpyDizi,"b--")


# myFigure = plt.figure() # Figür oluşturma-boş figür.
# figureAxes = myFigure.add_axes([0.07,0.07,0.8,0.8])

# figureAxes.set_xlabel("X Ekseni")
# figureAxes.set_ylabel("Y Ekseni")
# figureAxes.set_title("Grafik Başı")
# # figureAxes.plot(numpyDizi,numpyDizisi2,"g")

# figure2 = plt.figure()

# eksen1 = figure2.add_axes([0.1,0.1,0.3,0.9])#[Grafik nerede x,grafik nerede y,büyüklük x ,büyüklük y]
# eksen2 = figure2.add_axes([0.6,0.1,0.3,0.9])


# eksen1.set_xlabel("x")
# eksen1.set_ylabel("Y")
# eksen1.set_title("Ana Grafik")
# eksen1.plot(numpyDizi,numpyDizisi2,"g")

# eksen2.set_xlabel("x")
# eksen2.set_ylabel("Y")
# eksen2.set_title("Küçük Grafik")
# eksen2.plot(numpyDizisi2,numpyDizi,"b")

# myFigure,myAxes = plt.subplots(nrows=1,ncols=2) #Hem eksen hem değer
# for eksen in myAxes:
#     eksen.plot(numpyDizi,numpyDizisi2,"g")
#     eksen.set_xlabel("X Eksnei")
# print(myFigure)
# print(myAxes)

yeniFigur = plt.figure(dpi=200) # dpi kalite ve büyüklük 
yeniEksen = yeniFigur.add_axes([0.1,0.1,0.8,0.9])
yeniEksen.plot(numpyDizi,numpyDizi**2,label = "Numpy Dizisi ** 2")
yeniEksen.plot(numpyDizi,np.sqrt(numpyDizi),label = "Numpy Dizisi Kök")
yeniEksen.legend(loc=10) #Verinin etiketi gösterir. Ve Yerini

#yeniFigur.savefig("benimFigür.png",dpi=200) # DPİ ayarlama ve kaydetme
plt.show()