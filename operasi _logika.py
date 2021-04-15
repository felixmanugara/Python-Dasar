# operasi logika 
# not, or, and , xor

print("====NOT====")
x = True
y = not x
print('data x =', x)
print('NOT--------')
print('data y =', y)

print("====OR====") # jika salah satu atau kedua nilai True maka hasilnya True
x = False
y = True
z = x or y
print('data x =', x)
print('data y =', y)
print('OR--------')
print(x, 'OR' ,y, '=', z)

print("====AND====") # jika kedua nilai True maka hasilnya True
x = True
y = False
z = x and y
print('data x =', x)
print('data y =', y)
print('AND--------')
print(x, 'AND' ,y, '=', z)

print("====XOR====") # jika salah satu nilai true maka hasilnya true
x = True
y = True
z = x ^ y
print('data x =', x)
print('data y =', y)
print('XOR--------')
print(x, 'XOR' ,y, '=', z)





