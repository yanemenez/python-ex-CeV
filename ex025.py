#Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.

name = str(input('Qual é o seu nome completo?')).strip()
print(f'Seu nome tem silva? {'SILVA' in name.upper()}')



