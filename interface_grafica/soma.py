''' Criando uma interface de login
 e cadastro completo em python 
 utilizando Tkinter'''
# obs:
# Para trabalhar com servidores locais,utilizam o SQLite
# Para trabalhar com servidores que não são locais,se utiliza outros bancos,
# a exemplo do MySQL;
# Primeiro,vamos aprender a usar o Tkinter

from tkinter import *

# Criando a função de soma;
def Somar():
    n1 = int(num_1.get())
    n2 = int(num_2.get())
    soma = n1 + n2
    mostrar['text']  = soma

    
# Criando uma janela instanciando tk e fechando o loop com 'mainloop()'
root = Tk()                 # 'root' é um nome para chamar de tela; Root agora é uma instância de tk
root.geometry('400x400')    # Definindo o tamanho da tela.
root.title('SOMA')

# Como interagir com a janela? Criando algo dentro dela.
# row = linha ; column = coluna:
# Toda variável que tem o entry, não recebe parâmetro,pq pra pegar o resultado dessa
# variável,utiliza-se o comando '.get()'

num_1 = Entry()
num_1.grid(row = 0, column = 0)

num_2 = Entry()
num_2.grid(row = 1, column = 0)

# Criando botão:
Button(text = 'Somar', command = Somar).grid(row = 2, column = 0)

# Para mostrar o resultado da soma na tela:

mostrar = Label(text= 'Resultado')
mostrar.grid(row = 3, column = 0)

root.mainloop()
