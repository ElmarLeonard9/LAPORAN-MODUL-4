    #Identitas
def non_return_func(praktikan1, praktikan2):
    print(f"{praktikan1} - 21120119140120 dan {praktikan2} - 21120119140145")
    print('Shift 2 - Kelompok 53\n\n')

   #Pemanggilan identitas
non_return_func("Abimanyu Putro Yulianto", "Elmar Leonard")


    #Judul
print('---------E&A Jacket---------\n\n')

    #pilihan jenis
def non_return_func(jenis1, jenis2, jenis3):
    print(f" Daftar jenis jaket yang kami jual: \n 1. {jenis1} - Rp.350000 \n 2. {jenis2} - Rp.250000 \n 3. {jenis3} - Rp.450000")

    #Pemanggilan pilihan jenis
non_return_func("Jaket Jeans", "Jaket Hoodie", "Jaket Kulit")


    #memilih jenis
x = float(input('Pilih jenis jaket apa yang anda inginkan = '))

if x ==1:
    print('-----------------------------------------------------')
    print('\nAnda telah memilih Jaket Jeans dengan harga Rp.350000\n')
    print('-----------------------------------------------------')
    print('Daftar ukuran jaket yang tersedia')
    print('1. M')
    print('2. L')
    print('3. XL')
    print('4. XXL')
    y = float(input('Pilih ukuran jaket apa yang anda inginkan ='))
    if y ==1:
        print('-----------------------------------------------------')
        print('\nAnda memilih ukuran M\n')
        print('-----------------------------------------------------')
    elif y ==2:
        print('-----------------------------------------------------')
        print('\nMaaf stok ukuran yang anda pilih sudah habis\n')
        print('-----------------------------------------------------')
    elif y==3:
        print('-----------------------------------------------------')
        print('\nAnda memilih ukuran XL\n')
        print('-----------------------------------------------------')
    elif y==4:
        print('\nAnda memilih ukuran XXL\n')
    else:
        item = ['\n''!!Anda telah memilih inputan yang salah!!','pilihan yang tersedia hanya:','1','2','3']
        for ukuran in item:
            print(ukuran)

elif x ==2:
    print('-----------------------------------------------------')
    print('\nAnda telah memilih Jaket Hoodie dengan harga Rp.250000\n')
    print('-----------------------------------------------------')
    print('Daftar ukuran jaket yang tersedia')
    print('1. M')
    print('2. L')
    print('3. XL')
    print('4. XXL')
    y = float(input('Pilih ukuran jaket apa yang anda inginkan ='))
    if y ==1:
        print('-----------------------------------------------------')
        print('\nAnda memilih ukuran M')
        print('-----------------------------------------------------')
    elif y ==2:
        print('-----------------------------------------------------')
        print('\nMaaf stok ukuran yang anda pilih sudah habis\n')
        print('-----------------------------------------------------')
    elif y==3:
        print('-----------------------------------------------------')
        print('\nAnda memilih ukuran XL\n')
        print('-----------------------------------------------------')
    elif y==4:
        print('-----------------------------------------------------')
        print('\nAnda memilih ukuran XXL\n')
        print('-----------------------------------------------------')
    else:
        item = ['\n''!!Anda telah memilih inputan yang salah!!','pilihan yang tersedia hanya:','1','2','3']
        for ukuran in item:
            print(ukuran)
elif x ==3:
    print('-----------------------------------------------------')
    print('\nAnda telah memilih Jaket Kulit dengan harga Rp.450000\n')
    print('-----------------------------------------------------')
    print('Daftar ukuran jaket yang tersedia')
    print('1. M')
    print('2. L')
    print('3. XL')
    y = float(input('Pilih ukuran jaket apa yang anda inginkan ='))
    if y ==1:
        print('-----------------------------------------------------')
        print('\nMaaf stok ukuran yang anda pilih sudah habis\n')
        print('-----------------------------------------------------')
    elif y ==2:
        print('-----------------------------------------------------')
        print('\nMaaf stok ukuran yang anda pilih sudah habis\n')
        print('-----------------------------------------------------')
    elif y==3:
        print('-----------------------------------------------------')
        print('\nAnda memilih ukuran XL\n')
        print('-----------------------------------------------------')
    else:
        item = ['\n''!!Anda telah memilih inputan yang salah!!','pilihan yang tersedia hanya:','1','2','3']
        for ukuran in item:
            print(ukuran)
else:
    item = ['\n''!!Anda telah memilih inputan yang salah!!','pilihan yang tersedia hanya:','1','2','3']
    for jenis in item:
        print(jenis)
        #pilihan ukuran









