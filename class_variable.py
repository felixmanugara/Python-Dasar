class pelajar:
    # kedua variabel di bawah merupakan variabel kelas
    jurusan = "komputer"
    jumlah_anggota = 0

    def __init__(self,input_nama,input_kelas):
        self.nama = input_nama
        self.kelas = input_kelas
        # variabel jumlah anggota akan bertambah satu jika ada inisiasi class
        pelajar.jumlah_anggota += 1

# ini merupakan inisiasi class menambahkan 3 instances ke dalam class pelajar
felix = pelajar("Felix",3)
marco = pelajar("Marco",4)
manugara = pelajar("manugara",6)

# nilai variable untuk jurusan manugara akan di ubah ke sosiologi
manugara.jurusan = "sosiologi"

print(felix.nama)
print(marco.nama)
print(manugara.nama)
# output nilai adalah sosiologi, ini tidak akan mempengaruhi nilai instances lainnya
print(manugara.jurusan)
print(felix.jurusan)
# output berupa angka 3 karena kita menambahkan 3 instances ke dalam class pelajar
print(pelajar.jumlah_anggota)