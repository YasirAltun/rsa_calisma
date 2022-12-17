from math import gcd
from random import randint
primeNUmbers=[ 101, 103, 107, 109, 113, 127, 131, 137, 139, 149] #asal olmaları gerekiyor
s= len(primeNUmbers)
text= input(" şifrelenmesini istediğiniz metni giriniz: ")

list_n=list()
list_d=list()
list_e=list()
encryptedTextWithNumbers=list()
check=0
length=len(text)
while(check<length):
    rand1=randint(0,s-1)
    while 10:
        rand2=randint(0,s-1)
        if rand1!=rand2:
            break
    p=primeNUmbers[rand1]
    q=primeNUmbers[rand2]

    list_n.append(p*q)
    totient=(q-1)*(p-1) #totient  fonksiyonunun formülasyonu

    liste=list()
    #public key üreiliyor burda
    for t in range (2, totient) :
        if 1 == gcd((p*q), t) and 1 == gcd (totient, t): #gcd = ebob
            liste.append (t)

    rand = randint (0, len (liste) - 1)
    e = liste [rand]
    list_e.append (e)

    entry = text [check]
    encryptedTextWithNumbers.append((ord(entry) ** e) % (p * q)) #cipher textin üretildiği yer c=m^e mod n

    d = 2
    while 10:
        if 1 == (e * d)%totient:
            list_d.append(d)
            break
        d+=1
    check+=1

encryptedTextWithChars=list()
for i in encryptedTextWithNumbers:
    encryptedTextWithChars.append(chr(i))

print("\nşifrelenmiş metin: ", end="")
for i in encryptedTextWithChars:
    print(i, end="")

decrytedText=list()
for i in range(0,len(encryptedTextWithNumbers)):
    decrytedText.append(chr(encryptedTextWithNumbers[i]**list_d[i]%list_n[i]))

print("\n\nDeşifrelenmiş metin: ", end="")
for i in decrytedText:
    print(i,end="")

