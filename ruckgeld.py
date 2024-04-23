from collections import deque # Importiere Datentyp "Deque"

def wechselgeld(betrag, nennwert = [20,11, 7,1]):
    queue = [(betrag, [])] # Queue = Warteschlange -> Aktueller Betrag | genutzte Muenzen

    while queue: # So lange Queue nicht leer ist. 
        curr_betrag, curr_muenzen = queue.pop(0) # Betrag und bisher genutzte Muenzen loeschen aus Warteschlange loeschen

        if curr_betrag == 0: # Wenn curr_betrag == 0 schnellster Weg gefunden. 
            return curr_muenzen

        for muenze in nennwert: # Fuer jede Muenze (20, 11, 7 ,1)
            if muenze <= curr_betrag: # Checken ob Muenze groeser oder gleich rest Betrag
                new_muenzen = curr_muenzen + [muenze] # genutzte Muenze wird an Warteschlang ergaenzt -> neuer Betrag ebenfalls
                queue.append((curr_betrag - muenze, new_muenzen)) # Ergebnis fur jede Muenze wird in die Warteschlange angehangen.


if __name__ == '__main__': # Bei Skript Ausfuerung
    betrag = int(input('>>> ')) # Input (Betrag) erhalten
 
    print(wechselgeld(betrag)) # Muenzen ausgeben.

