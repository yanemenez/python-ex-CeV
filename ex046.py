#Faça um programa que mostra na tela uma contagem regressiva para estouro de fogos de artifício,
#indo de 10 até 0, com uma pausa de 1 segundo entre eles.


from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(0.5)
print('BUM, BUM, BUM!')