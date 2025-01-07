import time
import csv
import random
import matplotlib.pyplot as plt

# Algoritma Iteratif
def find_min_max_iterative(arr):
    min_val = max_val = arr[0]
    for num in arr[1:]:
        if num < min_val:
            min_val = num
        if num > max_val:
            max_val = num
    return min_val, max_val

# Algoritma Rekursif
def find_min_max_recursive(arr, start, end):
    if start == end:
        return arr[start], arr[start]
    
    mid = (start + end) // 2
    left_min, left_max = find_min_max_recursive(arr, start, mid)
    right_min, right_max = find_min_max_recursive(arr, mid + 1, end)

    return min(left_min, right_min), max(left_max, right_max)

# Algoritma Binary Search
def find_min_max_binary(arr):
    arr.sort()  # Urutkan array
    return arr[0], arr[-1]

def main():
    # File CSV untuk menyimpan hasil
    csv_filename = "hasil_perbandingan.csv"
    with open(csv_filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([
            "Ukuran Data", "Min Manual", "Max Manual",
            "Min Iteratif", "Max Iteratif", "Waktu Iteratif (ms)", "Akurasi Iteratif (%)",
            "Min Rekursif", "Max Rekursif", "Waktu Rekursif (ms)", "Akurasi Rekursif (%)",
            "Min Binary Search", "Max Binary Search", "Waktu Binary Search (ms)", "Akurasi Binary Search (%)"
        ])

        results = []

        while True:
            print("\nMasukkan ukuran array yang ingin diuji (ketik 'exit' untuk keluar):")
            user_input = input("> ").strip()

            if user_input.lower() == "exit":
                break

            try:
                size = int(user_input)
                if size <= 0:
                    print("Ukuran array harus lebih besar dari 0.")
                    continue
            except ValueError:
                print("Input tidak valid. Masukkan angka.")
                continue

            print(f"Apakah Anda ingin array diisi secara manual atau acak? (ketik 'manual' atau 'acak')")
            choice = input("> ").strip().lower()

            if choice == "manual":
                print(f"Masukkan {size} elemen array (pisahkan dengan spasi):")
                user_input = input("> ").strip()
                try:
                    arr = list(map(int, user_input.split()))
                    if len(arr) != size:
                        print(f"Error: Array harus berisi tepat {size} elemen.")
                        continue
                except ValueError:
                    print("Input tidak valid. Masukkan angka yang dipisahkan dengan spasi.")
                    continue
            elif choice == "acak":
                arr = [random.randint(1, 10000) for _ in range(size)]
                print(f"Array acak telah dibuat: {arr[:10]}... (menampilkan 10 elemen pertama)")
            else:
                print("Pilihan tidak valid. Coba lagi.")
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

            # Simpan hasil ke CSV
            writer.writerow([
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

    print(f"Hasil disimpan ke file '{csv_filename}'. Grafik runtime disimpan ke 'perbandingan_runtime.png'.")

if __name__ == "__main__":
    main()