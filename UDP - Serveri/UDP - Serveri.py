import socket
import sys
from _thread import *
import random
import datetime
import math 

host = 'localhost' 
port = 12000
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
try :
    serverSocket.bind((host,port))
    
except socket.error:
    print("Nuk u arrit lidhja me klientin")
    sys.exit()

print("******************************************************************\n")
print("Projekti i parë nga lënda Rrjeta Kompjuterike")
print("\tFIEK UDP Protokolli - SERVERI")
print("\t\tFatbardh Gashi\n")
print("******************************************************************\n")

def IPADRESA():
    return socket.gethostbyname(EMRIIKOMPJUTERIT())

def BASHTINGELLORE(Teksti):
    bashtingellore = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 
               'V', 'X', 'Z', 'b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'n', 'p', 'q',
              'r', 's', 't', 'v', 'x', 'z']
    count = 0
    for i in bashtingellore:
        for j in Teksti:
            if i==j:
                count = count+1
    return count

def PRINTIMI(Teksti):
    Teksti = (str(Teksti).strip())
    return Teksti

    return numbers

def EMRIIKOMPJUTERIT():
    return socket.gethostname()

def KOHA():
    from time import gmtime, strftime
    KohaAktuale = strftime("%d.%m.%Y %I:%M:%S %p")
    return KohaAktuale

def LOJA():
    NumratRandom = ""
    for k in range(1,8):
        NrRandom = random.randint(1,49)
        NumratRandom += str(NrRandom) + " "
    return NumratRandom

def FIBONACCI(Numri):
    a = 1 
    b = 1
    for i in range(2,Numri):
        f = a + b;
        a = b
        b = f;
    return f

def KONVERTIMI(opcioni, Numri):
    if opcioni == "KilowattToHorsepower":
        Rezultati = Numri*1.34102
    elif opcioni == "HorsepowerToKilowatt":
        Rezultati = Numri/(1.34102)
    elif opcioni == "DegreeToRadians":
        Rezultati = Numri*0.0174533
    elif opcioni == "RadiansToDegree":
        Rezultati = Numri/(0.0174533)
    elif opcioni =="GallonsToLiters":
        Rezultati = Numri*3.78541
    elif opcioni =="LitersToGallons":
        Rezultati = Numri/(3.78541)
    else:
        Rezultati= "Gabim! Zgjedhni një nga opcionet e mësipërme!\nSigurohuni që ta shkruani drejtë!"
    return Rezultati

# ```Metodat shtesë
def TEOREMAKOSINUS(a, b, C):
    c = math.sqrt(math.pow(a,2) + math.pow(b,2) - 2*a*b*math.cos(C))
    return c

def GJEJDITEN(numri):
    now = datetime.datetime.now()

    if((now.weekday() + numri) % 7 == 0):
        return "Monday"
    if((now.weekday() + numri) % 7 == 1):
        return "Tuesday"
    if((now.weekday() + numri) % 7 == 2):
        return "Wednesday"
    if((now.weekday() + numri) % 7 == 3):
        return "Thursday"
    if((now.weekday() + numri) % 7 == 4):
        return "Friday"
    if((now.weekday() + numri) % 7 == 5):
        return "Saturday"
    if((now.weekday() + numri) % 7 == 6):
        return "Sunday"

def ClientThread(input, address):
    try:
        informata = input.decode() 
    except socket.error:
        print("Ka ndodhur nje problem!")   


    vargu = str(informata).rsplit(" ")
    rreshti = ""
    gjatesia_vargu = len(vargu)
    for fjala in range(1, gjatesia_vargu):
        rreshti += vargu[fjala]
        if(fjala != gjatesia_vargu):
            rreshti += " "
    if not informata:
        return
    elif(vargu[0]=="IPADRESA"):
            informata = "IP Adresa e klientit është : " + IPADRESA()
    elif(vargu[0]=="NUMRIIPORTIT"):
            informata = "Klienti është duke përdorur portin " + str(address[1])
    elif(vargu[0]=="BASHTINGELLORE"):
            informata = "Teksti i pranuar ka : " + str(BASHTINGELLORE(rreshti)) + " bashtingëllore!"    #  ``` Teksti i pranuar ka x bashtingëllore ```
    elif(vargu[0]=="PRINTIMI"):
            informata = "Teksti që keni shtypur është : " + str(PRINTIMI(rreshti))
    elif(vargu[0]=="KOHA"):
            informata = KOHA()
    elif(vargu[0]=="EMRIIKOMPJUTERIT"):
        try:
            informata = "Emri i kompjuterit është : " + EMRIIKOMPJUTERIT()
        except socket.error:
            informata = "Emri i kompjuterit nuk mund të gjendet!"
    elif(vargu[0]=="LOJA"):
            informata = "Shtatë numrat e gjeneruar rastësisht prej 1-49 janë : " + LOJA()
    elif(vargu[0]=="FIBONACCI"):
            rreshti = int(vargu[1])
            informata = str(FIBONACCI(rreshti))
    elif(vargu[0]=="KONVERTIMI"):
            try:
                numri = float(vargu[2])
            except socket.error:
                return "Gabim!!!"
            informata = str(KONVERTIMI(vargu[1], numri))
    elif(vargu[0]=="TEOREMAKOSINUS"):
            a = int(vargu[1])
            b = int(vargu[2])
            C = int(vargu[3])
            informata = "Teorema e kosinusit : c=" + str(TEOREMAKOSINUS(a,b,C))
    elif(vargu[0]=="GJEJDITEN"):
            rreshti = int(vargu[1])
            informata = str(GJEJDITEN(rreshti))
    else:
        informata="Serveri nuk mund ti pergjigjet kesaj kerkese"
    serverSocket.sendto(informata.encode(),address)


while 1:

        informata, address=serverSocket.recvfrom(128)
        print('Serveri eshte lidhur me klientin me Ip Adrese ' + address[0] + ' ,ne portin ' + str(address[1]))
        start_new_thread(ClientThread,(informata, address,))

serverSocket.close()