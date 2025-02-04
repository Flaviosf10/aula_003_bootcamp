### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

valor = input('Digite um valor válido do produto: ')
quantidade = input('Digite a quantidade: ')
valor_decimal = valor.split('.')

if valor_decimal[0].isdigit() and  valor_decimal[1].isdigit() and quantidade.isdigit():
    
    print('Dados válidos!!')
    print(valor)
    print(quantidade)
else:
    print ('Dados incorretos!!')