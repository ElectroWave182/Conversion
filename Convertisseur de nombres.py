from math import floor
from sys import stdin,stdout
input,print = stdin.readline,stdout.write
indA,indR = [0.083,0.5,1,5,10,50,100,500,1000],["•","S","I","V","X","L","C","D","M"]
def convAra(nb):
    out,maxi = 0,0
    for lettre in list(reversed(nb)):
        pos = indR.index(lettre)
        chiffre = indA[pos]
        if pos > maxi: maxi = pos
        if pos < maxi: out -= 2*chiffre
        out += chiffre
    return str(out)
def convRom(nb):
    if nb > 0: neg = False
    else: neg = True
    nb = floor(12*abs(nb))
    out,nb = nb%12//6 * "S" + nb%6 * "•",list(str(nb//12))
    nb = (4 - len(nb)) * [0] + nb
    for cran in range(2,7,2):
        chiffre = int(nb[-1])
        if chiffre in [4,9]: out = indR[cran] + indR[cran + chiffre//4] + out
        else: out = chiffre//5 * indR[cran + 1] + chiffre%5 * indR[cran] + out
        del nb[-1]
    out = int(nb[-1]) * "M" + out
    if neg: out = "-" + out
    return out
def presentation():
    print("•: 0.083\nS: 0.5\nI: 1\nV: 5\nX: 10\nL: 50\nC: 100\nD: 500\nM: 1000\nEntrez un nombre en écriture romaine, ou bien un décimal appartenant à ]-4 000 ; 4 000[...\n")
    while True:
        inp = input().rstrip("\n")
        if inp.isupper():
            carRom = True
            for lettre in inp:
                if not lettre in indR: carRom = False
            if carRom: return inp + " s'écrit aussi, en écriture décimale " + convAra(inp)
        if inp.lstrip("-").replace(".","",1).isdigit() and -4000 < float(inp) < 4000: return inp + " s'écrit aussi, en écriture romaine " + convRom(float(inp))
print(presentation())