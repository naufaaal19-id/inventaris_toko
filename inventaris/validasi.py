
# Memeriksa apakah data barang sudah benar

def validasi_barang(nama, harga, stok):
    # Memastikan nama barang berupa teks dan tidak kosong
    if not isinstance(nama, str) or not nama.strip():
        raise ValueError("Nama barang tidak boleh kosong.")

    # Memastikan harga berupa bilangan bulat
    if not isinstance(harga, int) or isinstance(harga, bool):
        raise ValueError("Harga harus berupa bilangan bulat.")

    # Memastikan stok berupa bilangan bulat
    if not isinstance(stok, int) or isinstance(stok, bool):
        raise ValueError("Stok harus berupa bilangan bulat.")

    # Memastikan harga dan stok tidak negatif
    if harga < 0 or stok < 0:
        raise ValueError("Harga dan stok tidak boleh negatif.")

    return True


def cek_data_barang(nama, harga, stok):
    # Memastikan data memenuhi ketentuan menggunakan assert
    assert isinstance(nama, str) and nama.strip() != "", \
        "Nama barang tidak boleh kosong."

    assert isinstance(harga, int) and not isinstance(harga, bool), \
        "Harga harus berupa bilangan bulat."

    assert isinstance(stok, int) and not isinstance(stok, bool), \
        "Stok harus berupa bilangan bulat."

    assert harga >= 0, "Harga tidak boleh negatif."
    assert stok >= 0, "Stok tidak boleh negatif."

    return True
