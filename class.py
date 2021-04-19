# membuat class bernama people sering juga disebut object
class people:
    "ini adalah people class" # ini adalah doc string
    status = "status" # ini adalah attribute dari people class

    # ini merupakan function object (method/attributes) dari class people
    def age(self):
        print("im 20 years old")
    
    def kegiatan(self):
        print("seorang",self.status)

# ini adalah instance dari class people dengan nama felix
felix = people()
felix.status = "mahasiswa"
felix.age() # ini adalah pemangilan method sama dengan people.age(felix)
felix.kegiatan()


#print(felix.status)
#print(people.__doc__) digunakan untuk memanggil docstring yang ada di dalam class
#print(people.age)
#print(felix.age)
#print(felix.status)
#print(people.status)

class name:
    # __init__ merupakan method yang akan pertama kali dijalankan saat menginisiasi sebuah class
    def __init__(self,input_nama,input_nim): 
        self.nama = input_nama
        self.nim = input_nim

    def status(self):
        print(self.nama,'dengan nim',self.nim,'adalah seorang pelajar')

    def jurusan(self,argumen): # menambahkan argumen kedua pada method
        print(self.nama,"sedang mempelajari computer science",argumen)

data = name("Felix marco",12243546) # untuk menginisiasi class dan memberikan input argumen pada method init
print(data.nama)
print(data.nim)
data.status() # memanggil method status di dalam class
data.jurusan('lewat Youtube') # memanggil method jurusan disertai argumen kedua

class ini:
    # variabel yang diawali tanda __ merupakan variabel yang bersifat private 
    # yang berarti hanya dapat diakses oleh parent element nya saja dalam 
    # contoh ini class ini: merupakan parent dari __value
    __value = 0 

    def add(self,input_value):
        self.__value += input_value # public variable

    def sum(self,input_value):
        self.__value += input_value # public variable
    
    def show(self):
        print(self.__value)


dat = ini()
dat.add(30)
dat.sum(40)
dat.show()

#print(*"=" "class tanpa __init__ method")

#class make:
    #menu = 'menu'
    #def loop(self):
         #for i in makan.menu:
             #print(i)
    
    #def conditional(self,cek_makanan):
        #if cek_makanan in makan.menu:
            #print("ya",cek_makanan,"di dalam list",makan.menu)
        #else:
            #print(cek_makanan,"tidak ada di dalam lsit",makan.menu)

   
#makan = make()
#makan.menu = ['tempe','tahu','molen','bakwan','risoles']

#print(makan.menu)
#makan.loop()
#makan.conditional("tempe")

