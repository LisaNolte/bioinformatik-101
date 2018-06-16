#Median String Ba2b

k_input=input("Länge des k-mers hier einfügen")
dna_input=input("Collection of DNA strings dna hier einfügen")

import math
dna_list=dna_input.split(" ")                                               #Erstellen einer Liste, die die einzelnen DNA Strings enthält

number_to_symbol={0:"A", 1:"C", 2:"G", 3:"T"}                               #Zuordnung der Basen mit Nummern in einem Dictionary
def number_to_pattern(i,k):
    if k == 1:
        return number_to_symbol[i]
    else:
        last_number_value = i % 4                                           #last_number_value ist die Number des Symbols der allerletzten Base im String (durch % wird uns der Rest der Division ausgegeben (Modulo-Operator))
        prefix_index=(i - last_number_value)/4                              #der Index (die Nummer) des Präfix ist gleich dem Gesamtindex minus dem Rest (also der Number der letzten Base) geteilt durch 4
        prefix_pattern=""
                                                                            #l ist Länge des kmers, -1 für index (weil erster Character die Zahl 0 hat) und nochmal -1 weil prefix eins kürzer ist
        for l in range(k-2,-1,-1):                                          #l soll der Exponent sein (also die Position der Base, von rechts beginnend im String mit 0). Da die erste Base den höchsten Exponenten hat und die letzte Base den niedrigsten, fangen wir bei k-1 an und zählen dann runter bis 0.
            number_for_symbol=int (prefix_index/(4**l))                     #Nummer des Präfix-Eintrages an der Position l; die höchste Zahl ist ganz links
            prefix_pattern += number_to_symbol[number_for_symbol]
            prefix_index -= number_for_symbol*(4**l)                        #vom prefix index muss die aktuelle potenz abgezogen werden
        current_pattern=prefix_pattern + number_to_symbol[last_number_value]

    return current_pattern                                                  #damit hat man jetzt das current_pattern herausgefunden, von welchem man die Distanz zu den dna_strings der dna_list herausfinden will


def distance_between_pattern_and_strings(current_pattern,dna,k):            #Funktionsdefinition zur Bestimmung von der insg. Distanz zwischen current_pattern und den DNA strings
    distance_current_pattern=0                                              #Definition der distance_current_pattern als Variable, die am Anfang den Wert 0 einnimmt
    for m in range(0, len(dna_list)):                                       #für jeden einzelnen DNA string in der dna_list
        hamming_distance = k                                                #hamming_distance ist am Anfang eines jeden DNA strings der dna_list genauso lang wie k (größer, als wenn alle Basen anders sind, kann die Distanz ja nicht sein)
        for start in range (0,len(dna_list[m])-k+1):                        #für alle möglichen Startpunkte innerhalb des einzelnen DNA strings der dna_list
            dna_pattern=""                                                  #dna_pattern ist am Anfang leer
            for j in range(start,start+k):                                  #Zusammenbau des dna_patterns vom Startpunkt ausgehend, sodass ein dna_pattern der Länge k gebildet wird  
                dna_pattern+=dna_list[m][j]                                 #der Character an der Stelle j des einzelnen DNA Strings der dna_list (also [m]) soll zum dna_pattern hinzugefügt werden                             
            count = 0                                                       #der count(Differenz zwischen dna_pattern und current_pattern) ist zu Beginn jedes dna_patterns 0
            for n in range (0, k):                                          #für alle Stellen n des dna_patterns (welches die Länge k hat)
                if dna_pattern[n] != current_pattern[n]:                    #wenn der Character an der Stelle n im dna_pattern sich von dem Character an der Stelle n im current_pattern unterscheidet
                    count += 1                                              #erhöhe den Count um 1. Der Count ist am Ende der for Schleife dann die Distanz zwischen einem einzelnen dna_pattern und dem current_pattern
            if hamming_distance >= count:
                hamming_distance = count                                    #so wird die hamming_distance immer die kleinste hamming_distance, die in dem einzelnen DNA string gefunden wird

        distance_current_pattern += hamming_distance                        #die distance addiert die einzelnen hamming_distances der Substrings (Dna_strings der dna_list) miteinander
    return distance_current_pattern


def median_string(dna,k):
    distance = float("inf")                                                 #Definition der Variable distance, die uns am Ende einer jeden for Schleife die Distanz des current_patterns und der dna_strings aus der dna_list ausgeben soll (der Wert wird immer möglichst klein gehalten und am Anfang mit unendlich initialisiert)
    for i in range(0, (4**k)-1):                                            #für alle möglichen Werte i (4**k Möglichkeiten gibt es, ein Pattern der Länge k aus den 4 Basen zu bilden); i geht sozusagen die Indices durch, wenn man ein Pattern_Array erstellt hätte
        current_pattern = number_to_pattern(i,k)                            #das current_pattern wird durch die Funktion number_to_pattern bestimmt
        if distance_between_pattern_and_strings(current_pattern,dna,k) < distance:
            distance = distance_between_pattern_and_strings(current_pattern,dna,k)
            median = current_pattern
    return median

print(median_string(dna_input, int(k_input)))
