def add_zero(friccao: set, possible_variables: list):
    new_friccao = set()
    for item in friccao:
        item = str(item).split("'")[0]

        if (len(item) < len(possible_variables)):
            item = '0'*(len(possible_variables)-len(item)) + str(item)

        new_friccao.add(item)

    return new_friccao

def adjust_confianca(friccao_otimizada: set, last_element_friccao: set):

    if(last_element_friccao == friccao_otimizada):
        return friccao_otimizada
    else:
        new_item = set()

        for item in last_element_friccao:

            var = str(item).split("'")[0][:2]
            conf = str(item).split("'")[0][-3:]

            for x in friccao_otimizada:
                    x_var = str(x).split("'")[0][:2]
                    x_conf = str(x).split("'")[0][-3:]
                    
                    new_x = x_var

                    if(x_var == var):
                        print(x_conf)
                        print(conf)
                        z = zip(conf, x_conf)
                        for a, b in z:
                            if((a != '0') & (b != '0')):
                                new_x += '0'
                            else:
                                new_x += str(b)
                    else:
                        new_x += x_conf

                    new_item.add(new_x)        
            
    return new_item