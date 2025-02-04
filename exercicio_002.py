### Exercício 2: Classificação de Dados de Sensor
# Imagine que você está trabalhando com dados de sensores IoT. 
# Os dados incluem medições de temperatura. Você precisa classificar cada leitura 
# como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

temperatura = 61

if temperatura <= 20:
    print ('Baixa temperatura')
elif temperatura <= 50:
    print('Temperatura moderada')
elif temperatura <=70:
    print('Temperatura alta')
else:
    print ('Temperatura alta')
