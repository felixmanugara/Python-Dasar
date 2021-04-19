# input output file

# input output command
# w = write mode / mode untuk menulis atau menghapus file lama, jika file belum dibuat maka akan dibuat baru
# r = read only mode 
# a = appending mode / menambahkan data pada akhir baris
# r+ = write and read mode

# membuat file text

file = open("data.txt",'w')

file.write("ini adalah baris pertama untuk file data.txt")
file.write("\nini adalah baris kedua")
file.write("\nini adalah baris ketiga")

file.close()  

# membaca file

file = open("data.txt",'r')

#print(file.read()) kita bisa mengatur jumlah karakter yang ingin ditampilkan (5)

print(file.readline())

file.close()

# appending mode

file = open("data.txt",'a')

file.write("\nbaris ini dibuat menggunakan mode append")

file.close()