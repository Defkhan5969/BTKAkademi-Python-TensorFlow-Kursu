def toplama(numara1,numara2):
    return numara1 + numara2

# x = int(input("İlk numarayı giriniz: 10"))
# y = int(input("İkinci numarayı giriniz: "))
# print(toplama(x,y))
#Str girerese ne olacak?

#try & except &else finallay

while True:
    try:
        benimInt= int(input("Numaranızı Giriniz: "))
    except:
        print("Lütfen gerçekten numara giriniz")
        continue
    else:
        print("Teşekkürler")
        break
    finally:
        print("Finally Geldi")