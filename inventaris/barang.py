
# Class untuk merepresentasikan satu barang

class Barang:
    def __init__(self, nama, harga, stok):
        # Memastikan data barang valid sebelum disimpan
        if not nama.strip():
            raise ValueError("Nama barang tidak boleh kosong.")

        if harga < 0 or stok < 0:
            raise ValueError("Harga dan stok tidak boleh negatif.")

        # Menyimpan informasi barang
        self.nama = nama
        self.harga = harga
        self.stok = stok

    def hitung_nilai(self):
        # Menghitung nilai seluruh stok barang
        return self.harga * self.stok

    def tampilkan_info(self):
        # Mengembalikan informasi barang dalam bentuk teks
        return (
            f"{self.nama} | "
            f"Harga: Rp{self.harga} | "
            f"Stok: {self.stok}"
        )
