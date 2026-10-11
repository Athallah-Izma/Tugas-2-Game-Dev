import heapq

# ==========================================
# TOWER OF HANOI - GREEDY BEST-FIRST SEARCH
# ==========================================
# File ini mendemonstrasikan penyelesaian game puzzle Tower of Hanoi 
# menggunakan Algoritma Graph dan Best-First Search sesuai materi.
# Cocok untuk di-push ke GitHub sebagai portofolio implementasi algoritma.

def get_valid_moves(state):
    """
    Fungsi untuk mencari EDGE atau langkah pergerakan yang valid.
    Merepresentasikan transisi state pada Graph: G = (V, E)
    di mana V (Vertex) adalah tuple posisi piringan saat ini.
    """
    moves = []
    pegs = ['A', 'B', 'C']
    
    # Mencari piringan teratas di masing-masing tiang
    # (Index 0 = Kecil, 1 = Sedang, 2 = Besar)
    top_disks = {'A': -1, 'B': -1, 'C': -1}
    for disk_size, peg in enumerate(state):
        if top_disks[peg] == -1:
            top_disks[peg] = disk_size
            
    # Mengevaluasi kemungkinan pergerakan (transisi State)
    for source_peg in pegs:
        if top_disks[source_peg] != -1: # Jika tiang memiliki piringan
            disk_to_move = top_disks[source_peg]
            
            for target_peg in pegs:
                if source_peg != target_peg:
                    # Aturan Game: Piringan hanya bisa pindah ke tiang kosong 
                    # atau diletakkan di atas piringan yang lebih besar
                    if top_disks[target_peg] == -1 or top_disks[target_peg] > disk_to_move:
                        # Membuat Vertex (Node) baru
                        new_state = list(state)
                        new_state[disk_to_move] = target_peg
                        moves.append(tuple(new_state))
    return moves

def heuristic(state, goal):
    """
    Fungsi Heuristik h(n)
    Memberikan estimasi biaya jarak dari state menuju goal.
    
    Logika: 
    Piringan yang lebih besar diberikan beban prioritas (2^i) lebih tinggi.
    Hal ini memastikan algoritma mencari jalur yang memprioritaskan pemindahan 
    piringan paling besar (yang paling sulit dipindah) ke tiang tujuan (C) secepat mungkin.
    """
    h = 0
    for i in range(len(state)):
        if state[i] != goal[i]:
            h += 2 ** i 
    return h

def reconstruct_path(parent, current):
    """
    Fungsi untuk membangun kembali path dari state akhir (Goal) 
    mundur hingga ke titik awal (Start).
    """
    path = []
    while current is not None:
        path.append(current)
        current = parent[current]
    path.reverse() # Balik urutan: Start -> Goal
    return path

def best_first_search(start, goal):
    """
    Algoritma Greedy Best-First Search
    Berdasarkan rumus prioritas: f(n) = h(n)
    
    Pemilihan rute selanjutnya:
    n* = arg min_{n in OPEN} f(n)
    (Mengambil node dengan estimasi biaya h(n) yang paling kecil).
    """
    # Priority Queue OPEN list.
    # Menyimpan node dengan tuple (f(n), node_state)
    open_list = []
    heapq.heappush(open_list, (heuristic(start, goal), start))
    
    # VISITED list untuk menyimpan state yang sudah pernah dikunjungi
    visited = set()
    
    # Dictionary untuk menyimpan hierarki pergerakan
    parent = {start: None}
    
    while open_list:
        # Mengambil node dengan f(n) terkecil (n*)
        f, current = heapq.heappop(open_list)
        
        # Jika Goal (tujuan) ditemukan
        if current == goal:
            return reconstruct_path(parent, current)
            
        # Jika node sudah dieksplorasi, skip (menghindari infinite loop)
        if current in visited:
            continue
            
        visited.add(current)
        
        # Eksplorasi node anak / successor (tetangga valid)
        for neighbor in get_valid_moves(current):
            if neighbor not in visited:
                if neighbor not in parent: # Simpan jalur parent
                    parent[neighbor] = current
                
                # Menghitung estimasi heuristik node baru
                h = heuristic(neighbor, goal)
                
                # Memasukkan ke dalam antrian OPEN list
                heapq.heappush(open_list, (h, neighbor))
                
    return None # Jika tidak ada solusi ditemukan

if __name__ == "__main__":
    # Inisialisasi awal (Start State):
    # Struktur Tuple: (Posisi Disk Kecil, Posisi Disk Sedang, Posisi Disk Besar)
    start_state = ('A', 'A', 'A')
    
    # Kondisi kemenangan (Goal State):
    # Sesuai gambar, memindahkan semua piringan ke tiang C
    goal_state = ('C', 'C', 'C')
    
    print("Mencari path penyelesaian Tower of Hanoi (Greedy Best-First Search)...")
    path = best_first_search(start_state, goal_state)
    
    if path:
        print(f"\nJalur optimal ditemukan ({len(path) - 1} Langkah):")
        for step, state in enumerate(path):
            print(f"Langkah ke-{step:02d}: {state}")
    else:
        print("\nPath tidak ditemukan.")