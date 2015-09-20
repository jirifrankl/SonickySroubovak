#!/usr/bin/python

def zjisteni_rozsahu( *s): 
    print("Napiste velikost predmetu v cm.")
    #a=predmet,v=rychlost zvuku, fa=frekvence "a" predmetu, fb=frekvence "2a" , fc=frekvence "a/2" , d=rozdil frakvenci , k=d/10
    a=int(input())
    a=a/100
    v=346
    fa=v/a
    print("presna velikost vlny pri 20 C: ","%d"%fa)
    fb=fa*2
    fc=fa/2
    d=fb-fc
    k=d/10
    s=[]
    u=0
    print (__name__)
    while u!=11:
        s=s+[fb]
        fb=fb-k
        u=u+1
    i=0
    while i<11:
        print("%d"%(s)[i]) #tisk bez desetine casti
        (s)[i]=int ((s)[i]) #prevod na integer
        i=i+1
    return s


# pokud je modul spusten jako skript, vykonej testy
if __name__ == "__main__":
    err = False
    #Unitest
    n = input("Zadejte své jméno: ")
    s=[]
    sout=zjisteni_rozsahu(s)
    print (sout)
    print('Test prosel OK')
    print(__name__)
