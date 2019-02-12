# -*- coding: utf-8 -*-
"""Aufgabe 1

Original file is located at
    https://colab.research.google.com/drive/1YKMcv4-cwHAheY-Nhrm3F4TnzYKWxgQq

Aufgabe 1- Superstar
Das Programm besteht aus vier Teilen. Das gleiche Programm funktioniert außerdem bei allen Beispielen.

1.Das Text Dokument wird eingelesen und in eine Liste verpackt.

2.Nun werden die Follower aller einzelnen Personen gezählt.

3.Durch den vorherigen Schritt können jetzt ganz einfach die potentiellen Superstart bestimmt werden.

4.Im letzten Schritt checkt das Programm ob oder die potentiellen Superstars nicht doch selber noch anderen Leuten folgen.
Wenn dies der Fall ist, gibt es keinen Superstar. Wenn aber nicht dann wird dieser ausgegeben.
"""

#Beispiel in Programm laden
file = open("1.4.txt")
gruppe = []
reader = file.readlines()
for line in reader:
  elements = []
  for i in range(0,1):
    elements.append(line.split())
  gruppe.append(elements)

print(gruppe)

#follower der einzelnen Personen bestimmen
anzahl_der_mitglieder = len(gruppe[0][0])
follower = []
for i in range(1,anzahl_der_mitglieder+1):
  follower.append(0)
  for d in range(1,len(gruppe)):
    if gruppe[d][0][1] == gruppe[0][0][i-1]:
      follower[i-1] += 1
print(follower)

#die Personen bestimmen, denen allen folgen
pot_superstar = []
for i in range(0, len(follower)):
  if follower[i] == anzahl_der_mitglieder -1:
    pot_superstar.append(gruppe[0][0][i])
    
print(pot_superstar)

#schauen ob der potentielle superstar selber jemanden folgt
superstar_der_gruppe = ''
for superstar in pot_superstar:
  anzahl_der_gefolgten_Personen = 0
  for i in range(1, anzahl_der_mitglieder):
    if gruppe[i][0][0] == superstar:
      anzahl_der_gefolgten_Personen += 1
    
  if anzahl_der_gefolgten_Personen == 0:
    superstar_der_gruppe = superstar
    break
if superstar_der_gruppe == '':
  print("Es gibt in dieser Gruppe keinen Superstar!")
else:
  print("Der Superstar der Gruppe heisst:", superstar_der_gruppe)
