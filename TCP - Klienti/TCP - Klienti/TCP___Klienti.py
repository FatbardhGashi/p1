import socket

serverName = 'localhost'
port = 12000
soketi = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
soketi.connect((serverName, port))

print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Projekti i parë nga lëmda Rrjeta Kompjuterike")
print("\tFIEK TCP Protokolli - Klienti")
print("\t\tFatbardh Gashi\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")
print("Metodat (funksionet) në dispozicion : \n")
print("IPADRESA")
print("NUMRIIPORTIT")
print("BASHTINGELLORE{Hapsirë}Fjala/Fjalia")
print("PRINTIMI{Hapsirë}Fjala/Fjalia")
print("EMRIIKOMPJUTERIT")
print("KOHA")
print("LOJA")
print("KONVERTIMI{Hapsirë}Opcioni{Hapsirë}Vlera")
print("\t*KilowattToHorsepower")
print("\t*HorsepowerToKilowatt")
print("\t*DegreesToRadians")
print("\t*RadiansToDegrees")
print("\t*GallonsToLiters")
print("\t*LitersToGallons\n")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\n")

hyrja = input("Zgjedhni një kërkesë(metodë)")

i=1
while(i==1):
    soketi.send(hyrja.encode())
    informata = soketi.recv(128).decode()
    print(informata)
    hyrja = input("Zgjedhni një kërkesë(metodë)")
    if(informata == "SHKYQU" and informata==""):
        i=2
print("Lidhja e klientit me serverin është shkyqur!")
socket.close()