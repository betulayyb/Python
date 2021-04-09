"""and operatörü
true true --> true
true false --> false
true false --> false
false false --> false
"""
print(1<2 and "Murat"=="Murat")
print(2>3 and "Murat"=="Murat")
print(2==2 and 3.14<2.54 and "Elma"!="Armut")

""" or operatörü
true true --> true
true false --> true
false true --> true
false false --> false 
"""
print(1<2 or "Murat"=="Murat")
print(2>3 or "Murat"=="Murat")
print(2==2 or 3.14<2.54 or "Elma"!="Armut")
""" Not operatörü
true --> false
false --> true
"""
print(not 2==2)
print(not "python" == "pyho")

"""
operatörlerin beraber kullanılması

"""
not (2.14 > 3.49 or ( 2 != 2 and "Murat" == "Murat"))
"Araba" < "Zula" and ( "Bebek" < "Çoçuk" or (not 14 ))
