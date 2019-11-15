from random import randrange
import pdb

FELS = '*'
WEG = ' '

OBEN = (0, -1)
UNTEN = (0, 1)
LINKS = (-1, 0)
RECHTS = (1, 0)

REIHE = 0
SPALTE = 1

GERADE = [OBEN, UNTEN, LINKS, RECHTS]
DIAGONAL = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

LINIEN = {'ensw': '┼',
          'ens': '├',
          'enw': '┴',
          'esw': '┬',
          'es': '┌',
          'en': '└',
          'ew': '─',
          'e': '╶',
          'nsw': '┤',
          'ns': '│',
          'nw': '┘',
          'sw': '┐',
          's': '╷',
          'n': '╵',
          'w': '╴'}



def wuerfeln(seiten):
    return randrange(1, seiten + 1)


def ob_fels(anteil_fels):
    if wuerfeln(100) <= anteil_fels:
        return FELS
    else:
        return " "


def hoch(lab):
    """Anzahl Zeilen """
    return len(lab)


def breit(lab):
    """Anzahl Spalten"""
    return len(lab[0])


def malen(lab):
    """Alle Felder reihenweise hinschreiben. """
    for reihe in lab:
        print(''.join(reihe))


def neues_brett(zeilen, spalten, feld):
    """Erzeuge neues Brett mit identichen Feldern"""
    return [[feld for _ in range(0, spalten)] for _ in range(0, zeilen)]


def mache(feld, inhalt, brett):
    """Inhalt eines Felds verändern. XXX"""
    brett[feld[0]][feld[1]] = inhalt


def schaue(feld, brett):
    """Inhalt eines Felds auslesen. """
    return brett[feld[0]][feld[1]]


def bewege(richtung, feld):
    """Gehe vom Feld in die übergebene Richtung"""
    return (feld[REIHE] + richtung[REIHE],
            feld[SPALTE] + richtung[SPALTE])


def innen(feld, brett):
    """Prüft ob Feld weder außerhalb noch auf dem Rand liegt"""
    return 0 < feld[REIHE] < (hoch(brett) - 1) and \
        0 < feld[SPALTE] < (breit(brett) - 1)


def nachbarn(feld, brett, diagonal=False):
    """Liste er Nachbarfelder"""
    felder = []
    richtungen = GERADE
    if diagonal:
        richtungen = richtungen + DIAGONAL
    for r in richtungen:
        nachbar = bewege(r, feld)
        if innen(nachbar, brett):
            felder.append(nachbar)
    return felder


def zaehle(felder, inhalt, brett):
    """Anzahl der Felder mit dem vorgegeben Inhalt"""
    anzahl = 0
    for feld in felder:
        if schaue(feld, brett) == inhalt:
            anzahl += 1
    return anzahl


def wohin(feld, versuche, brett):
    """Finde des nächste Welt, dass sich als Weg eignet"""
    for versuch in range(0, versuche):
        neu = bewege(GERADE[wuerfeln(4) - 1], feld)
        # pdb.set_trace()
        if innen(neu, brett) and \
                (schaue(neu, brett) == FELS) and \
                zaehle(nachbarn(neu, brett), WEG, brett) <= 1:
            return neu
    return None
