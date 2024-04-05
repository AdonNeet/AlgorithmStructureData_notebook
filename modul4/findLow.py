def cariTerkecil(kumpulan):
    n = len(kumpulan)
    # Anggap item pertama adalah yang terkecil
    terkecil = kumpulan[0]
    # Bandingkan apakah item lain lebih kecil
    for i in range(1, n):
        if kumpulan[i] < terkecil:
            terkecil = kumpulan[i]
    return terkecil

