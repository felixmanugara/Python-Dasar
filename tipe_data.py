# bebagai macam tipe data yang ada pada python
# tipe data integer
nilai_integer = 8
print("data :", nilai_integer, ", bertipe :", type(nilai_integer))

# tipe data float
nilai_float = 8.0
print("data :", nilai_float, ", bertipe :", type(nilai_float))

# tipe data string
nilai_string = "contoh string"
print("data :", nilai_string, ", bertipe :", type(nilai_string))

# tipe data boolean
nilai_bool = True
print("data :", nilai_bool, ", bertipe :", type(nilai_bool))

# bilangan kompleks
nilai_kompleks = complex(7,5)
print("data : ", nilai_kompleks, ", bertipe : ", type(nilai_kompleks))

# kita juga dapat menggunakan tipe data yang ada pada bahasa C
# tipe data dari bahasa C

from ctypes import c_double # modul library untuk tipe data bahasa C 

nilai_c_double = c_double(34.6)
print("data :", nilai_c_double, ", bertipe :", type(nilai_c_double))

