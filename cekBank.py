#!/usr/bin/python

print("\n\nSKRIP CEK BANK\nAuthor by The Dark Knight\n============================================")

import requests

# Data Menu
pilihanmenu = [1, 2]

#Listing Menu
print('List Menu :\n###########################################\n 1.list bank (Guna Mengetahui Kode bank)\n 2.Ambil Data Bank (Kode Bank & No Rekening)\n ===========================================')

inputanUser = int(input('Masukkan Pilihan mu (Nomornya saja 1,2) : '))

if inputanUser in pilihanmenu:
    print("Pilihan mu ada !")
    
    if inputanUser == 1:
        # Jika Opsi 1
        # Endpoint API
        url = 'https://api-rekening.lfourr.com/listBank'
        # Kirim permintaan GET
        response = requests.get(url)
        dataBank = response.json()
        print(dataBank['msg']+'\n')
        print('=== list Bank ===')
        for data in dataBank['data']:
            # print(data)
            # function untuk membongkar file json
            print("Kode Bank "+ data['kodeBank'])
            print("Kode Bank "+ data['namaBank'])
            print("\n")
        
    elif inputanUser == 2:
        # Jika Opsi 2
        pass
    else:
        # Jika tidak ada di dalam opsi
        pass

else:
    print("Pilihan mu tidak ada")
