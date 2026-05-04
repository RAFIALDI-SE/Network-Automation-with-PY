# Data tuple sifatnya immutable jadi tidak bisa diubah itemnya 

data_tuple = ("x", "y", "z")

print(data_tuple)
print(data_tuple[1])
print(data_tuple[-1])

# data_tuple[1] = 'a' ini akan menyebabkan error karena sifat dari tuple immutable

data_tuple_baru = (1, 2, 3, 4, 5, 5, 7, 7, 7, 8)
print(data_tuple_baru.count(7))
print(data_tuple_baru.index(3))