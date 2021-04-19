# set atau himpunan : karakteristik tidak mempunyai urutan
# set tidak mendukung duplikasi data
makanan = {"bakmi",
           "bacang",
           "nasi tim",
           "nasi hainan"}

makanan.add("pangsit")
makanan.add("bakmi") # jika memasukkan data yang sudah ada di dalam set maka tidak akan dimasukkan

print(makanan)

# cara kedua membuat set
makanan = set()

makanan.add("bakmi")
makanan.add("bacang")
makanan.add("nasi hainan")
print(makanan)
print(sorted(makanan)) # sorted digunakan jika ingin mengurutkan tipe data set



