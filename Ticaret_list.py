from tkinter import N        #numpy


urun_liste = [['SIRA', 'URUN', 'ADET', 'FIYAT']]


def topla(x) -> int:
    toplam = 0
    if x == 1:
        for i in urun_liste[1:]:
            toplam += int(i[2])
    elif x == 2:
        for i in urun_liste[1:]:
            toplam += int(i[3])
    return toplam


def urun_ekle():
    ad = input('URUN ADI GİRİNİZ: ')
    adet = input('URUN ADEDİ GİRİNİZ: ')
    fiyat = input('URUN FİYATI GİRİNİZ: ')
    urun = [f'{len(urun_liste)}.', ad, adet, fiyat]
    urun_liste.append(urun)
    kontrol = input("URUN EKLENDİ. TEKRAR EKLEMEK İÇİN D'YE ÇIKIŞ İÇİN C'YE BASINIZ.")
    if kontrol.lower() == "d":
        pass
    elif kontrol.lower() == "c":
        exit()
    else:
        print('Hatalı girdi. Programdan cıkılıyor.')
        exit()


def urun_listele():
    sutun_genislik = max(len(eleman) for urun in urun_liste for eleman in urun)
    for urun in urun_liste:
        index = urun_liste.index(urun)
        if index == 0:
            print()
        urun_txt = "".join(eleman.ljust(sutun_genislik) for eleman in urun)
        print(urun_txt)
    print(f'TOPLAM ÜRÜN ADEDİ: {topla(1)}')
    print(f'TOPLAM TUTAR: {topla(2)}')


def main():
    secenek = input(" ÜRÜN KAYIT İÇİN 1'E \n ÜRÜNLERİ LİSTELEMEK İÇİN 2'YE \n ÇIKIŞ İÇİN C'YE BASINIZ :")
    if secenek == "1":
        urun_ekle()
    elif secenek == "2":
        urun_listele()
    elif secenek.lower() == "c":
        print(f'iyi günler')
        exit()
    else:
        print('Hatalı girdi. Tekrar deneyin.')
    return main()


if __name__ == "__main__":
    main()