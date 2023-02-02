kor_lista = []
def kor_beker():
    i = 0
    szoveg = ""
    while i < 5:
        ev = int(input("Kérem adja meg az ember korát: "))
        kor_lista.append(ev)
        if i != 4:
            szoveg += str(ev) + ":"
        else:
            szoveg += str(ev)
        i += 1
    print(f"II/A, B,C:\n\t {szoveg}")


def elso_idos():
    i = 0
    hely = -1
    while i < len(kor_lista) and hely < 0:
        if kor_lista[i] > 70:
            hely = i
        i += 1

    return hely

def konzolra_ir(hely):
    if hely > 0:
        print(f"II/D, E:\n\t Első idős ember korának helye a listában: {hely+1}")
    else:
        print(f"II/D, E:\n\t Nincs 70 feletti ember")


def fajl_ir(hely):
    fajl = open("oreg.txt", "w", encoding="utf-8")
    if hely > 0:
        fajl.write(f"II/F:\n\t Első idős ember korának helye a listában: {hely+1}")
    else:
        fajl.write(f"II/F:\n\t Nincs 70 feletti ember")
    fajl.close()