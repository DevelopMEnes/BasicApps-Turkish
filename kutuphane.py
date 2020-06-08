''' Bu program temel bir kütüphane programıdır.\n

Program komut olarak sadece x tuşu için büyük-küçük harf duyarlıdır.\n
Diğer komutlar küçük harflerle işlemektedir.
'''


liste = [[1, "Toprak Ana"], [2, "Yaban"], [3, "Yılkı Atı"]]

print("Kütüphane kitap arama programına hoş geldiniz.\n",
      "Kitap aramak için numara veya isim giriniz.",
      "Kitap listesi için l tuşuna basınız.",
      "Kitap eklemek için e tuşuna basınız.",
      "Kitap çıkarmak için ç tuşuna basınız.",
      "Kitap adı değiştirmek için d tuşuna basınız.",
      "Kitap isimleri sadece sayılardan veya zaten var olan kitaplardan seçilemez.",
      "Çıkmak için x tuşuna basınız.\n", sep="\n")


def listede_ara_isim(isim):
    '''İsim listede varmı kontrol eder.'''
    for index in liste:
        if index[1] == isim:  # eğer isim bulunursa True dönecek.
            return True
    return False  # eğer isim bulunmazsa False dönecek.


def listeden_cikar():
    ''' öğe çıkarıldıktan sonra listede 0.indexlerde bulunan numaraları\n
        düzenleme işini yapar.
    '''
    for m_degeri in liste:
        m_degeri[0] = liste.index(m_degeri) + 1

    print("Kitap listeden çıkarıldı.")


while True:  # ana program döngüsü

    while not liste:  # eğer liste boşsa öğe eklemeniz gerekir.
        print("\nBu kütüphanede hiç kitap yok.")
        print("Kitap eklemek için lütfen e tuşuna basınız.")
        print("Programdan çıkmak için x tuşuna basınız.")
        x = input()
        if x == "e":
            x = input("Kitap ismi giriniz : ")
            liste.append([1, x])
            print("Kitap listeye kaydedildi.")
        elif x in ["x", "X"]:
            print("Programdan çıkılıyor...")
            break

    numara = input("\nKitap numarası giriniz : ")
    # Bu bilgiyi kitap aratma veya işlem gerçekleştirmede kullanacağız.

    if numara.isdigit() and not numara == "0":  # numara girildiyse kitap arar.

        for i in liste:

            if int(numara) == i[0]:
                print(i[0], "numaralı kitap :", i[1])
                break
            elif i == liste[-1]:
                print(
                    "Bu numaraya ait bir kitap bulunamadı. Lütfen uygun bir numara giriniz.")
                print("Kitap listesini görmek için l tuşuna basınız.")

    elif numara in ["x", "X"]:  # x girildiyse programdan çıkar.
        print("Programdan Çıkılıyor...")
        break

    elif numara == "l":
        for i in liste:
            print(i[0], ":", i[1])

    elif numara == "e":  # Kullanıcı listeye aynı isimde var olan  kitabı ekleyemez.
        x = input("Kitabı kaçıncı sıraya veya "
                  "hangi kitaptan sonraki sıraya eklemek istediğinizi giriniz.\n"
                  "Sona eklemek isterseniz s tuşuna basınız.")
        if x.isdigit() and not x == "0":  # sıra numarası alır.
            for i in liste:

                if int(x) == i[0]:
                    y = input("Kitap ismi giriniz : ")
                    if not listede_ara_isim(y):  # kitap listede yoksa ekler.
                        liste.insert(int(x) - 1, ([int(x), y]))
                        for n in range(int(x), len(liste)):
                            liste[n][0] = n + 1
                        print("Kitap listeye eklendi.")
                        break  # kitap varsa eklemez.
                    print(
                        "Eklemek istediğiniz adda bir kitap halihazırda bulunmaktadır.")
                    break
                print(  # kitap ismi bulunmazsa bu şekilde çıktı verir:
                    "Bu numaraya ait bir kitap bulunamadı. Lütfen uygun bir numara giriniz.")
                print("Kitap listesini görmek için l tuşuna basınız.")

        elif x == "s":  # kitabı sona ekler.
            y = input("Kitap ismi giriniz : ")
            if not listede_ara_isim(y):
                liste.append([len(liste) + 1, y])
                print("Kitap listeye eklendi.")
            else:
                print("Eklemek istediğiniz adda bir kitap halihazırda bulunmaktadır.")

        else:  # eğer numara veya "s" değilse kitap ismidir.
            # Öğeyi verilen isimdeki kitaptan bir sonraki sıraya ekler.
            for i in liste:
                if i[1] == x:
                    y = input("Kitap ismi giriniz : ")
                    if not listede_ara_isim(x):
                        liste.insert(liste.index(i) + 1,
                                     ([liste.index(i) + 2, y]))
                        print("Kitap listeye eklendi.")
                        for n in range(liste.index(i) + 1, len(liste)):
                            liste[n][0] = n + 1
                        break
                    else:
                        print(
                            "Eklemek istediğiniz adda bir kitap halihazırda bulunmaktadır.")
                        break
                elif i == liste[-1]:
                    print("Bu isimde bir kitap bulunamadı.",
                          "Kitap listesini görmek için l tuşuna basınız.", sep="\n")

    elif numara == "ç":  # öğe çıkarma işlemi yapar.
        x = input("Çıkartmak istediğiniz kitabın numarasını veya adını giriniz : ")
        if x.isdigit() and not x == "0":
            for i in liste:
                if i[0] == int(x):
                    del liste[int(x) - 1]
                    listeden_cikar()
                    break

                elif i == liste[-1]:
                    print("Bu numaraya ait bir kitap bulunamadı.")

        else:
            for k in liste:
                if k[1] == x:
                    del liste[liste.index(k)]
                    listeden_cikar()
                    break

            else:
                print("Bu isimde bir kitap bulunamadı.",
                      "Kitap listesini görmek için l tuşuna basınız.", sep="\n")

    elif numara == "d":  # Kitap ismi değiştirir.
        x = input(
            "Değiştirmek istediğiniz kitabın numarasını veya adını giriniz : ")
        if x.isdigit() and not x == "0":
            for i in liste:

                if int(x) == i[0]:
                    y = input("Kitap ismi giriniz : ")
                    if not listede_ara_isim(y):
                        liste[int(x) - 1] = [int(x), y]
                        print("Kitap ismi değiştirildi.")
                        break
                    else:
                        print(
                            "Değiştirmek istediğiniz adda bir kitap halihazırda bulunmaktadır.")
                elif i == liste[-1]:
                    print(
                        "Bu numaraya ait bir kitap bulunamadı. Lütfen uygun bir numara giriniz.")
                    print("Kitap listesini görmek için l tuşuna basınız.")
        else:
            for i in liste:
                if i[1] == x:
                    y = input("Kitap ismi giriniz : ")
                    if not listede_ara_isim(y):
                        i[1] = y
                        print("Kitap ismi değiştirildi.")
                        break
                    else:
                        print(
                            "Değiştirmek istediğiniz adda bir kitap halihazırda bulunmaktadır.")
                elif i == liste[-1]:
                    print("Bu isimde bir kitap bulunamadı.",
                          "Kitap listesini görmek için l tuşuna basınız.", sep="\n")
    else:  # Komutlar veya numara değilse isimdir. Verilen isimdeki kitabı yazar.
        for i in liste:
            if i[1] == numara:
                print(i[0], "numaralı kitap :", i[1])
                break
            elif i == liste[-1]:
                print("Bu isimde bir kitap bulunamadı.",
                      "Kitap listesini görmek için l tuşuna basınız.", sep="\n")
