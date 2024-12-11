# Otimizador Completo

O programa aplica o algoritmo de Quine-McCluskey sobre uma equação booleana e entrega a solução otimizada para o problema.

# Como utilizar?

## Inicializando o código
```
python3 app.py
```

## Variáveis e operações aceitas

As variáveis permitidas como entrada no programa são definidas em `src > otimizador.py`, sob a [lista correspondente](https://github.com/brunolima2696/otimizador_completo/blob/339c0f60636665cf434480963c3428cea89f65dd/src/otimizador.py#L10) e as operações aceitas pelo programa são `AND`, `OR` e `NOT`. 
 
> ⚠️  utilizar variáveis não definidas ou operações não aceitas resulta em erro.

Um exemplo de entrada é:

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

A lista `R` representa para cada saída na solução otimizada, a lista de mintermos correspondente.

A lista de sets `Fricções` representa cada uma das expressões na saída do algoritmo, com `OR` lógico entre cada elemento do set `{'--1--'} OR {'---11'}`, e `AND` lógico entre cada item do elemento `'X' , 'Y AND Z'`. `1` representa variáveis sem negação, `0` representam variáveis negadas e `-` representam dontcares.

A lista de equações `Expressões` representa, num formato legível de equações booleanas, a lista de `Fricções`.

## Adicionando novas equações

Conforme novas entradas são inseridas, o algoritmo é novamente aplicado sobre elas e sobre entradas pré-existentes, modificando-as conforme as regras de interação entre fricções que foram definidas para o problema.

Se, em adição à equação do exemplo anterior `(X OR Y) AND (X OR Z)` for adicionada a entrada `X AND Y AND Z`, a nova saída do programa será:

```
R: 
[[3, 4, 5, 6, 11, 12, 13, 14, 19, 20, 21, 22, 27, 28, 29, 30], [7, 15, 23, 31]]

Friccoes:
[{'--011', '--10-', '--1-0'}, {'--111'}]

Expressoes:
[" X'YZ + XY' + XZ' ", ' XYZ ']
```

Contendo, agora, duas listas em cada uma das saídas, com o primeiro item - que representa a saída da primeira entrada - modificado pela inserção da segunda.