file = open("file_baru_1.txt", "w") # Perintah w ini kalau filenya belum ada maka akan dibuat jika sudah ada akan di replace beda dengan a

file.write("Mangga\nSalak\nNanas\nAnggur\n")
file.write("Jeruk\n")

file.close()

file_baru1 = open("file_baru_1.txt", "w") # Ini akan me replace jika kita gunakan w 
file_baru1.write("Jeruk\n")
file_baru1.close()

file_baru2 = open("file_baru_1.txt", "a") # a ini akan menambahkan data ke file yang sudah ada tidak me replacenya
file_baru2.write("Apel\nJeruk\n")
file_baru2.write("Salak\n")
file_baru2.close()

file_baru3 = open("file_baru_2.txt", "a") # a ini juga kita bisa manfaatkan untuk membuat file baru
file_baru3.write("\nApel\nMangga\nJeruk\nKelengkeng\n")
file_baru3.close()