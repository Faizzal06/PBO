class Mahasiswa:
    def __init__(self, nama, nim, ipk):
        self.__nama = nama
        self.__nim = nim
        self.__ipk = ipk

# Getter dan Setter Nama
    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, nama):
        if nama and isinstance(nama, str):
            self.__nama = nama
        else:
            print("Error: Nama tidak valid!")

# Getter dan Setter NIM
    @property
    def nim(self):
        return self.__nim
    
    @nim.setter
    def nim(self, nim):
        if nim and isinstance(nim, str):
            self.__nim = nim
        else:
            print("Error: NIM tidak valid!")

# Getter dan Setter IPK
    @property
    def ipk(self):
        return self.__ipk
    @ipk.setter
    def ipk(self, nilai):
        if 0.0 <= nilai <= 4.0:
            self.__ipk = nilai
        else:
            print("Error: IPK harus 0.0 - 4.0!")

# Method Tampilkan data
    def tampilkan_data(self):
        print(f"Nama: {self.__nama}")
        print(f"NIM: {self.__nim}")
        print(f"IPK: {self.__ipk}")

# Membuat data
mhs = Mahasiswa("Andi", "202601", 3.5)
mhs1 = Mahasiswa("Budi", "202602", 3.8)
mhs.tampilkan_data()
mhs1.tampilkan_data()

# Mengubah data
print("==== setelah data diubah ====")
mhs.nama = "Andi Haryanto"
mhs.ipk = 3.6
mhs1.nama = "Budiono"
mhs1.ipk = 3.9
mhs.tampilkan_data()
mhs1.tampilkan_data()