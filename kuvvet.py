hastanin_cinsiyeti=int(input("Hasta kadınsa 1'e, erkekse 2'ye basınız:"))
hastanin_yasi=int(input("Hasta cocuksa 11'e, gençse 22'ye, yaşlıysa 33'e basınız:"))

if (hastanin_cinsiyeti==1):
    kuvvet=int(input("1-15 arası kuvvet değeri seçiniz:"))
    if (hastanin_yasi==11):
        if (kuvvet>8):
            print("Motoru durdur veya yavaşlat.")
        else:
            print("çalışmaya devam et.")
    elif (hastanin_yasi==22):
        if (kuvvet>12):
            print("Motoru durdur veya yavaşla.")
        else:
            print("çalışmaya devam et.")
    elif (hastanin_yasi==33):
        if (kuvvet>10):
            print("Motoru durdur veya yavaşlat.")
        else:
            print("çalışmaya devam et.")

elif (hastanin_cinsiyeti == 2):
    kuvvet = int(input("1-15 arası kuvvet değeri seçiniz:"))
    if (hastanin_yasi == 11):
        if (kuvvet > 9):
            print("Motoru durdur veya yavaşla.")
        else:
            print("çalışmaya devam et.")
    elif (hastanin_yasi == 22):
        if (kuvvet > 13):
            print("Motoru durdur veya yavaşla.")
        else:
            print("çalışmaya devam et.")
    elif (hastanin_yasi == 33):
        if (kuvvet > 11):
            print("Motoru durdur veya yavaşla.")
        else:
            print("çalışmaya devam et.")
else:
    print("Böyle bir giriş bulunmamaktadır.")