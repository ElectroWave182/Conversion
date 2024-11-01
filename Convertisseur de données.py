def arr(val,unite):
    nb,uniteF = list(str("%.3e"%val)),unite[0].upper()
    if unite == "o": uniteF += ".\nLes valeurs sont égales, car il n'y a pas d'unité équivalente pour l'octet."
    elif unite[1] == "o": uniteF += "i."
    elif unite[1] == "i": uniteF += "o."
    chf = nb[-5]
    while chf == "0":
        del nb[-5]
        chf = nb[-5]
    if chf == ".": del nb[-5]
    aff = "".join(nb)
    return (aff + " " + uniteF)
def converse(oc,bi):
    print("\nEntrez votre valeur de départ...")
    val = float(input())
    print("","Octet: o","Kilo-Octet: ko","KibiOctet: ki","MégaOctet: mo","MébiOctet: mi","GigaOctet: go","GibiOctet: gi","TéraOctet: to","TébiOctet: ti","PétaOctet: po","PébiOctet: pi","ExaOctet: eo","ExbiOctet: ei","ZettaOctet: zo","ZébiOctet: zi","YottaOctet: yo","YobiOctet: yi","\nEntrez l'unité correspondante...",sep = "\n")
    while True:
        unite = input()
        if unite in oc:
            val *= 1.024**oc.index(unite)
            break
        if unite in bi:
            val /= 1.024**bi.index(unite)
            break
    return arr(val,unite)
print("\n" + converse(["o","ko","mo","go","to","po","eo","yo","zo"],["o","ki","mi","gi","ti","pi","ei","yi","zi"]))