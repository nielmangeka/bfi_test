nama = ["Budi" , "Anto"]
makanan = ["ayam", "bakso", "sate"]

hasilnya = []
for n in nama:
    for m in makanan:
        hasilnya.append(n + ' makan ' + m)

print(hasilnya)