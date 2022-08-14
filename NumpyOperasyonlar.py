import numpy as np

a = benimDizim = np.arange(0,15)
a = benimDizim[5]
a = benimDizim[3:5]#son alınmaz
a = benimDizim[3:8]
benimDizim[3:8] = -5

#dizinin parçası değişirse kendisi de değişir. 
a = baskaDizi = np.arange(0,24)
a = baskaDizi[4:9]
a[:] = 500

print(baskaDizi)

ornekDizi = np.arange(0,24)
copiedDizi = ornekDizi.copy()

ornekDiziSlicing = ornekDizi[1:3]
ornekDiziSlicing[:] = 800
print(ornekDiziSlicing)
print(ornekDizi)
print(copiedDizi)

#MATRİKS İNDEKSLEME
benimListem = [[10,20,30],[40,50,60],[70,80,90]]
ornekMatrixDizisi = np.array(benimListem)
a = ornekMatrixDizisi[0]
a = ornekMatrixDizisi[1][2]
a = ornekMatrixDizisi[1,2]
a = ornekMatrixDizisi[1:,2]
a = ornekMatrixDizisi[2:,0]
a = ornekMatrixDizisi[2:,0:]

print(ornekMatrixDizisi)



matris = np.arange(0,25).reshape(5,5)
a = matris[2]
a = matris[[0,2,4]] # Fancy İndex

print(matris)
print(a)

#OPERASYONLAR

a = yeniBirDizi = np.random.randint(1,100,20)
a = yeniBirDizi >24
a = yeniBirDizi[a]
a = yeniBirDizi[yeniBirDizi>24]

sonDizi = np.arange(0,24)
a = sonDizi+sonDizi
a = sonDizi*sonDizi
a = sonDizi/sonDizi
a = sonDizi-sonDizi

a = np.sqrt(sonDizi)

a= np.max(sonDizi)
a = np.min(sonDizi)
print(a)