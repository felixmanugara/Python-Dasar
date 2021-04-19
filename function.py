# function adalah sebuah cara yang digunakan 
#untuk menulis kode agar dapat diakses berulang
# dengan mudah

angka = 6
angka1 = 8

def tambah():
    add = angka + angka1
    print(angka," + ", angka1," = ", add) 

tambah() # digunakan untuk memanggil function tambah

# function arguments 
# kita dapat menambahkan nilai untuk diproses
# oleh function yang kita buat 

def bagi(argument1, argument2):
    div = int(argument1 / argument2)
    print(argument1," + ", argument2," = ", div)

bagi(20,5) # penggunaan argument boleh lebih dari 2

# return value
# digunakan untuk mengembalikan nilai yang telah
# diproses oleh function untuk selanjutnya dapat
# digunakan diluar function tersebut

def kali(arg1,arg2):
    power = arg1 * arg2
    return power

result = kali(4,5)

print(result)

# return value dapat juga digunakan untuk
# function lainnya

def kuadrat():
    kuad = result ** 2
    print(kuad)

kuadrat()

# lambda function lambda argumen: hasil
mod = lambda x,y: x % y
res = mod(4,6)
print(res)


