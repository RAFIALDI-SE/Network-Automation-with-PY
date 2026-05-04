# String merupakan immutable artinya setiap indek yang ada pada string tidak dapat di ubah

variabel = "Rafi Aldi"
print(len(variabel))

# Item pada string tidak bisa di edit ini akan error tapi kita bisa untuk mengubahnya 
# variabel[1] = "P" 

print(variabel)

# tapi kita bisa mengganti keseluruhan string itu bisa 
variabel = "Pafi Aldi"
print(variabel)

variabel= "Rafi Aldi"
print(variabel)
# method yang kita gunakan ini akan mengeluarkan output saja jika ingin mengubahnya kita buat variabel baru
print(variabel.upper())
print(variabel)
variabel1 = variabel.upper()
print(variabel1)
print(variabel1.lower())
print(variabel1.capitalize())
# print(dir(variabel))

print(variabel.endswith('p'))
print(variabel.endswith('i'))

print(variabel.startswith('R'))

# Strip akan menghapus spasi yang ada didepan dan belakang string tergantung spasinya memakai karakter apa ?
variabel2 = "        Rafi Aldi     "
print(variabel2)
print(variabel2.strip())

variabel3 = "........Rafi Aldi........"
print(variabel3) 
print(variabel3.strip(".")) 

# split akan memisahkan strig kita menjadi sebuah list tapi tergantung pemisahnya berdasarkan apa
print(variabel)
print(variabel.split())

variabel4 = "Rafi,Aldi,Putra"
print(variabel4)
print(type(variabel4))
print(variabel4.split(","))
print(type(variabel4.split(",")))