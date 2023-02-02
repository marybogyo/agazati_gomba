from Gomba import Gomba
gomba_lista = []
def beolvas():
    fajl = open("gombak_jav.txt", "r", encoding="utf-8")
    fajl.readline()
    sorok = fajl.readlines()
    fajl.close()

    i = 0
    while i < len(sorok):
        sor = sorok[i].strip().split("@")
        gomba_lista.append(Gomba(sor))
        i += 1

def gomak_szama():
    return len(gomba_lista)

def papsapka():
    i = 0
    neve = ""

    while i < len(gomba_lista) and neve == "":
        if gomba_lista[i].nemzettseg == "papsapkagombák ":
            neve = gomba_lista[i].nev

        i += 1

    return neve

def tinoru():
    i = 0
    db = 0

    while i < len(gomba_lista):
        if gomba_lista[i].nemzettseg == "tinóru":
            db += 1

        i += 1

    return db