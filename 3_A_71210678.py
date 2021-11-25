#Menghitung data yang dihapus
kalimat = input("Masukkan Kalimat: ")
start = int(input("Masukkan Index Start: "))
stop = int(input("Masukkan Index Stop: "))

def hitung_hapus():
    jumlah_awal=len(kalimat)
    jumlah_akhir=len(kalimat[start:stop+1])
    persen = (jumlah_akhir/jumlah_awal)* 100
    return persen

print (hitung_hapus())
