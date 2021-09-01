# while loop sama dengan for loop yang
# merupakan syntax perulangan cuma bedanya
# while loop sifatnya infinite (tidak akan berhenti)
num = 0 # nilai awal

while num < 5: # kondisi yang akan dicek ketika looping
    print('nilai saat ini', num)
    num +=1 # nilai akan bertambah 1 pada setiap iterasi
    # saat while num tidak lagi kurang
    # dari 5 maka program akan berhenti
begin = True
num = 2

while begin:
    num *= 2
    print(num, "\n")
    

