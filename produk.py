class Produk:
    def __init__(self, nama, harga, stok):
        self.__nama = ""
        self.__harga = 0.0
        self.__stok = 0
        self.nama = nama
        self.harga = harga
        self.stok = stok

    # ---------------- GETTER (@property) ----------------
    @property
    def nama(self):
        """Nama produk."""
        return self.__nama

    @property
    def harga(self):
        """Harga satuan produk (Rupiah)."""
        return self.__harga

    @property
    def stok(self):
        """Jumlah stok tersedia."""
        return self.__stok

    # ---------------- SETTER (dengan validasi) ----------------
    @nama.setter
    def nama(self, nama):
        """Nama harus teks dan tidak boleh kosong."""
        if isinstance(nama, str) and nama.strip():
            self.__nama = nama.strip()
        else:
            print(f"Error: Nama produk tidak valid! ({nama!r})")

    @harga.setter
    def harga(self, harga):
        """Harga harus angka dan tidak boleh negatif."""
        if isinstance(harga, (int, float)) and not isinstance(harga, bool) and harga >= 0:
            self.__harga = float(harga)
        else:
            print(f"Error: Harga tidak boleh negatif! ({harga})")

    @stok.setter
    def stok(self, stok):
        """Stok harus bilangan bulat dan tidak boleh negatif."""
        if isinstance(stok, int) and not isinstance(stok, bool) and stok >= 0:
            self.__stok = stok
        else:
            print(f"Error: Stok tidak boleh negatif! ({stok})")

    # ---------------- Method tambahan ----------------
    def info(self):
        """Menampilkan seluruh data produk."""
        print(f"Nama  : {self.__nama}")
        print(f"Harga : Rp {self.__harga:,.0f}")
        print(f"Stok  : {self.__stok} unit")

    def __str__(self):
        """Representasi singkat produk."""
        return f"{self.__nama} (Rp {self.__harga:,.0f}, stok {self.__stok})"


if __name__ == "__main__":
    print("=== CONTOH UJI SESUAI SOAL ===")
    produk = Produk("Laptop", 15000000, 10)
    produk.harga = -5000      # Harus muncul error!
    produk.stok = -3          # Harus muncul error!
    produk.nama = ""          # Harus muncul error!
    produk.info()

    print("\n=== UJI PERUBAHAN DATA YANG SAH ===")
    produk.harga = 14500000
    produk.stok = 8
    produk.info()

    print("\n=== GETTER @property BISA DIBACA SEPERTI ATTRIBUTE BIASA ===")
    print(f"produk.nama  = {produk.nama}")
    print(f"produk.harga = {produk.harga}")
    print(f"produk.stok  = {produk.stok}")

    print("\n=== ATTRIBUTE PRIVATE: TIDAK BISA DIAKSES LANGSUNG ===")
    for attr in ("__nama", "__harga", "__stok"):
        try:
            print(f"produk.{attr} = {getattr(produk, attr)}")
        except AttributeError as e:
            print(f"produk.{attr} -> AttributeError: {e}")

    print("\n=== PRODUK KEDUA (data berbeda) ===")
    produk2 = Produk("Mouse Wireless", 185000, 25)
    produk2.stok = 0          # stok 0 masih sah (tidak negatif)
    produk2.info()
    print(f"Ringkas: {produk2}")
