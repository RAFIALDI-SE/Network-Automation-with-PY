# Kita hanya bisa mengkonversi tipe data yang hampir mirip tidak bisa kita konversi data string ke dictionary

a = 2
print(a)
print(type(a))

b = str(a)
print(b)
print(type(b))

list_data = [1, 2, 3, 4, 6, 6, 6, 6, 6, 7, 7, 7]
print(list_data)
print(type(list_data))
data_set = set(list_data)
print(data_set)
print(type(data_set))

# Kode dibawah akan menyebabkan error karena tidak mirip
c = dict(b)
print(c)