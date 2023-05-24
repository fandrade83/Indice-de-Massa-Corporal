peso = float(input('Whal é o seu peso? (Kg) '))
altura = float(input('Qual é a sua altura? (m) '))
imc = peso / (altura ** 2)
print('O Imc dessa pessoa é de {:.1f}'.format(imc))
if imc < 18.5:
    print('O IMC esta ABAIXO DO PESO normal')
elif 18.5 <= imc < 25:
    print('PARABENS,  Voce esta na faixa de PESO NORMAL')
elif 25 <= imc < 30:
    print('Voce esta em SOBREPESO')
elif 30 <= imc < 40:
    print('Voce esta en OBESIDADE, CUIDADO!')
elif imc >= 40:
    print('Voce Esta em OBESIDADE MORBIDA, CUIDADO!')
