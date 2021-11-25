#Ambil Huruf

def ambil_tengah(x, index_tambahan = 0):
    if (index_tambahan) :
        jumlah_huruf = len(x)
        hasil = (jumlah_huruf//2)
        return(x[hasil+index_tambahan])
    else:
        jumlah_huruf = len(x)
        hasil = (jumlah_huruf//2)
        return(x[hasil])

print(ambil_tengah("abcdefg",1))
print(ambil_tengah("abcdefg",2))
print(ambil_tengah("abcd"))