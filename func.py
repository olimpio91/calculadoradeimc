def imc(peso, altura):

    calculo = peso / (altura ** 2)

    if calculo <= 18.5:
        return "Baixo peso"
    
    elif calculo >= 18.5 or calculo <= 24.9:
        return 'Peso normal'
    
    elif calculo >= 25 or calculo <= 29.9:
        return 'Sobrepeso'
    
    elif calculo >= 30 or calculo <= 34.9:
        return 'Obesidade grau 1'
    
    elif calculo >= 35 or calculo <= 40:
        return 'Obesidade grau 2'


    elif calculo >= 40:
        return 'Obesidade grau 3'

    
    return 

print(imc(peso = float(input('Qual seu peso? :')), altura = float(input('Qual sua altura? :'))))