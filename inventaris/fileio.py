
# Modul untuk menyimpan dan membaca data barang
from pathlib import Path

# Menentukan folder utama project inventaris_toko
FOLDER_PROJECT = Path(__file__).resolve().parent.parent


def simpan_barang(data_barang, nama_file="barang.txt"):
    # Menambahkan data baru tanpa menghapus data sebelumnya
    lokasi_file = FOLDER_PROJECT / nama_file

    try:
        # Membuat file baru jika belum tersedia
        if not lokasi_file.exists():
            if not buat_file_barang(nama_file):
                return False

        # Mode a digunakan untuk menambahkan data
        with open(lokasi_file, "a", encoding="utf-8") as file:
            for barang in data_barang:
                nama = barang["nama"]
                harga = barang["harga"]
                stok = barang["stok"]

                # Mencegah pemisah file merusak format data
                if "|" in nama or "\n" in nama:
                    raise ValueError("Nama barang mengandung karakter terlarang.")

                file.write(f"{nama}|{harga}|{stok}\n")

        print("Data barang berhasil disimpan.")
        return True

    except (OSError, KeyError, TypeError, ValueError) as error:
        # Menangani kegagalan file atau struktur data
        print(f"Gagal menyimpan data barang: {error}")
        return False


def baca_barang(nama_file="barang.txt"):
    # Membaca data barang dan melewati baris yang rusak
    lokasi_file = FOLDER_PROJECT / nama_file
    daftar_barang = []

    try:
        # Mode r digunakan untuk membaca file
        with open(lokasi_file, "r", encoding="utf-8") as file:
            for baris in file:
                try:
                    nama, harga, stok = baris.strip().split("|")
                    harga = int(harga)
                    stok = int(stok)

                    # Memastikan data yang dibaca masuk akal
                    if not nama.strip() or harga < 0 or stok < 0:
                        raise ValueError("Isi data tidak valid.")

                    daftar_barang.append({
                        "nama": nama,
                        "harga": harga,
                        "stok": stok
                    })

                except ValueError:
                    # Baris rusak dilewati tanpa menghentikan program
                    print(
                        f"Data dilewati karena tidak valid: {baris.strip()}"
                    )

    except FileNotFoundError:
        # Membuat file kosong jika belum tersedia
        print("File barang belum ada. Membuat file baru.")
        buat_file_barang(nama_file)

    except OSError as error:
        # Menangani kesalahan saat membaca file
        print(f"Gagal membaca data barang: {error}")

    return daftar_barang


def buat_file_barang(nama_file="barang.txt"):
    # Mode x membuat file baru tanpa menimpa file lama
    lokasi_file = FOLDER_PROJECT / nama_file

    try:
        with open(lokasi_file, "x", encoding="utf-8") as file:
            file.write("")

        print(f"File berhasil dibuat: {lokasi_file}")
        return True

    except FileExistsError:
        # File yang sudah ada tidak dibuat ulang
        return True

    except OSError as error:
        print(f"Gagal membuat file: {error}")
        return False


def simpan_laporan(isi, nama_file="laporan.txt"):
    # Mode w membuat atau menimpa laporan lama
    lokasi_file = FOLDER_PROJECT / nama_file

    try:
        with open(lokasi_file, "w", encoding="utf-8") as file:
            file.write(isi)

        print(f"Laporan berhasil disimpan di: {lokasi_file}")
        return True

    except OSError as error:
        print(f"Gagal menyimpan laporan: {error}")
        return False


if __name__ == "__main__":
    # Pengujian lokal fungsi pembuatan file dan laporan
    buat_file_barang()
    simpan_laporan(
        "LAPORAN INVENTARIS TOKO\n"
        "Program inventaris berhasil dijalankan.\n"
    )
