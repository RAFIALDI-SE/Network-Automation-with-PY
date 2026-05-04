list_angka = [1, 2, 3, 4, 5 ,6 ,7 ,8 ,9, 10]
print(list_angka)
print(f"hasil count : {list_angka.count(5)}")
list_angka.append(5)
print(list_angka)
print(f"hasil count : {list_angka.count(5)}")

print(f"angka 7 ada di index : {list_angka.index(7)}") #ini untuk mencari data ada di index ke berapa

print(f"jumlah data yang ada di list {len(list_angka)}")

print(f"hapus data menggunakan method clear, data di list_angka akan kosong : {list_angka.clear()}")
print(list_angka)