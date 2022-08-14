import string
import numpy as np

## Numpy ARRAY
benimListem = [20,30,40]
print(type(benimListem))

a = np.array(benimListem)
print(type(a))

matriksListesi = [[10,20,30],[20,30,40],[50,60,70]]
print(matriksListesi[1])
a = np.array(matriksListesi)
print(a)

#ARANGE METODU--ÖNEMLİ

print(list(range(0,10)))
print(np.arange(0,10))
print(np.arange(0,20,2))

#ZEROS Yöntemi

a = np.zeros((5,2))
a=np.zeros((9,9))
a= np.ones(5)
a = np.ones((9,9))



#LİNSPACE YÖNTEMİ--ÖNEMLİ

a = np.linspace(0,20,10)
a = np.linspace(1,10,100)

#EYE METHODU

a = np.eye(10)



#RANDOM METHODU- KENDİSİNİN VE ÖNEMLİ

a = np.random.randn(4)
a = np.random.randn(8,8)
a = np.random.randint(1,10)#Sonu almaz
a = np.random.randint(1,300,5) #sonuncu kaç tane olacağını alır

benimNumpyDizim= np.arange(30)
benimRandomDizim = np.random.randint(0,100,20)

print(benimNumpyDizim)
print(benimRandomDizim)

# Numpy Dizi Methodları

b = benimNumpyDizim.reshape(5,6)
a = benimNumpyDizim.reshape(6,5)
a = benimNumpyDizim.max()
a = benimRandomDizim.max()
a = benimRandomDizim.argmax()
a = b.shape
print(a)