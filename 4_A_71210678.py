#Ambil dan Balik Nama

def ambildanbalik (kalimat,mulai,akhir,TF):
    if (TF==True):
        huruf=(kalimat[mulai-1:akhir])
        hasil=(huruf[::-1])
        return hasil
    else:
        huruf=(kalimat[mulai-1:akhir])
        return huruf
    

print(ambildanbalik("abcdefg",2,4,True))
print(ambildanbalik("abcdefg",1,5,False))
print(ambildanbalik("Qwerty",3,4,True))
print(ambildanbalik("Qwerty",2,2,False))
