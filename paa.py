def hitung_ratio(item):
    for nama, nilai, berat in item:
        ratio = nilai / berat
        print(f"Nama: {nama}, Nilai: {nilai}, Berat: {berat}, Rasio: {ratio:.2f}")

def knapsack_greedy_01(item, kapasitas):
    item_sorted = sorted(item, key=lambda x: x[1] / x[2], reverse=True)
    item_terpilih = []
    total_nilai = 0
    total_berat = 0

    for nama, nilai, berat in item_sorted:
        if total_berat + berat <= kapasitas:
            item_terpilih.append((nama, nilai, berat))
            total_nilai += nilai
            total_berat += berat

    return item_terpilih, total_nilai, total_berat

def knapsack_greedy_dynamic(item, kapasitas):
    n = len(item)
    dp = [[0] * (kapasitas + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        nama, nilai, berat = item[i - 1]
        for w in range(kapasitas + 1):
            if berat <= w:
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - berat] + nilai)
            else:
                dp[i][w] = dp[i - 1][w]

    total_nilai = dp[n][kapasitas]
    total_berat = 0
    item_terpilih = []

    w = kapasitas
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            nama, nilai, berat = item[i - 1]
            item_terpilih.append((nama, nilai, berat))
            total_berat += berat
            w -= berat

    return item_terpilih, total_nilai, total_berat

def main():
    item = [
        ("Laptop", 1000, 30),
        ("Buku", 500, 20),
        ("Pensil", 100, 1),
        ("Kamera", 800, 24),
        ("Headphone", 300, 15),
        ("Earphone", 200, 10),
        ("Randy", 400, 5)
    ]
    kapasitas = 50

    print("Rasio Nilai terhadap Berat:")
    hitung_ratio(item)

    item_terpilih, total_nilai, total_berat = knapsack_greedy_01(item, kapasitas)
    print("\nItem yang dipilih:")
    for nama, nilai, berat in item_terpilih:
        print(f"Nama: {nama}, Nilai: {nilai}, Berat: {berat}")
    print(f"\nTotal Nilai: {total_nilai}, Total Berat: {total_berat}")

    # Test with dynamic programming approach
    print("\n--- Dynamic Programming Approach ---")
    item_terpilih_dp, total_nilai_dp, total_berat_dp = knapsack_greedy_dynamic(item, kapasitas)
    print("Item yang dipilih:")
    for nama, nilai, berat in item_terpilih_dp:
        print(f"Nama: {nama}, Nilai: {nilai}, Berat: {berat}")
    print(f"\nTotal Nilai: {total_nilai_dp}, Total Berat: {total_berat_dp}")

if __name__ == "__main__":
    main()