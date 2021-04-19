while True:
    try:
        num = int(input("masukkan angka pertama: "))
        num2 = int(input("masukkan angka kedua: "))
        res = num / num2
        break
    except ValueError:
        print("data yang anda masukkan bukan berupa angka")
    except ZeroDivisionError:
         print("masukkan angka selain nol")

print("berhasil data yang anda masukkan adalah angka, hasilya adalah", res)

# bisa juga menggunakan syntax di bawah
# except Exception as err:
#    print(err)
# syntax di atas digunakan untuk mencetak apapun error yag keluar (baik untuk debugging)

# tipe-tipe exception error
# IOError : error pada data masuk atau keluar contoh file .txt, corrup, etc.
# importError : error yang terjadi saat module yang digunakan tidak ada
# valueError
# Division by zero
# EOFError