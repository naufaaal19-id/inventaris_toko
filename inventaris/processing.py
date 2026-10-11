
# Fungsi untuk mengolah dan mencari data barang

def hitung_total_nilai(daftar_barang):
    # Menghitung nilai seluruh stok barang
    total = sum(
        barang["harga"] * barang["stok"]
        for barang in daftar_barang
    )
    return total


def cari_barang(daftar_barang, kata_kunci):
    # Mencari barang berdasarkan nama menggunakan lambda
    hasil = list(
        filter(
            lambda barang: kata_kunci.lower() in barang["nama"].lower(),
            daftar_barang
        )
    )
    return hasil


def urutkan_barang(daftar_barang, berdasarkan="nama"):
    # Mengurutkan barang berdasarkan nama, harga, atau stok
    if berdasarkan not in ("nama", "harga", "stok"):
        raise ValueError("Pilihan pengurutan tidak tersedia.")

    return sorted(
        daftar_barang,
        key=lambda barang: barang[berdasarkan]
    )


def hitung_total_banyak_barang(*args):
    # *args menerima beberapa angka untuk dijumlahkan
    return sum(args)


def buat_data_barang(**kwargs):
    # **kwargs menerima atribut barang yang bervariasi
    return kwargs


def format_rupiah(nilai, *, simbol="Rp"):
    # Keyword-only argument untuk menentukan simbol mata uang
    return f"{simbol}{nilai:,}".replace(",", ".")


if __name__ == "__main__":
    # Pengujian lokal fungsi pengolahan data
    print("Total angka:", hitung_total_banyak_barang(1000, 2000, 3000))

    data = buat_data_barang(
        nama="Buku",
        harga=5000,
        stok=10
    )
    print("Data barang:", data)

    print("Format harga:", format_rupiah(5000, simbol="Rp"))
