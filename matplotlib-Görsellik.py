import numpy as np
import matplotlib.pyplot as plt

numpyDizisi1 = np.linspace(0,10,20)
numpyDizisi2 = numpyDizisi1**2

# (benimFigur,benimEksen) = plt.subplots()
# benimEksen.plot(numpyDizisi1,numpyDizisi2,"g",color="#3333FF",alpha = 0.3)
# benimEksen.plot(numpyDizisi2,numpyDizisi1,"b")

# yeniFigür , yeniEksen = plt.subplots()
# yeniEksen.plot(numpyDizisi1,numpyDizisi1+2,color="blue",linewidth=2.)
# yeniEksen.plot(numpyDizisi1,numpyDizisi1+3,color="yellow",linewidth=2,linestyle=":")
# yeniEksen.plot(numpyDizisi1,numpyDizisi1+4,color="brown",linewidth=2.0,linestyle="-.")
# yeniEksen.plot(numpyDizisi1,numpyDizisi1+5,color="#0000",linestyle="--",marker="o",markerfacecolor="red")

#SCATTER PLOT

# plt.scatter(numpyDizisi1,numpyDizisi2,color="red")

#HİSTOGRAM:
yeniDizi = np.random.randint(0,100,50)

# plt.hist(yeniDizi)

#BOXPLOT

plt.boxplot(yeniDizi)

plt.show()