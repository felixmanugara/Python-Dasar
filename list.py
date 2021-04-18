# list adalah variabel yang menyimpan lebih dari 1 data atau biasa disebut array

data = [1, 2, 3, 4, 5, 6, 7, 8]
data1 = [2, 5, 7, 3, 8, 9, 6, 0, 1]

# mengakses list dapat dilakukan dengan [index:range:step]
subdata = data[0] # data[0] digunakan untuk memanggil data urutan pertama dari kiri
subdata2 = data[-1] # data[-1] digunakan untuk memanggil data urutan pertama dari kanan

# slicing list
subdata3 = data[2:6] # digunakan untuk memanggil data dari urutan 3 sampai 5 (berhenti sebelum range)
subdata4 = data[-1:] # digunakan untuk mengambil data dari kanan mulai dari paling awal
subdata5 = data[:4] # digunakan untuk memanggil data dari kiri mulai dari paling awal

# memasukkan data kedalam list
data.append(9)

print(subdata)
print(subdata2)
print(subdata3)
print(subdata4)
print(subdata5)
print(data)

a = data[:] # data[:] digunakan untuk mengcopy list ke variabel a 
a[4] = 6 # merubah isi list urutan ke 5 dengan angka 6

print(a) 
print(data)

# merubah content list dengan metode slicing 
data[3:6] = [4, 0, 3]
print(data)

# mengabungkan dua list 
x = [data, data1]
print(x)

# mengakses multidimensinal list
y = x [0] [6] # kurung pertama untuk urutan list dan kurung kedua untuk urutan dari list content
print(y)

# fungsi yang bisa digunakan pada list
panjang_list = len(data)
print(panjang_list)