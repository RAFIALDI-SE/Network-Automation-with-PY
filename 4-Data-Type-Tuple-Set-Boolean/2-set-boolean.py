# type data set unorderlist artinya tidak bisa di akses menggunakan index
# biasanya kita gunakan untuk menyimpan nilai list yang duplikat jadi kita lakukan konversi


data_set = {"a", "b", "c"}
print(data_set)

data_set.add("a")
print(data_set)

data_set.add("d")
print(data_set)

print(data_set.pop())
print(data_set)
# code dibawah akan menyebabkan error
# data_set[1]

# data list
data_list = ["a", "b", "c", "d", "d", "d"]
print(data_list)

data_set_baru = set(data_list) #kita konversi ke set terlebih dahulu
print(data_set_baru)

data_list_baru = list(data_set_baru) #kita konversi ke lis lagi
print(data_list_baru)

# Tipe data boolean 
print("a" == "A")
print("a" == "a")