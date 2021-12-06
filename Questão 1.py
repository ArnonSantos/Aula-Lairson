csm = float(input('Insira seu consumo mensal em KWh:  '))

csmv = float(input('Caso o seu estado esteja em bandeira vermelhar informe aqui o valor, caso não cobre insira 0: '))

cs = 100
#bandeira vermelha
if(0 < csmv < 4):
    print('Seu consumo na bandeira vermelha em reais é de: ', (cs * 0.90) + ((csm - 100 )* 3.971))

# bandeira verde
elif(csm < 100):
    print('Seu consumo na bandeira verde em reais é de: ', csm * 0.90)

# bandeira verde ate 100KWh
elif(csm == 100):
    print('Seu consumo na bandeira verde em reais é de: ', csm * 0.90)

# bandeira amarela
elif(csm > 100):
    print('Seu consumo em reais na bandeira amarela é de: ', (cs * 0.90) + ((csm - 100 )* 1.874))
