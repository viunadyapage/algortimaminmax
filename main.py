import time
import openpyxl # type: ignore
import matplotlib.pyplot as plt
from iterative import find_min_max_iterative
from recursive import find_min_max_recursive
from binary_search import find_min_max_binary # type: ignore

def main():
    # Membuat workbook Excel
    workbook = openpyxl.Workbook()
    sheet = workbook.active
    sheet.title = "Perbandingan Algoritma"
    sheet.append([
        "Ukuran Data", "Min Manual", "Max Manual",
        "Min Iteratif", "Max Iteratif", "Waktu Iteratif (ms)", "Akurasi Iteratif (%)",
        "Min Rekursif", "Max Rekursif", "Waktu Rekursif (ms)", "Akurasi Rekursif (%)",
        "Min Binary Search", "Max Binary Search", "Waktu Binary Search (ms)", "Akurasi Binary Search (%)"
    ])

    # Daftar ukuran data yang akan diuji
    arr_sizes = [10, 100, 1000, 5000, 10000]
    results = []

    for size in arr_sizes:
        print(f"Masukkan array dengan {size} elemen (pisahkan angka dengan spasi):")
        user_input = input("> ").strip()

        try:
            arr = list(map(int, user_input.split()))
            if len(arr) != size:
                print(f"Error: Array harus berisi tepat {size} elemen.")
                continue
        except ValueError:
            print("Input tidak valid. Masukkan angka yang dipisahkan dengan spasi.")
            continue

        print("Masukkan nilai minimum yang dihitung manual:")
        manual_min = int(input("> "))
        print("Masukkan nilai maksimum yang dihitung manual:")
        manual_max = int(input("> "))

        # Iteratif
        start_time = time.time()
        min_iter, max_iter = find_min_max_iterative(arr)
        iter_time = (time.time() - start_time) * 1000  # dalam ms
        iter_accuracy = 100 if (manual_min == min_iter and manual_max == max_iter) else 0

        # Rekursif
        start_time = time.time()
        min_rec, max_rec = find_min_max_recursive(arr, 0, len(arr) - 1)
        rec_time = (time.time() - start_time) * 1000  # dalam ms
        rec_accuracy = 100 if (manual_min == min_rec and manual_max == max_rec) else 0

        # Binary Search
        start_time = time.time()
        min_bin, max_bin = find_min_max_binary(arr.copy())
        bin_time = (time.time() - start_time) * 1000  # dalam ms
        bin_accuracy = 100 if (manual_min == min_bin and manual_max == max_bin) else 0

        # Simpan hasil ke Excel dan daftar hasil
        sheet.append([
            size, manual_min, manual_max,
            min_iter, max_iter, iter_time, iter_accuracy,
            min_rec, max_rec, rec_time, rec_accuracy,
            min_bin, max_bin, bin_time, bin_accuracy
        ])
        results.append({
            "Ukuran Data": size,
            "Waktu Iteratif (ms)": iter_time,
            "Waktu Rekursif (ms)": rec_time,
            "Waktu Binary Search (ms)": bin_time
        })

        # Tampilkan hasil di terminal
        print("\nHasil:")
        print(f"Iteratif: Min={min_iter}, Max={max_iter}, Waktu={iter_time:.6f} ms, Akurasi={iter_accuracy}%")
        print(f"Rekursif: Min={min_rec}, Max={max_rec}, Waktu={rec_time:.6f} ms, Akurasi={rec_accuracy}%")
        print(f"Binary Search: Min={min_bin}, Max={max_bin}, Waktu={bin_time:.6f} ms, Akurasi={bin_accuracy}%\n")

    # Simpan file Excel
    workbook.save("hasil_perbandingan.xlsx")
    print("Hasil disimpan ke file 'hasil_perbandingan.xlsx'.")

    # Buat grafik runtime
    sizes = [result["Ukuran Data"] for result in results]
    iter_times = [result["Waktu Iteratif (ms)"] for result in results]
    rec_times = [result["Waktu Rekursif (ms)"] for result in results]
    bin_times = [result["Waktu Binary Search (ms)"] for result in results]

    plt.figure(figsize=(10, 6))
    plt.plot(sizes, iter_times, label="Iteratif", marker='o')
    plt.plot(sizes, rec_times, label="Rekursif", marker='o', linestyle='--')
    plt.plot(sizes, bin_times, label="Binary Search", marker='o', linestyle='-.')
    plt.title("Perbandingan Waktu Eksekusi")
    plt.xlabel("Ukuran Data")
    plt.ylabel("Waktu Eksekusi (ms)")
    plt.legend()
    plt.grid(True)
    plt.savefig("perbandingan_runtime.png")
    plt.show()

if __name__ == "__main__":
    main()
