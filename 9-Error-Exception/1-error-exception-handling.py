file = open("file.txt", "w")
file.write("Mangga\nApel\nJeruk\nSalak")
file.close()

file_baru = open("file.txt", "r")
print(file_baru.read())

try :
    file_baru_lagi = open(file.txt, "r")
    print(file_baru_lagi.read())
except FileNotFoundError :
    print("File tidak ditemukan")
except ValueError :
    print("Argumen tidak dapat digunakan")
except :
    print("ada error yang lain mungkin")

print("Akhir dari kode")