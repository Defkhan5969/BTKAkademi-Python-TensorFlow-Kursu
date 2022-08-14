from mimetypes import init


benimListem= list()
print(type(benimListem))

## instant & attributte// örnek ve özellik

class SuperKahraman():
    #sınıfların ilk harfi büyük olacak
    #Değişkenler Camel Case
    #Yapıcı Method
    ozelGuc = "Gorunmezlik"

    
    def __init__(self,isim,yas,meslek):
        print("İnit Çağrıldı")
        self.isim=isim
        self.yas = yas
        self.meslek=meslek

    def ornekMethod(self):
        print(f"Ben bir süper kahramanım ve mesleğim: {self.meslek}")

superman = SuperKahraman("Superman",30,"Gazeteci")
superman.isim = "Clark Kent"
print(superman.isim)
superman.ornekMethod()

class Kopek():
    yilÇarpani = 7
    def __init__(self,yas=8):
        self.yas=yas
    def insanYasiHesapla(self):
        print(f"İnsan Yaşı: {self.yas*Kopek.yilÇarpani}")

benimKopek = Kopek(3)
print(benimKopek.yas)
benimKopek.insanYasiHesapla()

#İnheritance

class Hayvan():
    def __init__(self) -> None:
        print("Hayvan sınıfı init çağrıldı")
    def method1(self):
        print("Hayvan sınıfı method 1 ")
    def method2(self):
        print("Hayvan sınıfı method 2 çağrıldı")

benimHayvanım = Hayvan()
benimHayvanım.method1()
benimHayvanım.method2()

class Kedi(Hayvan):
    def __init__(self) -> None:
        super().__init__()
        print("Kedi Sınıfı init çağrıldı")
    def miyavla(self):
        print("MİYAV")
        #OVERRIDE
    def method1(self):
        print("Kedi Sınıfındaki method 1 çağırıldı")

benimKedim = Kedi()
benimKedim.method1()
benimKedim.miyavla()

#Polymorphism

class Elma():
    def __init__(self,isim) -> None:
        self.isim = isim
    def bilgiVer(self):
        return self.isim + ": 100 Kalori"

class Muz():
    def __init__(self,isim) -> None:
        self.isim=isim
    def bilgiVer(self):
        return self.isim  + ": 150 Kalori"
elma = Elma("elma")
muz = Muz("muz")

meyveListesi = [elma,muz]
for meyve in meyveListesi:
    print(meyve.bilgiVer())

def bilgiAl(meyve):
    print(meyve.bilgiVer())
bilgiAl(muz)