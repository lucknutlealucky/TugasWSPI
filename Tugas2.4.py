import Tugas21m
import matplotlib.pyplot as plt
import numpy as np

Berat = [0.3,0.3,0.25,0.15]
juge = []
data = [["Riky",80,76,80,80],["david",45,80,80,80],["isac",45,80,65,80],["rio",80,80,70,80],["maven",80,77,80,96],["devi",75,80,80,92],["Anggel",78,79,79,79],["Steven",69,72,68,48]]


print ("No.\t|Nama Mhs\t|N.Tgs\t|N.Kuis\t|N.UTS\t|N.UAS\t|NilaiAkhir\t|NilaiHuruf")
print("-------------------------------------------------------------------")
for i in range(len(data)) :
    nilaiAkhir = (data[i][1]*Berat[0])+(data[i][2]*Berat[1])+(data[i][3]*Berat[2])+(data[i][4]*Berat[3])
    juge.append(Tugas21m.ukurNilai(nilaiAkhir))
    print(str(i) + ".\t|" +str(data [i][0])+ "\t\t|" + str(data [i][1]) +"\t|" + str(data [i][2]) +"\t|" + str(data [i][3]) +"\t|" + str(data [i][4]) +"\t|" + str(int(nilaiAkhir))+"\t\t|" + str(juge[i]))
y = np.array(juge)
print (y)
plt.hist(y)
plt.show()
