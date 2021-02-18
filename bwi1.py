"""Ich habe mich für diesen Algorithmus entschieden da er schnell und einfach ist"""
"""Idee: Ich mache ein Objekt LKW mit den Methoden add und remove. 
Dann schreibe ich einen Algorithmus der die LWKs auffült. 
Wenn er ein Objekt findet das einen höheren "score" als ein anderes hat und in den LKW passt, wenn man das andere entfert, 
wird das neue objekt in den LKW getan und das Alte entfert.

Ich habe rausgefunden das wenn man als "Score", für die Sortierung, nicht nur dem Nutzwert sondern den Nutzwert/Gewicht nimmt man den höchsten gesamt Nutzerwert bekommt.
Das setzt sich daraus zusammen das um so höher das Gewicht ist um so weniger Teile passen in den Lkw
-> um so höher das Gewicht um so kleiner wir der Gesamtnutzwert
-> Score~1/Gewicht
Umso höher der Nutzwert eines Teils um so höher der Gesamtnutzwert
->Gesamtnutzwert~Nutzwert
--> score~Nutzwert/Gewicht

Zum schluss wird der Score aber nur als der Nutzwert angegeben da der Lkw am Ende so oder so möglichst voll sein soll."""

vorrat=[['Notebook Büro 13', 205, 2451, 40],
['Notebook Büro 14', 420, 2978, 35],
['Notebook outdoor', 450, 3625, 80],
['Mobiltelefon Büro', 60, 717, 30],
['Mobiltelefon Outdoor', 157, 988, 60],
['Mobiltelefon Heavy Duty', 220, 1220, 65],
['Tablet Büro klein', 620, 1405, 40],
['Tablet Büro groß', 250, 1455, 40],
['Tablet outdoor klein', 540, 1690, 45],
['Tablet outdoor groß', 370, 1980, 68]]

#objekt Lkw
class Lkw:
    def __init__(self, kg_fahrer):
        """Initialisiert ein Objekt LKW. Das Object hat als Eigenschaften das Gewicht des Fahrers,
        die Gesamtzuladung des LKWs und die Ladung des LKWs."""

        self.kg_fahrer=kg_fahrer
        self.kg_max=1100*(10**3)-kg_fahrer*(10**3)#hier wird die maximale zuladung mit fahrere ausgerechnet. Aber nicht in kg sondern in g, da die einzuladenden Gegenstände alle in Gramm angegeben sind
        self.ladung=[]

    def add(self, element):
        """Fuegt elemente zu dem Lwk hinzu und nimmt sie aus dem Vorrat"""
        if element[2]<=0:
            #print("\nWarning add: Das element ist nicht mehr auf Lager und kann deshalb nicht hinzugefuegt werden")
            pass

        else:
            vorrat[vorrat.index(element)][2]-=1#Die Anzahl des Elements in dem Vorrat wird um 1 reduziert

            temp=[x for x in self.ladung if x[0]==element[0]]#wenn der Name des Elements in der Ladung ist wird das Element aus der Ladung in temp gespeichert
            
            if temp:#wenn das Element in der Ladung ist. (Also wenn temp nicht leer ist)
                for x in self.ladung:
                    if x[0]==element[0]:#wenn die Elemente den gleichen Namen haben
                        index=self.ladung.index(x)#wird der Index es Elements in der Ladung mit diesem Namen gesucht
                        self.ladung[index][2]+=1#und die Anzahl dieses Elements erhöht

            else:#wenn das Element nicht in der Ladung ist wird es hinzugefuegt
                self.ladung.append([element[0],element[1],1,element[3]])

    def remove(self, element):
        """das Element aus der Ladung nehmen und zurück in den Vorrat tun"""

        temp=[x for x in self.ladung if x[0]==element[0]]#wenn Element in der Ladung ist
        if temp:
            for x in vorrat:
                if x[0]==element[0]:#wenn die Elemente in der Laudung und dem Vorrat den gleichen Namen haben
                    vorrat[vorrat.index(x)][2]+=1#wird die Anzahl des Elements in dem Vorrat wird um 1 erhöht

            for x in self.ladung:
                if x[0]==element[0]:
                    index=self.ladung.index(x)
                    self.ladung[index][2]-=1#Die Anzahl des Elements in der Ladung wird um 1 reduziert

                    if self.ladung[index][2]<=0:#wenn das element nicht mehr vorhanden ist wird es aus der Liste gelöscht
                        self.ladung.pop(index)
        else:
            #print("\nWarning remove: Das element ist nicht in der Ladung!")
            pass
    def kg_aktuell(self):
        """Das aktuelle Gewicht der Ladung"""
        return sum([x[1]*x[2] for x in self.ladung])
    
    def score(self):
        """Der Nutzerwert der gesamten Ladung in dem LKW"""
        return sum([x[3]*x[2] for x in self.ladung])





#Hier fängt Algorithmus an
#beachten ich habe zwei lkws zwischen denen kann ich auch die elemente austauschen!!!!!!!

def aufFuellen(lkw):
    """Der eigentliche Algorithmus der oben beschrieben wurde"""
    change=True
    temp_list_change=[]

    while change==True: #solange noch Änderungen in der Ladung des LKWs gemacht wurden wird diese Schleife aus geführt
        #print("Noch eine Runde")
        for item in vorrat:
            if item[2]>0:#wenn das Item noch auf Lager ist

                while lkw.kg_max>=lkw.kg_aktuell() and vorrat[vorrat.index(item)][2]>0:#Der Lkw wird mit diesem Element aufgefüllt
                    lkw.add(item)
                    if lkw.kg_max<lkw.kg_aktuell():
                        lkw.remove(item)
                        break
                
                if lkw.kg_max<lkw.kg_aktuell():#muss gemacht werden da wenn die while bedinung ueberschritten wird noch ein element drauf gelegt wird
                    lkw.remove(item)

                for x in lkw.ladung:#Ersetzen
                    if item[3]/item[1]>x[3]/x[1] and lkw.kg_max>=lkw.kg_aktuell()-x[1]+item[1]:#Wenn das Element besser als eins aus der Lkw Ladung ist
                        #ersetzt es das Element in der Ladung.
                        #besser heist der Nutzwert/Gewicht ist höher 

                        while lkw.kg_max>=lkw.kg_aktuell() and vorrat[vorrat.index(item)][2]>0 and x in lkw.ladung:
                            lkw.remove(x)
                            lkw.add(item)
                            """while lkw.kg_max>=lkw.kg_aktuell() and vorrat[vorrat.index(item)][2]>0:
                                lkw.add(item)
                                if lkw.kg_max<lkw.kg_aktuell():
                                    lkw.remove(item)
                                    break"""#gibt niedrigeren score keine Ahnung wieso
                            if lkw.kg_max<lkw.kg_aktuell():        
                                lkw.remove(x)
                        
        if temp_list_change==lkw.ladung:#wenn die Ladung in dem LKW sich nicht mehr geändert hat wird die Schleife unterbrochen und der Algorithmus ist am fertig
            change=False
            temp_list_change=lkw.ladung
        else:
            temp_list_change=lkw.ladung
    

def doppelKontrolle(lkw):
    """Zwei Elemente in dem Vorrat können zusammen besser sein als ein Element in der LKW Ladung sein.
    Diese Elemente in der Ladung werden hier ausgetauscht"""
    for item in lkw.ladung:
        for x in vorrat:
            for y in vorrat:
                if x[3]/x[1]+y[3]/y[1]>item[3]/item[1] and lkw.kg_max>=lkw.kg_aktuell()+x[1]+y[1]-item[1]:
                    if x[2]>0 and y[2]>0 and item[2]>0:
                        lkw.remove(item)
                        lkw.add(x)
                        lkw.add(y)

def trippelKontrolle(lkw):
    """Drei Elemente in dem Vorrat können zusammen besser sein als ein Element in der LKW Ladung sein.
    Diese Elemente in der Ladung werden hier ausgetauscht.
    Kommt eher nicht vor."""
    for item in lkw.ladung:
        for x in vorrat:
            for y in vorrat:
                for z in vorrat:
                    if x[3]/x[1]+y[3]/y[1]+z[3]/z[1]>item[3]/item[1] and lkw.kg_max>=lkw.kg_aktuell()+x[1]+y[1]+z[1]-item[1]:
                        if x[2]>0 and y[2]>0 and z[2]>0 and item[2]>0:
                            lkw.remove(item)
                            lkw.add(x)
                            lkw.add(y)

def doppelKontrolle2(lkw):
    """Zwei Elemente in der LKW Ladung können zusammen schlecher sein als ein Element in dem Vorrat sein.
    Diese Elemente in der Ladung werden hier ausgetauscht.
    Das das vorkommt ist eher unwarscheinlich."""
    for item in vorrat:
        for x in lkw.ladung:
            for y in lkw.ladung:
                if x[3]/x[1]+y[3]/y[1]<item[3]/item[1] and lkw.kg_max>=lkw.kg_aktuell()-x[1]-y[1]+item[1]:
                    #print("Kommt das ueberhaubt vor?????????")
                    if x[2]>0 and y[2]>0 and item[2]>0:
                        lkw.add(item)
                        lkw.remove(x)
                        lkw.remove(y)


if __name__ == "__main__":
    lkw1=Lkw(72.4)
    lkw2=Lkw(85.7)

    #print("Maximale Zuladung (in Gramm) mit Fahrer für den ersten LKW:", lkw1.kg_max)
    
    aufFuellen(lkw1)
    aufFuellen(lkw2)
    aufFuellen(lkw1)#Keine Ahung wieso. Gibt aber höheren score

    doppelKontrolle(lkw1)
    doppelKontrolle(lkw2)

    #Die Funktionen ab hier verbessern den Score nicht aber sind hier zur Vollständigkeit angeben. 
    #Z.B. Wenn sich der Vorrat ändert könnten sie vielleicht noch etwas ändern
    doppelKontrolle2(lkw1)
    doppelKontrolle2(lkw2)
    
    trippelKontrolle(lkw1)
    trippelKontrolle(lkw2)
    


    print("\nLkw1: \nLadung: ", lkw1.ladung)
    print("Score1: ", lkw1.score())
    print("kg_max1: ", lkw1.kg_max," kg_aktuell1: ", lkw1.kg_aktuell())

    print("\nLkw2: \nLadung: ", lkw2.ladung)
    print("Score2: ", lkw2.score())
    print("kg_max2: ", lkw2.kg_max," kg_aktuell2: ", lkw2.kg_aktuell())
    

    print("\nVorrat:", vorrat)

    print("\nNutzwert Gesamt: ",lkw1.score()+lkw2.score())


