import sys
from .modules import functions
from .modules import json_mapper
from .modules import output_fixer
from .modules import errorhandler
from .quine_mccluskey.qm import QuineMcCluskey
import json

# possible_variables = ['N','L','C','D','S','U','W','X','Y','Z']
possible_variables = ['L','N','X','Y','Z']

dontcares = []
# dontcares_file = open("initializers/dontcares.txt","r")
# for line in dontcares_file:
#     x = line[:-1]
#     dontcares.append(int(x))

v0 = []
# v0_file = open("initializers/v0.txt","r")
# for line in v0_file:
#     x = line[:-1]
#     v0.append(int(x))

R_list = []
# R_list.append(v0)

while True:
    
    while True:
        
        friccao = input("Nova friccao: ")
        if friccao.lower() == 'exit':
            print("Saindo. \n")
            sys.exit()

        friccao = functions.replacer(friccao)
        
        try:
            ones = functions.minterms(functions.friccao_results(friccao, possible_variables))
            break
        except errorhandler.InvalidExpression as e:
            print(f"Ocorreu um erro: {e} \n")

    R_list.append(ones)
    xyzcount = functions.xyzcounter(friccao)

    if(functions.findcontexto(friccao) == True):
        for i in range(len(R_list)-1):
            functions.substitui_mintermo(R_list[i],ones,xyzcount)
    else:
        for i in range(len(R_list)-1):
            functions.remove(ones,R_list[i])      
        

    expressoes = []
    friccoes = []
    qm = QuineMcCluskey()
    file = open("saidas.json","w").close()
    file = open("saidas.json","a")
    jsonOutput = []
    
    # last_element = R_list[-1]
    # last_element_friccao = qm.simplify(last_element, dontcares)
    # last_element_friccao = output_fixer.add_zero(last_element_friccao,possible_variables)

    for element in R_list:
        if element:
            friccao_otimizada = qm.simplify(element, dontcares)
            friccao_otimizada = output_fixer.add_zero(friccao_otimizada,possible_variables)
            # friccao_otimizada = output_fixer.adjust_confianca(friccao_otimizada,last_element_friccao)

            expressao_formatada = functions.response_formatter(friccao_otimizada,possible_variables)
            output = {
                "ID": expressao_formatada,
                "friccao": R_list.index(element), 
                "contexto":[]
            }
                    
            for x in friccao_otimizada:
                json_mapper.json_mapper(x,output)

            friccoes.append(friccao_otimizada)
            expressoes.append(expressao_formatada)
            jsonOutput.append(output)
    file.write(json.dumps(jsonOutput,indent=3))
    file.close()

    filtered_R_list = list(filter(None,R_list))

    
    print('R: ')
    print(filtered_R_list, '\n')
    print('Friccoes: ')
    print(friccoes, '\n')
    print('Expressoes: ')
    print(expressoes, '\n')