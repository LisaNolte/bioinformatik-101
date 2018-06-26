#randomized motif search

k_input=input("Länge des k-mers hier einfügen")
t_input=input("Anzahl der DNA strings hier einfügen")
dna_input=input("Collection of DNA strings dna hier einfügen")

import random
dna_list=dna_input.split(" ") 
best_motifs=[]

def symbol_to_number(symbol):                               #definieren der Funktion Symbol_to_number, durch die A,C,G und T je einen Integer zugewiesen bekommen 
    if symbol == "A":
        return 0
    if symbol == "C":
        return 1
    if symbol == "G":
        return 2
    if symbol == "T":
        return 3


def score(pattern,profile_matrix):                          #Definieren einer Funktion score, welche die einzelnen Wahrscheinlichkeiten (der Basen des Patterns) der profile-Matrix miteinander multipliziert
    score=1
    for x in range (0,len(pattern)):                        #für jeden Character des patterns
        line=symbol_to_number(pattern[x])                   #line ist die Nummer des Characters analog zur Funktion symbol_to_number (so erhalten wir den Index, an dem wir in die Profile_matrix gucken müssen)
        if profile_matrix[line][x] != 0:                    #wenn der Eintrag x des Indices [line] der profile_matrix ungleich 0 ist
            score*=profile_matrix[line][x]                  #dann multipliziere den bisherigen Score (anfangs 1) mit dem Wert, der in der profile_matrix im Index [line] an der Stelle x steht
    return score

def update_best_motifs(best_motifs, dna_list,k,t):
    profile_array=[]                                        #Initialisieren der Profile Matrix als Array, zu welchem später die einzelnen Arrays a,c,g und t hinzugefügt werden
    a_array=[]
    c_array=[]
    g_array=[]
    t_array=[]
    for m in range (0,k):
        a_array.append(0)
        c_array.append(0)
        g_array.append(0)
        t_array.append(0)
    profile_array.append(a_array)
    profile_array.append(c_array)
    profile_array.append(g_array)
    profile_array.append(t_array)                           #im Profile Array hat nun der a_array den Index 0, der c_array den Index 1, der g_array den Index 2, der t_array den Index 3

    for l in range (0, len(best_motifs)):                   #für jeden Eintrag (Index) l im random_morifs Array
        for o in range (0,k):                               #für jeden Character eines jeden random_motifs (k-mer)
            line_index=symbol_to_number(best_motifs[l][o])  #die Variable line_index = die Nummer des jeweiligen Characters (wird errechnet aus der Funktion symbol_to_number; A=0, C=1, G=2, T=3)
            profile_array[line_index][o]+=1/t               #zum Profile_array wird am Eintrag des line_indices (sagt aus in welchem Subarray wir uns befinden) der o'te Eintrag (sagt aus an welcher Stelle des k-mers wir uns befinden) um 1/t erhöht (weil die Wahrscheinlichkeit, diesen Character zu erhalten, bis zum jetzigen Zeitpunkt 1/t ist
    
    for p in range (0,len(dna_list)):                       #für jeden String der Dna_list
        y=len(dna_list[0])-k+1                              #y ist der letzt mögliche Startpunkt, von dem aus man ein k-mer bilden kann; 
        new_motifs=[]
        for q in range (0,y):                               #für jeden Startpunkt q zwischen 0 und y (+1, da der Endpunkt der For-Schleife, der in der Klammer angegeben wird, schon nicht mehr mitgezählt wird)
            motif_pattern=""
            for r in range (q,q+k): 
                motif_pattern+=dna_list[p][r]               #es werden k-mere gebildet vom Startpunkt q aus und zwar so, dass jeweils der r'te Character aus dem p'ten Index der DNA-list dem pattern des new_motifs hinzugefügt wird
            new_motifs.append(motif_pattern)                #im new_motifs Array sind nun alle möglichen k-mere des jeweiligen zu betrachtenden Strings gespeichert
        for s in range (0,len(new_motifs)):                 #für jeden Eintrag des new_motifs Arrays (also für jeden möglichen k-mer new_motif des betrachteten Strings)
            if score(new_motifs[s],profile_array) > score(best_motifs[p],profile_array): #wenn der Score des betrachteten new_motifs größer ist als der des bisherigen besten_motifs des betrachteten Strings
                best_motifs[p] = new_motifs[s]              #dann erhält der p'te Eintrag des best_motifs Array das Pattern des s'ten Eintrages des new_motifs Arrays (dessen Score ja augenscheinlich größer, also besser, ist) 
      

    return best_motifs

def randomized_motif_search(dna,k,t):
    global best_motifs
    random_motifs=[]                                        #random_motifs soll eine Liste sein, in der sich je ein random ausgewähltes k-mer aus jedem String der dna_list befindet; am Anfang wird die Liste mit 0 initialisiert
    for i in range (0,len(dna_list)):                       #für jeden Eintrag i innerhalb der dna_list (für jeden String)
        y=len(dna_list[i])-k                                #y soll der letzt mögliche Startpunkt sein, von dem aus in jedem String ein k-mer gebildet werden kann
        n=random.randint(0,y)                               #n ist eine random ausgewählte Zahl zwischen 0 und y (y ist nicht eingeschlossen!), n sind dann die möglichen Startpunkte von denen aus die Pattern gebildet werden können
        pattern=""
        for j in range(n,n+k):                                  
            pattern+=dna_list[i][j]                         #Zusammenbau des Patterns von n ausgehend (hinzugefügt wird der Character an der Stelle j innerhalb des Indexes i der dna_list), sodass ein Pattern der Länge k gebildet wird; jetzt haben wir für jeden String ein random ausgewähltes Pattern der Länge k
        random_motifs.append(pattern)                       #das Pattern wird der Liste random_motifs hinzugefügt, in dem sich am Ende der for-Schleife je ein random ausgewähltes k-mer aus jedem String befindet

    best_motifs=update_best_motifs(random_motifs, dna_list,k,t)
        

    return(best_motifs)


best_motifs=randomized_motif_search(dna_input,int(k_input),int(t_input))
print(best_motifs)



