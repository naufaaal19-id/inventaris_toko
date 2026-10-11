
# Program Inventaris Barang Toko

# Mengimpor fungsi dari package inventaris
from inventaris import (
    validasi_barang,
    simpan_barang,
    baca_barang,
    hitung_total_nilai,
    cari_barang
)


def tampilkan_menu():
    # Menampilkan pilihan menu program
    print("\n=== INVENTARIS BARANG TOKO ===")
    print("1. Tambah barang")
    print("2. Lihat barang")
    print("3. Cari barang")
    print("4. Hitung total nilai stok")
    print("5. Keluar")


def tambah_barang(daftar_barang):
    # Meminta input, memvalidasi, dan menyimpan barang baru
    try:
        nama = input("Nama barang: ").strip()
        harga = int(input("Harga barang: "))
        stok = int(input("Jumlah stok: "))

        validasi_barang(nama, harga, stok)

        data = {
            "nama": nama,
            "harga": harga,
            "stok": stok
        }

        daftar_barang.append(data)
        simpan_barang([data])

        print("Barang berhasil ditambahkan.")

    except ValueError as error:
        # Menangani input angka atau data yang tidak valid
        print(f"Data tidak valid: {error}")


def lihat_barang(daftar_barang):
    # Menampilkan seluruh data barang
    if not daftar_barang:
        print("Belum ada data barang.")
        return

    for nomor, barang in enumerate(daftar_barang, start=1):
        print(
            f"{nomor}. {barang['nama']} | "
            f"Harga: Rp{barang['harga']} | "
            f"Stok: {barang['stok']}"
        )


def main():
    # Membaca data lama saat program dimulai
    daftar_barang = baca_barang()

    # Mengulang menu sampai pengguna memilih keluar
    while True:
        tampilkan_menu()
        pilihan = input("Pilih menu (1-5): ").strip()

        if pilihan == "1":
            tambah_barang(daftar_barang)

        elif pilihan == "2":
            lihat_barang(daftar_barang=daftar_barang)

        elif pilihan == "3":
            kata_kunci = input("Nama barang yang dicari: ")
            hasil = cari_barang(daftar_barang, kata_kunci)
            lihat_barang(daftar_barang=hasil)

        elif pilihan == "4":
            total = hitung_total_nilai(daftar_barang)
            print(f"Total nilai stok: Rp{total}")

        elif pilihan == "5":
            print("Program selesai. Sampai jumpa!")
            break

        else:
            print("Pilihan tidak tersedia. Coba lagi.")


# Menjalankan program utama
if __name__ == "__main__":
    main()
