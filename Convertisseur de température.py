def arr(val):
    nb = list(str(round(val,12)))
    chf = nb[-1]
    while chf == "0":
        del nb[-1]
        chf = nb[-1]
    if chf == ".": del nb[-1]
    nb.join("")
    print()
    return nb

def cf(c):
    nb = c*1.8 + 32
    print(nb)
    return nb
cf(5)
