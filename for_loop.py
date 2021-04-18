# for loop merupakan syntax yang digunakan untuk melakukan perulangan 
# for loop biasanya digunakan untuk mengulang proses yang sudah diketahui
# jumlah perulangannya.

nama = "felix"
# i disini merupakan variabel yang digunakan untuk menyimpan
# hasil dari perulangan 
for i in nama:
    print(i)
    # kita juga dapat menyisipkan kondisi dalam sebuah loop
    if i is "f": 
        # jika kondisi di mana variabel i terdapat huruf "f"
        # maka syntax di bawah ini akan dieksekusi
        print("huruf ",i," ditemukan")


# break digunakan untuk keluar dari sebuah loop
print("=========mengunakan statment break============")
data = "belajar python"

for i in data:
    print(i)
    
    if i is "a":
        print("huruf ",i," ditemukan")
        break
        # jika kondisi di atas terpenuhi maka loop akan berhenti 
        # hal ini dimungkinkan dengan penggunaan statment break

# range digunakan untuk membuat set angka
set_angka = []
for i in range(0,11): # akan dibuat set angka dimulai dari 0 sampai 10
    set_angka.append(i)

print(set_angka)

# continue digunakan untuk melanjutkan loop walaupun suatu kondisi telah dipenuhi
for i in range(11,21):
    print(i)
    if i == 15:
        print("angka ",i," ditemukan")
    continue