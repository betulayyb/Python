a=1
b=1
fibonacci=[a,b]
sayi=int(input("Sayıyı giriniz:"))
for i in range(sayi):
    a,b=b,a+b
    fibonacci.append(b)
print(fibonacci)