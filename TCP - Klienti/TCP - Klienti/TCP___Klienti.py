import socket
import sys
import io

host='localhost'
port=11000

socketClient = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
socketClient.connect((host,port))
print("******************************************************************\n")
print("Projekti i parë nga lënda Rrjeta Kompjuterike")
print("\tFIEK TCP Protokolli - KLIENTI")
print("\t\tFatbardh Gashi\n")
print("******************************************************************\n")
print("Metodat (funksionet) në dispozicion : \n")
print("IPADRESA")
print("NUMRIIPORTIT")
print("BASHTINGELLORE{Hapsirë}Teksti")
print("PRINTIMI{Hapsirë}Teksti")
print("EMRIIKOMPJUTERIT")
print("KOHA")
print("LOJA")
print("KONVERTIMI{Hapsirë}Opconi{Hapsirë}Numri")
print("\t*KilowattToHorsepower")
print("\t*HorsepowerToKilowatt")
print("\t*DegreesToRadians")
print("\t*RadiansToDegrees")
print("\t*GallonsToLiters")
print("\t*LitersToGallons\n")
print("******************************************************************\n")

hyrja=input("Zgjedhni nje komande>>> ")
while((hyrja != "") and (hyrja !="SHKYQU")):
        socketClient.send(hyrja.encode())                
        informata = socketClient.recv(128).decode()

        print(informata)
        hyrja = input("Zgjedhni nje komande >>> ")

socketClient.close();
