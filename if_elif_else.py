# if digunakan untuk membuat keputusan

data = 60

if data == 50: # merupakan kondisi yang harus dipenuhi
    print('data sama dengan 50') # jika kondisi terpenuhi makan kode ini akan dieksekusi
else:
    print('data tidak sama dengan 50')

# nested if

data = int(input("masukkan angka: "))

if data >= 5:  # merupakan kondisi yang harus dipenuhi
    if data == 10:
        print('data di bawah atau sama dengan 10')
    else:
        print('data di atas 10')

# nested if vs if elif

def analisa_umur(age):
    if age < 21:
        print("kamu masih anak - anak")
    if age >= 21:
        print("kamu sudah dewasa")
    else:
        print("ini adalah else")

# komputer melihat kedua if sebagai 2 penyataan terpisah yang akan dieksekusi keduanya
# dan else yang akan menjadi output

analisa_umur(21)

def analyzeAge(umur):
    if umur < 21:
        print("kamu masih anak - anak")
    elif umur >= 21:
        print("kamu sudah dewasa")
    else:
        print("ini adalah else")

analyzeAge(18)

# sedangkan pada elif komputer melihat ini sebagai kesatuan
# yang mana jika salah satu if condition dipenuhi maka elif akan dilewati