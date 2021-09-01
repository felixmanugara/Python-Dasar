nama_makanan = ['bakmi',
                 'bacang',
                 'nasi tim',
                 'nasi hainan',
                 'pangsit']

nama_minuman = ['cola',
        'bir',
        'kopi',
        'teh',
        'air putih']
# for index,value
for i,makanan in enumerate(nama_makanan): # enumerate digunakan untuk memberi nomor pada loop
    print(i,':',makanan)

# zip : untuk menggabungkan dua dictionary 

for makanan,minuman in zip(nama_makanan,nama_minuman):
    print('makan',makanan,'minumnya',minuman)

# set 
angka = {"satu","tiga","lima","tujuh","sembilan"}

for num in sorted(angka):
    print(num)

# dictionary
food = {'bakmi':'jumbo',
        'bacang':'ayam',
        'nasi tim':'ayam',
        'nasi hainan':'kenanga',
        'pangsit':'udang'}
# bisa menggunakan .keys() atau .values()
for i in food.items():
    print(i)
