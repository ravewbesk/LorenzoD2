import aforca
import adivinhe

print('*****************************************')
print('----------- Escolha seu Game! -----------')
print('*****************************************')

print('\n(1) Forca \n(2) Adivinhe o número')
jogo = int(input('Qual vai ser o game? '))

if (jogo == 1):
    print('GG Forca')
elif (jogo == 2):
    adivinhe.gg()

