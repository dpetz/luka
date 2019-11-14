from random import randrange

FELS = '*'
WEG  = ' '


def wuerfeln(seiten):
    return randrange(1, seiten + 1)


def ob_fels(anteil_fels):
    if wuerfeln(100) <= anteil_fels:
        return FELS
    else:
        return " "


def hoch(lab):
    """Anzahl Zeilen """
    len(lab)


def breit(lab):
    """Anzahl Spalten"""
    len(lab[0])


def malen(lab):
    for reihe in lab:
        print(''.join(reihe))


def brett(zeilen, spalten, feld):
    """Erzeuge neues Brett mit identichen Feldern"""
    return [[FELS for s in range(0, spalten)] for z in range(0, zeilen)]