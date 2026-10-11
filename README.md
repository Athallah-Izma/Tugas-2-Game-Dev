# Tugas 2: Pemodelan Graph & Algoritma Greedy Best-First Search pada Tower of Hanoi

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python)
![Course](https://img.shields.io/badge/Course-Game%20Development-orange)
![Algorithm](https://img.shields.io/badge/Algorithm-Best--First%20Search%20(GBFS)-green)
![Topic](https://img.shields.io/badge/Topic-Graph%20State%20Space-purple)

Proyek ini disusun untuk memenuhi **Tugas 2 Mata Kuliah Game Development**. Repositori ini berisi implementasi pemodelan graph (*state space*) dan algoritma pencarian **Greedy Best-First Search (GBFS)** untuk menyelesaikan teka-teki klasik **Tower of Hanoi** (3 Piringan).

---

## Deskripsi Permasalahan

**Tower of Hanoi** adalah permainan teka-teki matematis yang terdiri dari tiga tiang (*pegs*), dinamakan tiang **A**, **B**, dan **C**, serta sejumlah piringan (*disks*) dengan ukuran yang berbeda-beda.

### Aturan Permainan:
1. Hanya satu piringan yang boleh dipindahkan dalam satu waktu.
2. Setiap perpindahan hanya mengambil piringan paling atas dari satu tiang dan meletakkannya di atas tiang lain.
3. **Piringan yang lebih besar tidak boleh diletakkan di atas piringan yang lebih kecil.**
4. **Kondisi Awal (*Start State*)**: Semua piringan bertumpuk di tiang **A**.
5. **Kondisi Akhir (*Goal State*)**: Semua piringan berhasil dipindahkan ke tiang **C** dengan urutan yang sama.

---

## Pemodelan Graph ($G = (V, E)$)

Permainan ini dimodelkan sebagai graf berarah (*directed graph*) ruang keadaan (*state space*):

$$G = (V, E)$$

### 1. Vertices / Nodes ($V$)
Setiap *vertex* $v \in V$ merepresentasikan konfigurasi posisi seluruh piringan pada saat tertentu.
Posisi piringan direpresentasikan sebagai sebuah *tuple*:

$$\text{State} = (p_0, p_1, p_2)$$

* $p_0$: Posisi tiang untuk piringan terkecil (Ukuran 0) $\in \{A, B, C\}$
* $p_1$: Posisi tiang untuk piringan sedang (Ukuran 1) $\in \{A, B, C\}$
* $p_2$: Posisi tiang untuk piringan terbesar (Ukuran 2) $\in \{A, B, C\}$

**Contoh State:**
* `('A', 'A', 'A')`: Seluruh piringan berada di tiang A (*Start State*).
* `('C', 'C', 'C')`: Seluruh piringan berada di tiang C (*Goal State*).

### 2. Edges ($E$)
Sebuah garis sambung (edge) $e = (u, v) \in E$ merepresentasikan transisi atau langkah perpindahan yang valid dari state $u$ ke state $v$ yang mematuhi hukum Tower of Hanoi.

---

## Algoritma Greedy Best-First Search (GBFS)

Algoritma **Greedy Best-First Search** mengeksplorasi ruang pencarian dengan selalu memperluas (*expanding*) simpul yang diperkirakan paling dekat dengan tujuan (*goal*).

### 1. Formulasi Fungsi Evaluasi

Pada Greedy Best-First Search, fungsi evaluasi $f(n)$ murni ditentukan oleh fungsi heuristik $h(n)$:

$$f(n) = h(n)$$

Di mana:
* $n$ = Node/state yang sedang dievaluasi.
* $h(n)$ = Nilai estimasi biaya heuristik dari simpul $n$ menuju simpul tujuan (*Goal*).
* $f(n)$ = Prioritas eksplorasi simpul.

Pada setiap iterasi, simpul berikutnya $n^*$ dipilih dari antrean terbuka (`OPEN` list) dengan nilai $f(n)$ minimum:

$$n^* = \arg \min_{n \in \text{OPEN}} f(n)$$

Dalam implementasi program, mekanisme ini direalisasikan dengan struktur data **Priority Queue** memanfaatkan modul bawaan Python `heapq`.

### 2. Desain Fungsi Heuristik $h(n)$

Fungsi heuristik dirancang dengan memberikan bobot eksponensial berdasarkan ukuran piringan:

$$h(n) = \sum_{i=0}^{k-1} \begin{cases} 0, & \text{jika } state[i] = goal[i] \\ 2^i, & \text{jika } state[i] \neq goal[i] \end{cases}$$

#### Alasan Desain Heuristik:
* Piringan yang berukuran lebih besar (indeks lebih tinggi) memiliki bobot penalti eksponensial ($2^i$).
* Bobot ini memaksa algoritma untuk memprioritaskan pemindahan piringan terbesar ke tiang target terlebih dahulu, menyerupai strategi optimal manusia dalam memecahkan Tower of Hanoi.

---

## Struktur Berkas

```text
Tugas-2-Game-Dev/
├── README.md               # Dokumentasi lengkap proyek & penjelasan akademis
└── tower_of_hanoi_bfs.py   # Implementasi source code algoritma Python
```

---

## Panduan Menjalankan Program

### Prasyarat
* Komputer telah terpasang **Python 3.8** atau versi yang lebih baru.
* Tidak memerlukan *library third-party* tambahan karena menggunakan pustaka standar Python (`heapq`).

### Langkah Eksekusi

1. **Clone repository ini:**
   ```bash
   git clone https://github.com/Athallah-Izma/Tugas-2-Game-Dev.git
   cd Tugas-2-Game-Dev
   ```

2. **Jalankan skrip Python:**
   ```bash
   python tower_of_hanoi_bfs.py
   ```

---

## Hasil Eksekusi & Solusi

Setelah skrip dijalankan, program akan menghasilkan lintasan perpindahan dari *Start State* menuju *Goal State* dalam 17 langkah:

```text
Mencari path penyelesaian Tower of Hanoi (Greedy Best-First Search)...

Jalur optimal ditemukan (17 Langkah):
Langkah ke-00: ('A', 'A', 'A')
Langkah ke-01: ('C', 'A', 'A')
Langkah ke-02: ('C', 'B', 'A')
Langkah ke-03: ('A', 'B', 'A')
Langkah ke-04: ('A', 'C', 'A')
Langkah ke-05: ('C', 'C', 'A')
Langkah ke-06: ('C', 'C', 'B')
Langkah ke-07: ('A', 'C', 'B')
Langkah ke-08: ('A', 'B', 'B')
Langkah ke-09: ('C', 'B', 'B')
Langkah ke-10: ('C', 'A', 'B')
Langkah ke-11: ('A', 'A', 'B')
Langkah ke-12: ('A', 'A', 'C')
Langkah ke-13: ('C', 'A', 'C')
Langkah ke-14: ('C', 'B', 'C')
Langkah ke-15: ('A', 'B', 'C')
Langkah ke-16: ('A', 'C', 'C')
Langkah ke-17: ('C', 'C', 'C')
```

---

## Analisis dan Kesimpulan

1. **Efektivitas Heuristik**: Desain fungsi heuristik berbobot $2^i$ berhasil memandu *Greedy Best-First Search* menavigasi ruang keadaan (*state space graph*) tanpa terjebak dalam siklus (*cycle*), dibantu oleh mekanisme `visited set`.
2. **Representasi Graf**: Model `state` berbasis *tuple* memungkinkan operasi *hashing* instan pada struktur data `set` dan `dict` (sebagai penunjuk `parent`), membuat proses *path reconstruction* menjadi efisien.
3. **Penyelesaian Masalah**: Program berhasil mencapai kondisi target `('C', 'C', 'C')` dengan aturan permainan yang terpenuhi secara valid pada setiap transisi.