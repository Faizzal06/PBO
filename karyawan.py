class Karyawan:
    LEMBUR_PER_JAM = 50_000   # Konstanta: 1 jam lembur = Rp 50.000
    def __init__(self, nama, nik, gaji_pokok):
        self.__nama = ""
        self.__nik = ""
        self.__gaji_pokok = 0.0
        self.nama = nama
        self.__nik = nik         
        self.gaji_pokok = gaji_pokok

    # ---------------- GETTER & SETTER: nama ----------------
    @property
    def nama(self):
        """Nama karyawan."""
        return self.__nama

    @nama.setter
    def nama(self, nama):
        """Nama harus teks dan tidak boleh kosong."""
        if isinstance(nama, str) and nama.strip():
            self.__nama = nama.strip()
        else:
            print(f"Error: Nama tidak valid! ({nama!r})")

    # ---------------- GETTER saja: nik (read-only) ----------------
    @property
    def nik(self):
        """NIK hanya bisa dibaca, TIDAK ada setter-nya."""
        return self.__nik

    # ---------------- GETTER & SETTER: gaji_pokok ----------------
    @property
    def gaji_pokok(self):
        """Gaji pokok karyawan (Rupiah)."""
        return self.__gaji_pokok

    @gaji_pokok.setter
    def gaji_pokok(self, gaji):
        """Gaji pokok harus angka dan minimal Rp 100.000 (tidak boleh negatif)."""
        if isinstance(gaji, (int, float)) and not isinstance(gaji, bool) and gaji >= 100_000:
            self.__gaji_pokok = float(gaji)
        else:
            print(f"Error: Gaji pokok tidak valid! ({gaji}) - minimal Rp 100.000")

    # ---------------- Method tambahan ----------------
    def tambah_lembur(self, jam):
        """Menambah gaji dari lembur: 1 jam lembur = Rp 50.000."""
        if isinstance(jam, (int, float)) and not isinstance(jam, bool) and jam > 0:
            tambahan = jam * self.LEMBUR_PER_JAM
            self.__gaji_pokok += tambahan
            print(f"Lembur {jam} jam x Rp {self.LEMBUR_PER_JAM:,} = Rp {tambahan:,.0f}")
            print(f"Gaji sekarang: Rp {self.__gaji_pokok:,.0f}")
        else:
            print(f"Error: Jam lembur tidak valid! ({jam}) - harus angka positif")

    def info(self):
        """Menampilkan data karyawan."""
        print(f"Nama       : {self.__nama}")
        print(f"NIK        : {self.__nik}")
        print(f"Gaji Pokok : Rp {self.__gaji_pokok:,.0f}")


if __name__ == "__main__":
    print("=== CONTOH UJI SESUAI SOAL ===")
    karyawan = Karyawan("Budi", "K001", 5000000)
    karyawan.tambah_lembur(3)   # Gaji jadi 5150000
    karyawan.info()

    print("\n=== SETTER VALIDASI: DATA TIDAK VALID DITOLAK ===")
    karyawan.nama = ""               # Error
    karyawan.gaji_pokok = -1000000   # Error (negatif)
    karyawan.gaji_pokok = 50000      # Error (di bawah batas minimal)
    karyawan.tambah_lembur(0)        # Error
    karyawan.tambah_lembur(-2)       # Error

    print("\n=== SETTER VALIDASI: DATA VALID DITERIMA ===")
    karyawan.nama = "Budi Setiawan"
    karyawan.gaji_pokok = 6000000
    karyawan.tambah_lembur(2)        # +100.000
    karyawan.info()

    print("\n=== NIK READ-ONLY: TIDAK BISA DIUBAH SETELAH DIBUAT ===")
    print(f"karyawan.nik = {karyawan.nik}  (bisa dibaca)")
    try:
        karyawan.nik = "K999"        # Tidak ada setter -> AttributeError
        print("NIK berhasil diubah (ini tidak seharusnya terjadi!)")
    except AttributeError as e:
        print(f"Gagal mengubah NIK -> AttributeError: {e}")
    print(f"NIK tetap: {karyawan.nik}")

    print("\n=== ATTRIBUTE PRIVATE: TIDAK BISA DIAKSES LANGSUNG ===")
    for attr in ("__nama", "__nik", "__gaji_pokok"):
        try:
            print(f"karyawan.{attr} = {getattr(karyawan, attr)}")
        except AttributeError as e:
            print(f"karyawan.{attr} -> AttributeError: {e}")

    print("\n=== KARYAWAN KEDUA (data berbeda) ===")
    karyawan2 = Karyawan("Siti Aminah", "K002", 4200000)
    karyawan2.tambah_lembur(10)      # +500.000
    karyawan2.info()
