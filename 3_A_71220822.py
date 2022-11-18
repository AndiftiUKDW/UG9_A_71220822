panjang = int(input("Masukan panjang : "))
lebar = int(input("Masukan lebar : "))
jari = int(input("Masukan jari-jari : "))
luas1 = panjang*lebar
luas2 = 3.14*jari*jari/2
Kaleng = round((luas1+luas2)/15)
print("Area tersebut membutuhkan",Kaleng,"kaleng cat")