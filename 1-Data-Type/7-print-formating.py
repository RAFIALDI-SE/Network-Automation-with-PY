name = "Rafi"

print("Hallo "+name+"!")

kota = "Malang"

print("Hallo %s berasal dari %s" %(name, kota)) #ini merupakan cara lama memakai %s

# kita bisa coba memakai .format dengan berbagai cara
print("Hallo {}, asal {}".format(name, kota))
print("Hallo {1}, asal {0}".format(name, kota))
print("Hallo {0}, asal {0}".format(name))
# print("Hallo {}, asal {}".format(name)) ini akan menyebabkan error karena index ke 2 atau 1 tidak ada
print("Hallo {a}, asal {b}".format(a=name, b=kota))

# F string ini merupakan cara baru untuk menuliskan dan lebih simpel dan enak dilihat
print(f"Hallo {name}, asal {kota}")
