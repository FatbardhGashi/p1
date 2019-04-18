import socket 

host='localhost'
port=12000

socketClient=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

print("******************************************************************\n")
print("Projekti i parë nga lënda Rrjeta Kompjuterike")
print("\tFIEK UDP Protokolli - KLIENTI")
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
print("FIBONACCI{Hapsirë}Numri")
print("KONVERTIMI{Hapsirë}Opcioni{Hapsirë}Numri")
print("\t*KilowattToHorsepower")
print("\t*HorsepowerToKilowatt")
print("\t*DegreesToRadians")
print("\t*RadiansToDegrees")
print("\t*GallonsToLiters")
print("\t*LitersToGallons\n")
print("******************************************************************\n")
print("Metodat shtesë : \n")
print("TEOREMAKOSINUS{Hapsirë}(Vlera e brinjës a){Hapsirë}(Vlera e brinjës b){Hapsirë}(Vlera e këndit C)")
print("GJEJDITEN{Hapsirë}(Numri-Pas sa dite)\n")
print("******************************************************************\n")

hyrja=input("Zgjedhni nje komande >>> ")
while((hyrja != "") and (hyrja !="SHKYQU")):

    socketClient.sendto(hyrja.encode(),(host,port))
    informata=socketClient.recv(128)
    print(informata)
    hyrja=input("Jepni kerkesen tuaj : ")

socketClient.close()