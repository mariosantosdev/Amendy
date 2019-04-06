from libs import amendy # Biblioteca personalizada

import wikipedia # API Wikipedia
import pyttsx3 # Converter texto em voz
import pybrackets.pybrackets as pybrackets # Limpar a string wikipedia
import clipboard # Copiar o texto

# Variaveis
wikipedia.set_lang('pt')

amendy.clearTerminal()
try:
    quest = input('Pesquisa: ')
    content = wikipedia.summary(quest)
except wikipedia.exceptions.PageError:
    print('Pagina nao encontrada')
    exit()

response = pybrackets.clearString(content)
print(response)
