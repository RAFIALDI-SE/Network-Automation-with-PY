list_buah = ["apel", "mangga", "salak", "kelapa", "jeruk"]

print(list_buah)
list_buah[1] = "kelengkeng"
print(list_buah)
list_buah.append("pepaya")
print(list_buah)
list_buah.insert(1, "rambusa")
print(list_buah)
list_buah.remove("salak") #ini harus menggunakan datanya
print(list_buah)
list_buah.remove(list_buah[1]) #ini adalah cara kalau kita mengetahui indexnya
print(list_buah)
list_buah.pop()
print(list_buah)
list_buah.pop(1)
print(list_buah)
list_angka = [1, 2, 3, 4, 5]
list_angka1 = [10, 6, 8, 7, 9]

list_hasil = list_angka + list_angka1   
print(list_hasil)
list_hasil.sort()
print(list_hasil)
list_hasil.reverse()
print(list_hasil)