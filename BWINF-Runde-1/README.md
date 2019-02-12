# BWINF-Runde 1
Link zu Aufgabenstellung : https://bwinf.de/fileadmin/user_upload/BwInf/2018/37/1._Runde/Aufgaben/BWINF_37_Aufgaben_WEB.pdf

Aufgabe 1: Superstar

Bearbeiter/-innen dieser Aufgabe: 
Leonardo Benini

4. November 2018


Lösungsidee:

Mithilfe von Pythons Listen und for Schleifen kann die Text-Datei mit den Gruppen bestens ausgewertet werden und somit kann bestimmt werden ob es einen Superstar gibt und wenn ja wen.

Umsetzung:

Das Programm ist in Python geschrieben und mit allen Beispielen ausgeführt werden. Es besteht aus vier Teilen:
1.	Die Textdateien werden mit open Methode eingelesen und in eine große Liste verpackt. Die Textdatei wird in eine zweidimensionale Liste, namens „gruppe“, verpackt, wobei eine Zeile in der Datei einer Liste in „gruppe“ entspricht.

2.	Es wird eine Liste erstellt, namens Follower, in der die Anzahl der Follower der einzelnen Personen steht. Dies wird durch zwei for Schleifen erreicht.

3.	Im dritten Schritt wird überprüft ob einer Person alle anderen folgen. Wenn ja dann ist er ein potentieller Superstar.

4.	Im letzten Schritt wird überprüft ob der potentielle Superstar jemanden folgt. Wenn er dies nämlich tut dann ist er kein Superstar. Wenn dies nicht der Fall ist dann wird er als Superstar ausgegeben und wenn es keinen Superstar gibt wird dies ebenfalls ausgegeben.

Beispiele:

Beispiel 1: ('Der Superstar der Gruppe heißt:', 'Justin')

Beispiel 2: ('Der Superstar der Gruppe heißt:', 'Dijkstra')

Beispiel 3:  Es gibt in dieser Gruppe keinen Superstar!

Beispiel 4: ('Der Superstar der Gruppe heißt:', 'Folke')

Aufgabe 3: Voll daneben

Bearbeiter/-innen dieser Aufgabe: Leonardo Benini

November 2018
Lösungsidee:

Da Al die Zahlen der Mitspieler schon kennt bevor er seine eigenen aufstellt, kann er durch geschickte Durchschnittsberechnung seinen Gewinn verbessern.

Umsetzung:

Das Programm ist in Python geschrieben und kann für alle Beispiele ausgeführt werden. Im ersten Schritt wird die Textdatei in eine Liste gepackt. Im zweiten Schritt werden mit dem Python Paket „random“ 10 zufällige Zahlen für Al generiert. Daraufhin wird mit der Funktion „billanz_berechen“ der Gewinn oder Verlust Als berechnet. Um diese Bilanz zu verbessern werden die Zahlen der Mitspieler in zehn Abschnitte eingeteilt. Dies wird mit for Schleifen erreicht. Dann wird der Durchschnitt des jeweiligen Abschnitts berechnet und als neue Zahl für Al gemerkt. Als letztes werden die Zahlen des Al und die mit der Funktion „billanz_berechnen“ neu berechneten Bilanz ausgedruckt.

Beispiele:

Beispiel 1:

Die Zahlen des Al: [52, 152, 252, 352, 452, 552, 652, 752, 852, 950]

Die Bilanz beträgt: -1387

Die Bilanz bevor der Algorithmus angewandt worden ist: -4134

Beispiel 2:

Die Zahlen des Al: [40, 114, 239, 347, 396, 487, 607, 760, 840, 937]

Die Bilanz beträgt: -880

Die Bilanz bevor der Algorithmus angewandt worden ist: -1705

Beispiel 3:

Die Zahlen des Al: [94, 220, 304, 400, 492, 554, 644, 716, 814, 930]

Die Bilanz beträgt: -888

Die Bilanz bevor der Algorithmus angewandt worden ist: -9003

Ergebnis: Man kann schnell erkennen, dass der Algorithmus bessere Zahlen für Al ausgibt als ein Zufallsgenerator. Doch es ist auch auffällig, dass es keinen Gewinn, sondern einen Verlust gibt. Um dieses Problem zu lösen kann Al einfach den Eintrittspreis erhöhen.

Zusammengefasst: So wie das Glücksspiel grad ist, ist es gut für den Spieler, aber nicht für den Veranstalter.


Aufgabe 5: Widerstand

Bearbeiter/-innen dieser Aufgabe: Leonardo Benini

November 2018
Lösungsidee:

Für k = 1, 2, 3, 4 werden alle seriellen und parallelen Schaltungen ausprobiert und dann wird die genommen, die am nächsten an dem gewünschten Widerstand herankommt.

Umsetzung:

Das Programm ist in Python geschrieben. Als erstes wird die Text-Datei mit allen verfügbaren Widerständen eingelesen. Als nächstes werden zwei Funktionen kreiert, die eine Liste als Input nehmen und dann den seriell/parallel geschalteten Widerstand berechnen. Für k = 1 wird der Widerstand aus der Grabbelkiste genommen, der am nächsten am Ziel-Widerstand ist. Für k = 2 wird die beste serielle Schaltung mit der besten parallelen Schaltung verglichen und die genauere genommen. Dazu werden alle möglichen Kombinationen ausprobiert. Für k = 3 ,4 wird genau das gleiche gemacht. Mir ist bewusst, dass es teilweise bei k = 3, 4 noch genauere Schaltungen gäbe, wenn man seriell und parallel mixt. Aber da die Ergebnisse schon so genau sind lohnte sich die Implementierung nicht. Prinzipiell würde das Programm mit den gemischten Schaltungen genauso ablaufen wie das jetzige.

Beispiele:

In der ersten Zeile steht immer der Bauplan (dieser setzt sich aus [parallel / seriell und den benutzten Widerständen zusammen]), in der zweiten die Ungenauigkeit, in der dritten die zu erreichenden Widerstände und in der letzten die erreichten Widerstände.

Für k = 1 (beim Bauplan ist natürlich alles seriell, da es nur einen Widerstand gibt):

[470, 150, 330, 330, 1500, 2700, 3900]

[30, 10, 16, 15, 120, 19, 342]

[500, 140, 314, 315, 1620, 2719, 4242]

[470, 150, 330, 330, 1500, 2700, 3900]

Für k = 2:

[['parallel', [4700, 560]], ['parallel', [2200, 150]], ['parallel', [6800, 330]], ['parallel', [6800, 330]], ['seriell', [1500, 120]], ['seriell', [1500, 1200]], ['seriell', [3900, 330]]]

[0.38022813688218093, 0.425531914893611, 0.7265077138849847, 0.2734922861150153, 0, 19, 12]

[500, 140, 314, 315, 1620, 2719, 4242]

[500.3802281368822, 140.4255319148936, 314.726507713885, 314.726507713885, 1620, 2700, 4230]

Für k = 3:

[['seriell', [180, 220, 100]], ['parallel', [820, 2700, 180]], ['parallel', [820, 5600, 560]], ['parallel', [1200, 1800, 560]], ['seriell', [270, 1200, 150]], ['seriell', [820, 1800, 100]], ['seriell', [220, 3900, 120]]]

[500, 140, 314, 315, 1620, 2719, 4242]

[500, 139.94943109987358, 314.0902872777018, 315.0, 1620, 2720, 4240]

Für k = 4:

[['parallel', [2200, 5600, 6800, 820]], ['parallel', [560, 1800, 3900, 220]], ['parallel', [1500, 4700, 5600, 470]], ['parallel', [1000, 1200, 8200, 820]], ['seriell', [180, 470, 820, 150]], ['seriell', [120, 1000, 1500, 100]], ['seriell', [220, 1200, 2700, 120]]]

[0.07803673550205303, 0.0054387941416393915, 0.09366303570010359, 0.01920614596673431, 0, 1, 2]

[500, 140, 314, 315, 1620, 2719, 4242]

[500.07803673550205, 139.99456120585836, 313.9063369642999, 314.98079385403327, 1620, 2720, 4240]
