# String indexing
# Karakter Rafi = R=0 a=1 f=2 i=3
# Dibalik Rafi = R=0 a=-3 f=-2 i=-1  karakter terakhir pasti -1 ini mempermudah kita dalam akses karakter terakhir

variabel = "Rafi"
# Akses huruf f
print(variabel[2])
# Gunakan revers index untuk akses huruf f
print(variabel[-2])

variabel = "Rafi Aldi"
# Akses huruf d
print(variabel[7])
# Gunakan revers index untuk akses huruf d
print(variabel[-2])