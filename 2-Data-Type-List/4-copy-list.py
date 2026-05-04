list_1 = [1, 2, 3, 4, 5,]
print(f"data ori di list 1 : {list_1}")

list_2 = list_1 #jika kita memakai cara seperti ketika kita mengubah data pada list_2 maka list_1 satu juga akan ikut berubah
list_3 = list_1.copy() #jika kita memakai cara seperti ini tidak akan mempengaruhi data yang asli
print(list_2)

list_2.pop(0)
print(f"ini data di list 2 : {list_2}")
print(f"ini data di list 1 : {list_1}")


print(list_3)
list_3.pop(1)

print(list_3)