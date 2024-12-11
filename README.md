# Otimizador Completo

O programa aplica o algoritmo de Quine-McCluskey sobre uma equação booleana e entrega a solução otimizada para o problema.

# Como utilizar?

## Inicializando o código
```
python3 app.py
```

## Variáveis e operações aceitas

As variáveis permitidas como entrada no programa são definidas em `src > otimizador.py`, sob a [lista correspondente](https://github.com/brunolima2696/otimizador_completo/blob/339c0f60636665cf434480963c3428cea89f65dd/src/otimizador.py#L10)

As operações aceitas pelo programa são AND,OR e NOT. Um exemplo de entrada é:

```
(X OR Y) AND (X OR Z)
```

Que resulta no conjunto de saídas:

```
R: 
[[3, 4, 5, 6, 7, 11, 12, 13, 14, 15, 19, 20, 21, 22, 23, 27, 28, 29, 30, 31]]

Friccoes:
[{'--1--', '---11'}]

Expressoes:
[' X + YZ ']
```

## Explicando cada uma das saídas

A lista `R` representa a posição dos mintermos da solução otimizada.

A lista de sets `Fricções` representa cada uma das expressões na saída do algoritmo, com `OR` lógicos entre cada elemento do set `{'--1--'} OR {'---11'}`, e `AND` lógico entre cada item do elemento `'X' ,'Y AND Z'`. `1` representa variáveis sem negação, `0` representam variáveis negadas e `-` representam dontcares.

A lista de equações `Expressões` representa, num formato legível de equações booleanas, a lista de `Fricções`.