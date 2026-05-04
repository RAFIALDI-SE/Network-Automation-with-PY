data_baru = {
    "nama" : "Aldi",
    "umur" : 22,
    "kota" : "jombang"
}
print(data_baru)

data_baru_2 = data_baru.copy()

print(type(data_baru))
print(data_baru["nama"])
print(data_baru["umur"])
print(data_baru.get("kota"))

data_baru["umur"] = 21

print(data_baru)

data_baru["negara"] = "indonesia"
print(data_baru)

print(data_baru.keys())
print(data_baru.values())
print(data_baru.pop("umur"))
print(data_baru)
print(data_baru.popitem()) #ini akan menghapus dari data terakhir
print(data_baru)
data_baru.clear()
print(data_baru)

print(data_baru_2)