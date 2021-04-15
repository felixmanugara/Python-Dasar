# berikut adalah operasi aritmatika dalam python

print("======penjumlahan======")
a = 5
b = 6
hasil = a + b # melakukan operasi aritmatika penjumlahan 
print("5 + 6 = ", hasil)

print("======pengurangan======")
a = 5
b = 6
hasil = a - b # melakukan operasi aritmatika pengurangan
print("5 - 6 = ", hasil)

print("======perkalian======")
a = 5
b = 6
hasil = a * b # melakukan operasi aritmatika perkalian 
print("5 x 6 = ", hasil)

print("======pembagian======")
a = 5
b = 6
hasil = a / b # melakukan operasi aritmatika pembagian
print("5 : 6 = ", hasil)

print("======modulus======") # meruakan sisa dari pembagian
a = 12
b = 4
hasil = a % b # melakukan operasi aritmatika modulus
print("12 % 4 = ", hasil)

print("======eksponensial======")
a = 5
b = 6
hasil = a ** b # melakukan operasi aritmatika eksponensial
print("5 ** 6 = ", hasil)

print("======floor division======")
a = 5
b = 6
hasil = a // b # melakukan operasi aritmatika floor division
print("5 // 6 = ", hasil)

# prioritas operasi
"""
    1. ( )
    2. eksponen
    3. perkalian / pembagian
    4. penambahan / pengurangan
"""
x = 6
y = 4
z = 3

result = x + y * z // x % y / z - y
print(x ,"+", y ,"x", z ,"//", x ,"%", y ,":", z ,"-", y , "= ", result)