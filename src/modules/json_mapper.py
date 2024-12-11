def json_mapper(friccao,output): 
    contexto = {
        "noite": [],
        "localConfiavel":[],
        "cadastrado": [],
        "tempoCadastro": 0,
        "nivelConfianca": []
    }
    
    # # Todas as variaveis
    # fric1 = list(friccao)[0:3]
    # fric2 = str(list(friccao)[3]+list(friccao)[4])
    # fric3 = list(friccao)[5:]
    # context1 = list(contexto)[0:3]
    
    # # possible_variables = ['L','C','D','S']
    # fric1 = list(friccao)[0:2]
    # fric2 = str(list(friccao)[2]+list(friccao)[3])
    # context1 = list(contexto)[1:3]

    # possible_variables = ['N','L','X','Y','Z']
    fric1 = list(friccao)[0:2]
    fric3 = list(friccao)[2:]
    context1 = list(contexto)[0:2]


    a = zip(context1,fric1)

    for key, value in (dict(a).items()):  
        if(value == '1'):
            contexto[key].append(True)
        elif(value == '0'):
            contexto[key].append(False)
        else:
            contexto[key].append(True)
            contexto[key].append(False)
     
    # # Mapeador Dia/Semana
    # match fric2:
    #     case "10": # DS'
    #         contexto["tempoCadastro"] = 1
    #         try: contexto["cadastrado"].remove(False)
    #         except: pass
    #     case "01": # D'S
    #         contexto["tempoCadastro"] = 7
    #         try: contexto["cadastrado"].remove(False)
    #         except: pass
    #     case "11": # DS
    #         contexto["tempoCadastro"] = 7
    #         try: contexto["cadastrado"].remove(False)
    #         except: pass
    #     case "-1": # S
    #         contexto["tempoCadastro"] = 7
    #         try: contexto["cadastrado"].remove(False)
    #         except: pass
    #     case "1-": # D
    #         contexto["tempoCadastro"] = 1
    #         try: contexto["cadastrado"].remove(False)
    #         except: pass
    #     case _: # caso default
    #         contexto["tempoCadastro"] = 0

    
    for x in range(len(fric3)):
        if(fric3[x] != '0'):
            contexto["nivelConfianca"].append(x+1)
    contexto["nivelConfianca"] = list(dict.fromkeys(contexto["nivelConfianca"]))


    output['contexto'].append(contexto)

    return output