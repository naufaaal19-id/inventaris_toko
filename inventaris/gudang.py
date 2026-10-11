
# Class untuk mengelola kumpulan barang

class Gudang:
    def __init__(self):
        # Menyimpan daftar objek barang
        self.daftar_barang = []

    def tambah(self, barang):
        # Memastikan yang ditambahkan merupakan objek Barang
        from .barang import Barang

        if not isinstance(barang, Barang):
            raise TypeError("Data harus berupa objek Barang.")

        self.daftar_barang.append(barang)

    def cari(self, kata_kunci):
        # Mencari barang berdasarkan nama
        return [
            barang for barang in self.daftar_barang
            if kata_kunci.lower() in barang.nama.lower()
        ]

    def hitung_total(self):
        # Menghitung nilai seluruh stok barang
        return sum(
            barang.hitung_nilai()
            for barang in self.daftar_barang
        )

    def tampilkan_semua(self):
        # Mengembalikan informasi semua barang
        return [
            barang.tampilkan_info()
            for barang in self.daftar_barang
        ]
