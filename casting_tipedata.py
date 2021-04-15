# casting adalah merubah suatu tipe data ke bentuk tipe data lainnya
# tipe data integer, float, string, boolean
print("======merubah tipe data int======")
data_int = 12
print("data = ", data_int, ", type =", type(data_int))

# merubah tipe data int ke tiga tipe data lainnya

data_float = float(data_int)
data_str = str(data_int)
data_bool = bool(data_int) # bernilai false jika data_int = 0
print("data = ", data_float, ", type =", type(data_float))
print("data = ", data_str, ", type =", type(data_str))
print("data = ", data_bool, ", type =", type(data_bool))

print("======merubah tipe data float======")
data_float = 7.0
print("data = ", data_float, ", type =", type(data_float))

# merubah tipe data float ke tiga tipe data lainnya
data_int = int(data_float)
data_str = str(data_float)
data_bool = bool(data_float)
print("data = ", data_int, ", type =", type(data_int))
print("data = ", data_str, ", type =", type(data_str))
print("data = ", data_bool, ", type =", type(data_bool))

print("======merubah tipe data string======")
data_str = "data string"
print("data = ", data_str, ", type =", type(data_str))

# merubah tipe data string ke tiga tipe data lainnya
#data_int = int(data_str) untuk string ke int harus angka
#data_float = float(data_str) untuk string ke float harus angka
data_bool = bool(data_str)
#print("data = ", data_int, ", type =", type(data_int))
#print("data = ", data_float, ", type =", type(data_float))
print("data = ", data_bool, ", type =", type(data_bool))

print("======merubah tipe data boolean======")
data_bool = False
print("data = ", data_bool, ", type =", type(data_bool))

# merubah tipe data int ke tiga tipe data lainnya
data_float = float(data_bool)
data_str = str(data_bool) # string harus kososng jika ingin menghasilkan false
data_int = int(data_bool)
print("data = ", data_float, ", type =", type(data_float))
print("data = ", data_str, ", type =", type(data_str))
print("data = ", data_int, ", type =", type(data_int))