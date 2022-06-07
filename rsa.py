import random

from Crypto.PublicKey import RSA
new_key = RSA.generate(1024, e=65537)
#To idiwtiko kleidi se PEM morfi
private_key = new_key.exportKey("PEM")

#To dhmosio kleidi se PEM morfi
public_key = new_key.publickey().exportKey("PEM")
print(private_key)
#epilogh 2 sunexomenwn thesewn sto idiwtiko kleidi
randNum = random.randint(31,len(private_key))
#print("The length of private key is:",len(private_key))
#pairnoyme 2 tyxaious xarakthres gia na tous valoume sto idiwtiko kleidi
rand1 = random.randint(0,127)
rand2 = random.randint(0,127)
#allagh twn 2 sunexomenwn tyxaiwn xarakthrwn me tous neous pou eftiaksa
new_key = private_key[1:randNum-1]+bytes(chr(rand1).encode("utf-8"))
new_key = new_key+bytes(chr(rand2).encode("utf-8"))
new_key = new_key + private_key[randNum+1:len(private_key)]
fd = open("private_key.pem", "wb")
fd.write(new_key)
fd.close()
print(public_key)
fd = open("public_key.pem", "wb")
fd.write(public_key)
fd.close()
print("Private_key changed at indexes",randNum,randNum+1, "with characters",chr(rand1),chr(rand2))
print()
print("Changed key :")
print(new_key)
