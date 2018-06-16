#Distance between Pattern and Strings Ba2h

pattern_input=input("Pattern hier einfügen")
dna_input=input("Collection of DNA strings dna hier einfügen")


dna_list=dna_input.split(" ")                                               #Erstellen einer Liste, die die einzelnen DNA Strings enthält


def distance_between_pattern_and_strings(pattern_input,dna):                #Funktionsdefinition zur Bestimmung von der insg. Distanz zwischen Pattern und den DNA strings
    distance=0                                                              #Definition der distance als Variable, die am Anfang den Wert 0 einnimmt
    k = len(pattern_input)                                                  #k entspricht der Länge des Pattern_input
    for i in range(0, len(dna_list)):                                       #für jeden einzelnen DNA string in der dna_list
        hamming_distance = k                                                # hamming_distance ist am Anfang eines jeden DNA strings der dna_list genauso lang wie k (größer, als wenn alle Basen anders sind, kann die Distanz ja nicht sein)
        for start in range (0,len(dna_list[i])-k+1):                        #für alle möglichen Startpunkte innerhalb des einzelnen DNA strings der dna_list
            pattern=""                                                      #pattern ist am Anfang leer
            for j in range(start,start+k):                                  #Zusammenbau des Patterns vom Startpunkt ausgehend, sodass ein Pattern der Länge k gebildet wird  
                pattern+=dna_list[i][j]                                     #der Character an der Stelle j des einzelnen DNA Strings der dna_list (also [i]) soll zum Pattern hinzugefügt werden                             
            count = 0                                                       #der count(Differenz zwischen pattern und pattern_input) ist zu Beginn jedes Patterns 0
            for m in range (0, k):                                          #für alle Stellen m des Patterns (welches die Länge k hat)
                if pattern[m] != pattern_input[m]:                          #wenn der Character an der Stelle m im Pattern sich von dem Character an der Stelle m im Pattern_input unterscheidet
                    count += 1                                              #erhöhe den Count um 1. Der Count ist am Ende der for Schleife dann die Distanz zwischen einem einzelnen Pattern und dem pattern_input
            if hamming_distance >= count:
                hamming_distance = count                                    #so wird die hamming_distance immer die kleinste hamming_distance, die in dem einzelnen DNA string gefunden wird

        distance += hamming_distance                                        #die distance addiert die einzelnen hamming_distances der Substrings (Dna_strings der dna_list) miteinander
    return distance

print(distance_between_pattern_and_strings(pattern_input, dna_input))


    
