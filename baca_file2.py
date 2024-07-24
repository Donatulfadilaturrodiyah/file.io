# buka file 
file_puisi = open ("pantun.txt", "r")

#baca isi file 
puisi = file_puisi.readlines()

#cetal isi file dengan perulangan 
for teks in puisi:
    print (teks)

#tutup file
file_puisi.close()