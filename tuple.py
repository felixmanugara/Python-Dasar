import sys
import timeit
# tuple merupakan tipe data yang tidak bisa diubah nilainya
num = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
ang = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(num.count(3)) # count digunakan untuk menghitung jumlah suatu data yang ada di dalam tuple
print(num.index(5)) # index digunakan untuk mengetahui urutan data yang ada di dalam tuple

# tuple lebih ringan jika dibandingkan dengan list
# kode di bawah digunakan untuk mengetahui jumlah memeori terpakai oleh list dan tuple
data_tuple = sys.getsizeof(num) 
data_list = sys.getsizeof(ang)

print('besar data tuple adalah',data_tuple)
print('besar data list adalah',data_list)

# kode di bawah digunakan untuk mengetahui waktu proses dari list dan tuple

time_tuple = (timeit.timeit(stmt = "(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)"))
time_list = (timeit.timeit(stmt = "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]"))

print('waktu proses tuple',time_tuple)
print('waktu proses list',time_list)