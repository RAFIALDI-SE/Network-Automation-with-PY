# slicing kita bisa langsung mengambil beberapa karakter menggunakan teknik ini 
# rules [start:stop:step]

variabel = "Rafi Aldi"

print(variabel[5:9])
print(variabel[5:]) #ini akan mengambil nilai sampai terkhir jika nilai stopnya kosong


print(variabel[0:4])
print(variabel[:4]) #ini akan mengambil nilai yang paling depan jika startnya kosong

print(variabel[0:4:2])
print(variabel[:4:2]) #kalau kita pake step jika tidak defaultnya melangkah 1

# cara balik kata 
print(variabel[::-1])
print(variabel)
variabel_baru = variabel[::-1]
print(variabel_baru)
