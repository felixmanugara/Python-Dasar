# adalah sebuah tipe data asosiatif menggunakan mapping
# {key:value}

anggota1 = { "NIM":989808997,
            "Nama": "Felix",
            "Pekerjaan": "Pelajar",
            "Status": "manusia"
          }

print(anggota1)
print(anggota1["NIM"]) # digunakan untuk memanggil data berdasarkan key
print(anggota1["Nama"])
print(anggota1.keys()) # digunakan untuk mengetahui key apa saja yang ada di dalam dictionary
print(anggota1.values()) # digunakan untuk mengetahui data apa saja yang ada di dalam dictionary

anggota2 = { "NIM":989808998,
            "Nama": "Marco",
            "Pekerjaan": "Pelajar",
            "Status": "manusia"
          }

list_anggota = {989808997:anggota1,989808998:anggota2} # digunakan untuk menggabungkan data dictionary
print(list_anggota[989808998]) # memanggil list dictionary berdasarkan key dari data dictionary yang bersangkutan

