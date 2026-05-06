data_string = "Hallo semua"

for data in data_string :
    print(data)

data_list = ["mangga", "apel", "pepaya", "jeruk", "salak"]

for x in data_list :
    print(f"Buah {x}")

for x in range(len(data_list)) :
    print(f"index {x} buah {data_list[x]}")

for index, value in enumerate(data_list) :
    print(f"index {index} data : {value}")

data_dict = {
    "nama" : "Rafi Aldi",
    "umur" : 22,
    "kota" : "Jombang",
    "negara" : "Indonesia"
}

for a in data_dict :
    print(a, data_dict[a])

for key, value in data_dict.items() :
    print(key, value)

for key, value in data_dict.items() :
    print(f"key {key} data {value}")

for a in data_dict :
    print(f"key {a} data {data_dict[a]}")