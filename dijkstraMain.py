import sys
import time
import math

print("Mettez le nombre de la question : ")
questionNo = int(input())

if(questionNo == 1):
    nombresList = []
    n = int(input("Mettez le nombre d'éléments désiré dans le liste : "))

    for i in range(0, n):
        ele = int(input())
        nombresList.append(ele)

    count = 0
    pgcdNombre = 0

    def pgcd(nombres):
        global count
        global pgcdNombre
        nombres = nombresList

        for i in range(1, (min(nombres) + 2)):
            if(count == len(nombres)):
                pgcdNombre = i-1
            count = 0
            for j in range(0, len(nombres)):
                if(nombres[j] % i == 0):
                    count += 1

        print("PGCD de ce liste est " + str(pgcdNombre))

    pgcd(nombresList)

if(questionNo == 2):
    nombresList = []
    n = int(input("Mettez le nombre d'éléments désiré dans le liste : "))

    for i in range(0, n):
        ele = int(input())
        nombresList.append(ele)

    count = 0
    ppmcNombre = 0
    addOne = -1

    def ppmc(nombres):
        global count
        global ppmcNombre
        global addOne
        flag = 1
        nombres = nombresList
        while(flag == 1):
            count = 0
            addOne += 1
            for i in range(0, len(nombres)):
                if((max(nombres) + addOne) % nombres[i] == 0):
                    count += 1
                if(count == len(nombres)):
                    flag = 0
                    ppmcNombre = max(nombres) + addOne
        print("PPMC de ce liste est " + str(ppmcNombre))

    ppmc(nombresList)

if(questionNo == 3):
    nombresList = []
    print("Mettez deux nombres à comparer : ")

    for i in range(0, 2):
        ele = int(input())
        nombresList.append(ele)

    count = 0
    pgcdNombre = 0
    
    def premierEntreEux(valeur1, valeur2):
        global count
        global pgcdNombre
        nombres = nombresList
        valeur1 = nombres[0]
        valeur2 = nombres[1]
        for i in range(1, (min(nombres) + 2)):
            if(count == len(nombres)):
                pgcdNombre = i-1
            count = 0
            for j in range(0, len(nombres)):
                if(nombres[j] % i == 0):
                    count += 1
        if(pgcdNombre == 1):
            print("Ces deux nombres sont premiers entre eux.")
        else:
            print("Ces deux nombres ne sont pas premiers entre eux.")

    premierEntreEux(nombresList[0], nombresList[1])

if(questionNo == 4):
    print("Mettez un nombre positif: ")

    ele = int(input())
    count = 0
    
    def estPremier(valeur):
        global count

        if(valeur == 0 or valeur == 1):
                print("Ce nombre n'est pas premier.")

        for i in range(2, int(valeur/2)):
            if(valeur % i == 0):
                count = 1
                break

        if(count == 0):
            print("Ce nombre est premier.")
        else:
            print("Ce nombre n'est pas premier.")

    estPremier(ele)

if(questionNo == 5):
    start = time.time()
    end = time.time()

    print("La durée d'exécution de ce programme est : ",
      (end-start) * 10**3, "ms")

if(questionNo == 6):
    print("Mettez un nombre positif: ")

    ele = int(input())
    count = 0

    def estPremierHalf(valeur):
        global count

        if(valeur == 0 or valeur == 1):
                print("Ce nombre n'est pas premier.")

        for i in range(2, int(valeur/2)):
            if(valeur % i == 0):
                count = 1

        if(count == 0):
            print("Ce nombre est premier.")
        else:
            print("Ce nombre n'est pas premier.")

    def estPremierSqrt(valeur):
        global count

        if(valeur == 0 or valeur == 1):
                print("Ce nombre n'est pas premier.")

        for i in range(2, int(math.sqrt(valeur))):
            if(valeur % i == 0):
                count = 1

        if(count == 0):
            print("Ce nombre est premier.")
        else:
            print("Ce nombre n'est pas premier.")

    startHalf = time.time()
    estPremierHalf(ele)
    endHalf = time.time()

    startSqrt = time.time()
    estPremierSqrt(ele)
    endSqrt = time.time()

    print("La durée d'exécution de programme non amélioré est : ",
      (endHalf-startHalf) * 10**3, "ms")
    print("La durée d'exécution de programme amélioré est : ",
      (endSqrt-startSqrt) * 10**3, "ms")

