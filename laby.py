from random import randrange
import pdb

REIHE = 0
SPALTE = 1

FELD = {'fels': '*',  # schwarze: ■, schraffierte: ▩
        'weg': ' '}

GERADE = {'n': (-1, 0),  # nord
          's': (1, 0),  # süd
          'w': (0, -1),  # west
          'o': (0, 1)}  # ost

DIAGONAL = {'nw': (-1, -1),
            'sw': (1, -1),
            'os': (1, 1),
            'on': (-1, 1)}

RICHTUNG = {**GERADE, **DIAGONAL}

LINIEN = {'onsw': '┼',
          'ons': '├',
          'onw': '┴',
          'osw': '┬',
          'os': '┌',
          'on': '└',
          'ow': '─',
          'o': '╶',
          'nsw': '┤',
          'ns': '│',
          'nw': '┘',
          'sw': '┐',
          's': '╷',
          'n': '╵',
          'w': '╴',
          '': '▩'}  # ■▪


def wuerfeln(seiten):
    return randrange(1, seiten + 1)


def ob_fels(anteil_fels):
    if wuerfeln(100) <= anteil_fels:
        return FELD['fels']
    else:
        return " "


def hoch(lab):
    """Anzahl Zeilen """
    return len(lab)


def breit(lab):
    """Anzahl Spalten"""
    return len(lab[0])


def zeige(lab):
    """Alle Felder reihenweise hinschreiben. """
    for reihe in lab:
        print(''.join(reihe))


def neues_brett(zeilen, spalten, inhalt=FELD['fels']):
    """Erzeuge neues Brett mit identichen Feldern"""
    return [[inhalt for _ in range(spalten)] for _ in range(zeilen)]


def schreibe(feld, inhalt, brett):
    """Inhalt eines Felds verändern. XXX"""
    brett[feld[0]][feld[1]] = inhalt


def lese(feld, brett, aussen='X'):
    """Inhalt eines Felds auslesen. """
    if feld[0] < 0 or feld[1] < 0:
        return aussen
    try:
        return brett[feld[0]][feld[1]]
    except IndexError:
        return aussen


def bewege(onsw, feld):
    """Gehe vom Feld in die übergebene Richtung (z.B. 'n')"""
    r = RICHTUNG[onsw]
    return feld[0] + r[0], feld[1] + r[1]


def innen(feld, brett):
    """Prüft ob Feld weder außerhalb noch auf dem Rand liegt"""
    return 0 < feld[REIHE] < (hoch(brett) - 1) and \
           0 < feld[SPALTE] < (breit(brett) - 1)


def nachbarn(feld, richtungen, brett):
    """Liste er Nachbarfelder"""
    felder = []
    for r in richtungen:
        nachbar = bewege(r, feld)
        if innen(nachbar, brett):
            felder.append(nachbar)
    return felder


def zaehle(felder, inhalt, brett):
    """Anzahl der Felder mit dem vorgegeben Inhalt"""
    anzahl = 0
    for feld in felder:
        if lese(feld, brett) == inhalt:
            anzahl += 1
    return anzahl


def wohin(feld, versuche, brett):
    """Finde nächstes Feld, das sich als Weg eignet"""
    richtungen = list(GERADE.keys())
    for versuch in range(0, versuche):
        gucke = bewege(richtungen[wuerfeln(4) - 1], feld)
        # pdb.set_trace()
        if innen(gucke, brett) and \
                (lese(gucke, brett) == FELD['fels']) and \
                zaehle(nachbarn(gucke, GERADE, brett), FELD['weg'], brett) <= 1:
            return gucke
    return None


def ersetze(regel,brett):
    """regel ist eine Funktion die ein Feld und ein Brett erwartet"""
    ersetzt = neues_brett(hoch(brett),breit(brett))
    for reihe in range(hoch(brett)):
        for spalte in range(breit(brett)):
            feld = (reihe,spalte)
            schreibe(feld,regel(feld,brett),ersetzt)
    return ersetzt