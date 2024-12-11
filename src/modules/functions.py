import itertools
import math
from ..modules import errorhandler

def evaluate(friccao, variable_values):

        for variable, value in variable_values.items():
            friccao = friccao.replace(variable, str(value)) 

        return eval(friccao)

def friccao_results(friccao, possible_variables):
            
        results = []
        try:    
            for combination in itertools.product([False, True], repeat=len(possible_variables)):
                    row = dict(zip(possible_variables, combination)) # gera combinacoes de linhas da tabela
                    row['Result'] = evaluate(friccao, row) # calcula valor da linha para a expressao
                    results.append(row['Result'])
            return results
        except Exception:
            raise errorhandler.InvalidExpression()      
            

def minterms(results):
        minterms = []

        for i in range(len(results)):
            if(results[i] != 0):
                minterms.append(i)
        return minterms

def remove(a,b):
    for i in a[:]:
        if i in b:
            b.remove(i)

# def response_formatter(response,possible_variables):
#     answer = []
#     for x in response:
#         term = []
#         a = zip(possible_variables, list(x))
#         for key, value in (dict(a).items()): 
#             if(value == '1'):
#                 term.append(key)
#             elif(value == '0'):
#                 term.append('('+'NOT '+key+')')
#             product = ' AND '.join(term)
#         answer.append('('+product+')')    

#     answer = ' OR '.join(answer)
#     return answer

def response_formatter(response,possible_variables): # ALTERNATIVO
    answer = []
    for x in response:
        term = []
        a = zip(possible_variables, list(x))
        for key, value in (dict(a).items()): 
            if(value == '1'):
                term.append(key)
            elif(value == '0'):
                term.append(key+ "'")
            product = ''.join(term)
        answer.append(' '+product+' ')    

    answer = '+'.join(answer)
    return answer

def replacer(expression):
    expression = expression.replace("AND","and")
    expression = expression.replace("OR","or")
    expression = expression.replace("NOT","not")

    return expression

def findcontexto(friccao):
    friccao = friccao.replace("and","")
    friccao = friccao.replace("not","")
    for item in set(list(friccao)):
        if item in ['L','N']:
            return True
    return False

def xyzcounter(friccao):
    variables = set(list(friccao))
    for item in variables:
        if item in ['X','Y','Z']:
            return 3
            
def substitui_mintermo(R1: list,R2: list, xyzcount: int):
    
    for m2 in R2:
        I = math.floor(m2/(2**xyzcount))*(2**xyzcount)
        F = math.floor(I + 2**xyzcount - 1)
        for m1 in R1:
            if(m1 >= I and m1 <= F):
                if(m1 != I or m1 == m2):
                    R1.remove(m1)
                if(m2 != F and m2 != m1):
                    sub = (m1 & (~m2)) + I
                    if(m1 != I):
                        # print("R1 antes: ", R1)
                        R1.append(sub)
                        break
                        # print("R1 depois: ", R1)
                        
    R1 = sorted(R1)
    return R1