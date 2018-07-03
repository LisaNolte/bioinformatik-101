#Gibbs Sampling

k_input=input("Länge des k-mers hier einfügen")
t_input=input("Anzahl der DNA strings hier einfügen")
N_input=input("Integer N hier einfügen")
dna_input=input("Collection of DNA strings dna hier einfügen")


import random
dna_list=dna_input.split(" ")


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


def create_empty_profile_array(k):
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
    profile_array.append(t_array) #im Profile Array hat nun der a_array den Index 0, der c_array den Index 1, der g_array den Index 2, der t_array den Index 3
    return (profile_array)


def get_random_motifs(dna,k):
    random_motifs=[]                                        #random_motifs soll eine Liste sein, in der sich je ein random ausgewähltes k-mer aus jedem String der dna_list befindet; am Anfang wird die Liste mit 0 initialisiert
    for i in range (0,len(dna_list)):                       #für jeden Eintrag i innerhalb der dna_list (für jeden String)
        y=len(dna_list[i])-k                                #y soll der letzt mögliche Startpunkt sein, von dem aus in jedem String ein k-mer gebildet werden kann
        n=random.randint(0,y)                               #n ist eine random ausgewählte Zahl zwischen 0 und y (y ist nicht eingeschlossen!), n sind dann die möglichen Startpunkte von denen aus die Pattern gebildet werden können
        pattern=""
        for j in range(n,n+k):                                  
            pattern+=dna_list[i][j]                         #Zusammenbau des Patterns von n ausgehend (hinzugefügt wird der Character an der Stelle j innerhalb des Indexes i der dna_list), sodass ein Pattern der Länge k gebildet wird; jetzt haben wir für jeden String ein random ausgewähltes Pattern der Länge k
        random_motifs.append(pattern)                       #das Pattern wird der Liste random_motifs hinzugefügt, in dem sich am Ende der for-Schleife je ein random ausgewähltes k-mer aus jedem String befindet
    return random_motifs


def gibbs_sampler(best_motifs,k,t,N):
    a=random.randint(0,t-1)
    smaller_motifs_array=best_motifs.copy()
    saved_dna_string=dna_list[a]
    del smaller_motifs_array[a]
    
    profile_array=create_empty_profile_array(k)

    for l in range (0, len(smaller_motifs_array)):                      #für jeden Eintrag (Index) l im smaller_morifs Array
        for o in range (0,k):                                           #für jeden Character eines jeden random_motifs (k-mer)
            line_index=symbol_to_number(smaller_motifs_array[l][o])     #die Variable line_index = die Nummer des jeweiligen Characters (wird errechnet aus der Funktion symbol_to_number; A=0, C=1, G=2, T=3)
            profile_array[line_index][o]+=1/t                           #zum Profile_array wird am Eintrag des line_indices (sagt aus in welchem Subarray wir uns befinden) der o'te Eintrag (sagt aus an welcher Stelle des k-mers wir uns befinden) um 1/t erhöht (weil die Wahrscheinlichkeit, diesen Character zu erhalten, bis zum jetzigen Zeitpunkt 1/t ist

    motifs_of_saved_dna_string=[]

    for start in range (0,len(saved_dna_string)-k+1):       #für alle möglichen Startpunkte (also endend mit dem letzten möglichen vollständigen k-mer)
        pattern=""                                          #pattern zurücksetzen
        for c in range(start,start+k):                      #ausgehend vom Startpunkt werden k-mere gebildet (für k-mere zwischen start und start+k)
            pattern=pattern+saved_dna_string[c]              #aktueller character zum pattern hinzufügen
        motifs_of_saved_dna_string.append(pattern)          #vollständiges pattern zum motifs_of_saved_dna_string Array hinzufügen


    probabilities_motifs_of_saved_dna_string=[]
    for d in range(0,len(motifs_of_saved_dna_string)):
        probabilities_motifs_of_saved_dna_string.append(score(motifs_of_saved_dna_string[d],profile_array)) #hier hat man jetzt für jedes k-mer des ausgewählten saved_strings die probability drin, dass dieses k-mere von der profile_matrix erstellt wurde


    minimum_score=min(probabilities_motifs_of_saved_dna_string) #finde die kleinste probability eines k-mers des saved_strings
    standardized_score=[]
    sum_of_standardized_scores=0
    computed_ratios=[]
    for e in range(0,len(probabilities_motifs_of_saved_dna_string)): 
        standardized_score.append(probabilities_motifs_of_saved_dna_string[e] / minimum_score)
    for f in range(0,len(standardized_score)):
        sum_of_standardized_scores+=standardized_score[f]
    for f in range (0,len(standardized_score)):
        computed_ratios.append(standardized_score[f] / sum_of_standardized_scores) #computed_ratios ist ein Array, der so viele Einträge hat, wie es k-mere in dem saved_string gibt
    
    g=random.randint(0,1)
    start_position=0
    for h in range(0,len(computed_ratios)):
        threshold=0
        for l in range(0,h):
            threshold+=computed_ratios[l]
        if g<=threshold:
            start_position=h
            break
    new_start_motif=motifs_of_saved_dna_string[h]
    best_motifs[a]=new_start_motif
    return best_motifs
            
            
best_motifs=get_random_motifs(dna_list, int(k_input))

for m in range(0,int(N_input)):
    best_motifs=gibbs_sampler(best_motifs,int(k_input),int(t_input),int(N_input))
print(best_motifs)
    

        
