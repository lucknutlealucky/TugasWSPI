import Tugas22m
i = 0
nama=[]

while True :
    namax=[]
    namax.append(str(input("Nama Barang: ")))
    namax.append(int(input("Harga : ")))
    namax.append(int(input("Jumlah: ")))
    namax.append(namax[1]*namax[2])
    print ("Sub Tot Harga :" + str(namax[3]))
    lan = str(input("lanjut ? y atau n ? : "))
    nama.append(namax)
    if lan in ['y', 'Y', 'yes', 'Yes', 'YES'] :
        i= i+1
    else :
        break
        

print ("Nama Barang\t\t|Jumlah\t|Harga\t")
print("-------------------------------------------------------------------")
for i in range(len(nama)):
    print(str(nama[i][0])+"\t\t|"+str(nama[i][1])+"\t|"+str(nama[i][3]))
print("-------------------------------------------------------------------")
print("Total Harga :"+str(Tugas22m.Total(nama)))