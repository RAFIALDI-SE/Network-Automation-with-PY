file = open('file.txt', 'r')

# print(file.read())
# print(file.tell())
# print(file.seek(0))
# print(file.tell())
# print(file.read())

# data_file = file.read()
# print(data_file)

print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())
print(file.readline())

print(file.tell())
file.seek(0)

data_file_list = file.readlines()
print(data_file_list)

for data in data_file_list :
    print(data)