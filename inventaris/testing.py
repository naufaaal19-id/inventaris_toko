
# Pengujian fungsi program inventaris

import unittest
import sys
from pathlib import Path

# Menentukan folder utama proyek inventaris_toko
FOLDER_PROJECT = Path(__file__).resolve().parent.parent

# Memastikan package inventaris dapat ditemukan Python
if str(FOLDER_PROJECT) not in sys.path:
    sys.path.insert(0, str(FOLDER_PROJECT))

# Mengimpor fungsi dari modul processing
from inventaris.processing import (
    hitung_total_nilai,
    cari_barang,
    urutkan_barang,
    hitung_total_banyak_barang,
    buat_data_barang,
    format_rupiah
)


class TestInventaris(unittest.TestCase):
    # Tes 1: menghitung nilai seluruh stok
    def test_hitung_total_nilai(self):
        data = [
            {"nama": "Buku", "harga": 5000, "stok": 10},
            {"nama": "Pensil", "harga": 2000, "stok": 20}
        ]

        self.assertEqual(hitung_total_nilai(data), 90000)

    # Tes 2: mencari barang berdasarkan nama
    def test_cari_barang(self):
        data = [
            {"nama": "Buku", "harga": 5000, "stok": 10}
        ]

        hasil = cari_barang(data, "buk")

        self.assertEqual(len(hasil), 1)
        self.assertEqual(hasil[0]["nama"], "Buku")

    # Tes 3: mengurutkan barang berdasarkan harga
    def test_urutkan_barang(self):
        data = [
            {"nama": "Buku", "harga": 5000, "stok": 10},
            {"nama": "Pensil", "harga": 2000, "stok": 20}
        ]

        hasil = urutkan_barang(data, berdasarkan="harga")

        self.assertEqual(hasil[0]["nama"], "Pensil")

    # Tes 4: menguji penggunaan *args
    def test_hitung_total_banyak_barang(self):
        hasil = hitung_total_banyak_barang(1000, 2000, 3000)

        self.assertEqual(hasil, 6000)

    # Tes 5: menguji penggunaan **kwargs
    def test_buat_data_barang(self):
        data = buat_data_barang(
            nama="Buku",
            harga=5000,
            stok=10
        )

        self.assertEqual(data["nama"], "Buku")
        self.assertEqual(data["harga"], 5000)
        self.assertEqual(data["stok"], 10)

    # Tes 6: menguji keyword argument
    def test_format_rupiah(self):
        hasil = format_rupiah(5000, simbol="Rp")

        self.assertEqual(hasil, "Rp5.000")


# Menjalankan pengujian saat file dibuka langsung
if __name__ == "__main__":
    unittest.main(verbosity=1)
