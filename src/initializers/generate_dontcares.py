from ..modules import functions

var = ['N','L','C','D','S','U','W','X','Y','Z']

friccao = '((NOT X) AND (Z OR Y) AND (U OR W)) OR ((U AND (NOT W)) AND X) OR (X AND (NOT Y) AND Z)'
    
friccao = functions.replacer(friccao)

ones = functions.minterms(functions.friccao_results(friccao, var))

#Gerar/Escrever dontcares
file = open("dontcares.txt","a")
for item in ones:
    file.write("%s\n" %item)
file.close()