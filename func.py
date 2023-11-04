def imc(peso, altura):

    calculo = peso / (altura ** 2)

    print(calculo)

    if calculo < 18.5:
        return "Baixo peso"
    
    elif calculo >= 18.5 and calculo <= 24.9:
        return 'Peso normal'
    
    elif calculo > 25.0 and calculo <= 29.9:
        return 'Excesso de peso'
    
    elif calculo > 30.0 and calculo <= 34.9:
        return 'Obesidade de classe 1'
    
    elif calculo > 35.0 and calculo <= 39.9:
        return 'Obesidade de classe 2'
    
    return 'Obesidade de classe 3'
    
print(imc(peso = float(input('Qual seu peso ? :')), altura = float(input('Qual sua altura ? :'))))