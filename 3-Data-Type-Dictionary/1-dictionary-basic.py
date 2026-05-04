data = {"nama" : "Rafi", "umur" : 22, "kota" : "Malang"}

print(type(data))
print(data["nama"])
print(data["umur"]) #kalau kita akses pake [] ini akan error jika tidak cocok keynya
print(data.get('kota')) #jika kita pake method get ini tidak akan menampilkan error 

data_baru = {
    "nama" : "Aldi",
    "umur" : 22,
    "kota" : "jombang"
}
print(data_baru)

print(type(data_baru))
print(data_baru["nama"])
print(data_baru["umur"])
print(data_baru.get("kota"))

data_baru["umur"] = 21

print(data_baru)

data_baru["negara"] = "indonesia"
print(data_baru)