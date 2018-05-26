#Implement Number to Pattern

import math
index_input=input("Fügen Sie hier den Integer 'index' ein")
k_input=input("Länge des k-mers hier einfügen")



number_to_symbol={0:"A", 1:"C", 2:"G", 3:"T"}
def number_to_pattern(index,k):
    if k == 1:
        return number_to_symbol[index]
    else:
        last_number_value=index % 4 #last_number_value ist die Number des Symbols der allerletzten Base im String
        print(last_number_value)
        prefix_index=(index - last_number_value)/4 #der Index des Präfix ist gleich dem Gesamtindex - dem Rest (also der Number der letzten Base) geteilt durch 4
        print(prefix_index)
        prefix_pattern=""

        #i ist Länge des kmers, -1 für index und nochmal -1 weil prefix eins kürzer ist
        for i in range(k-2,-1,-1): #i soll der Exponent sein (also die Position der Base, von rechts beginnend im String mit 0). Da die erste Base den höchsten Exponenten hat und die letzte Base den niedrigsten, fangen wir bei k-1 an und zählen dann runter bis 0.
            number_for_symbol=int (prefix_index/(4**i)) #Nummer des Präfix-Eintrages an der Position i; die höchste Zahl ist ganz links
            print(number_for_symbol)
            prefix_pattern += number_to_symbol[number_for_symbol]
            prefix_index -= number_for_symbol*(4**i)  #vom prefix index muss die aktuelle potenz abgezogen werden
        pattern=prefix_pattern + number_to_symbol[last_number_value]

    return pattern
print(number_to_pattern(int (index_input),int (k_input)))
            
            
