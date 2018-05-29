#Implement pattern to number

pattern=input("DNA string hier einfügen")
prefix=pattern[0:-1]                            #prefix wird definiert als der String von der ersten Base bis einschließlich zur vorletzten Base (hat dann Index -2)
last_symbol=pattern[-1]                         #das letzte Symbol ist die Base am Index -1

def symbol_to_number(symbol):                   #definieren der Funktion Symbol_to_number, durch die A,C,G und T je einen Integer zugewiesen bekommen 
    if symbol == "A":
        return 0
    if symbol == "C":
        return 1
    if symbol == "G":
        return 2
    if symbol == "T":
        return 3

def pattern_to_number_prefix(prefix):           #definieren der Funktion pattern_to_number_prefix, die die umgewandelte Nummer des Präfixes zurückgibt
    if len(prefix) == 0:
        return 0
    else:
        prefix_number=0                         #definieren der Variable prefix_number; muss definiert sein, damit man was drauf addieren kann
        for i in range(0,len(prefix)):          #für alle Werte i zwischen 0 und dem Ende des Präfixes (bzw. der vorletzten Zahl)
            prefix_number += symbol_to_number(prefix[len(prefix)-i-1])*4**(i+1) #Berechnung der Nummer des Präfixes: multipliziere das symbol_to_number des von rechts ersten Buchstaben des Präfixes mit 4**n, wobei 4 die Basis ist (da wir im 4er Zahlensystem sind) und n das "Gewicht", also die Position von hinten (i+1)
        return prefix_number

def pattern_to_number(pattern):
    if len(pattern) == 0:
        return 0
    if not pattern == 0:
        
        return pattern_to_number_prefix(prefix) + symbol_to_number(last_symbol)

print(pattern_to_number(pattern))        
