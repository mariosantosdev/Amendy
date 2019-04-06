from libs import amendy # Biblioteca personalizada

import wikipedia # API Wikipedia
import pyttsx3 # Converter texto em voz
import pybrackets.pybrackets as pybrackets # Limpar a string wikipedia
import clipboard # Copiar o texto

# Variaveis
wikipedia.set_lang('pt')
voice = pyttsx3.init()
op = 0

amendy.clearTerminal()
try:
    quest = input('Pesquisa: ')
    content = wikipedia.summary(quest)
except wikipedia.exceptions.PageError:
    print('Pagina nao encontrada')
    exit()

response = pybrackets.clearString(content)
print(response)

while op != 4:
    op = int(input('\nO que deseja fazer...\n[ 1 ] Copiar texto\n[ 2 ] Falar o texto\n[ 3 ] Criar arquivo\n[ 4 ] Sair\n>> '))
    if op == 1:
        clipboard.copy(response)
        print('Texto copiado\n')
    elif op == 2:
        voice.say(response)
        voice.runAndWait()
        print('\n')
    elif op == 3:
        amendy.createFile(response, quest)
        print('Arquivo criado\n')
    elif op == 4:
        print('Ate mais!')
        exit()
    else:
        print('Escolha uma das opcoes abaixo!')
