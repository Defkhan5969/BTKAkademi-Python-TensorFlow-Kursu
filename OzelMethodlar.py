class Meyve():
    def __init__(self,isim,kalori) -> None:
        self.isim = isim
        self.kalori = kalori
    def __str__(self) -> str:
        #Yazdırırisek ne döndürelim.
        return f"{self.isim} şu kadar kaloriye sahiptir: {self.kalori}"
    def __len__(self):
        return self.kalori
muz = Meyve("Muz",150)
print(muz.kalori)

print(muz)

benimListem= [1,2,3,4,'a',5,6.5]
print(benimListem)
print(len(benimListem))
print(len(muz))

elma = Meyve("Elma",200)
print(len(elma))