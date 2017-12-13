'''=================EP02===================='''
'''
FATEC S�O JOSE DOS CAMPOS
CURSO DE ANALISE E DESENVOLVIMENTO DE SISTEMAS
ALGORITMOS E LOGICA DE PROGRAMAÇAO
PROFESSOR FERNANDO MASSANORI
ALUNOS: Michele Cristina Nunes da Silva
'''
'''=========================================='''



import random # Importa a funcao que permite a escolha aleatoria de uma palavra.
import urllib.request # Importa a biblioteca que permite fazer requisicoes a uma URL.



'''=================DECLARACAO DE VARIAVAVEIS GLOBAIS==============='''
erradas = ''
certas = ''
contErros = 0
sorteada = ''
possibilidades = 'abcdefghijklmnopqrstuvwxyzáâãéêíóôõúç'    #Variavel com letras possiveis para chutar.
resultado = False

   

'''===============SORTEIO DA PALAVRA===================='''
''' Funcao que sorteia uma palavra do dicionario e checa se sao menor ou igual a 5.
Caso seja, sorteia outra palavra, caso contrario, retorna a palavra:'''
def sorteia():
  # Abre a url, la, decodifica seus valores para latim-1:
  resposta = urllib.request.urlopen('http://www.ime.usp.br/~pf/dicios/br')
  html = resposta.read()
  decodifica = html.decode('iso-8859-1')

  # Converte as letras para minusculas e divide a lista de palavras lidas na URL pelos espacos:
  minuscula = decodifica.lower()
  divide = minuscula.split()

  sorteada = random.choice(divide) #Escolhe aleatoriamente uma palavra da lista ja� dividida.

  # Verifica se a palavra sorteada tem mais que 5 letras e sorteia nova palavra caso seja menor.
  while len(sorteada) <= 5:
    sorteada = random.choice(divide)
  
  return sorteada

def perde():
  resultado = win()
  escolha = again()
  if resultado == False:
    again()
  if escolha == True:
    print ("Aguarde um momento enquanto sorteamos uma nova palavra.")
    iniciar()
  else:
    print("Que pena que voce parou!")
  exit()


  

'''========================DESENHA============================='''
'''Funcao que imprime na tela o desenho da forca e seu progresso.'''
def desenha():
  forca=['''
   +-----+
   |     |
         |
         |
         |
         |
============''','''
   +-----+
   |     |
   O     |
         |
         |
         |
============''','''
   +-----+
   |     |
   O     |
   |     |
         |
         |
============''','''
   +-----+
   |     |
   O     |
  /|     |
         |
         |
============''','''
   +-----+
   |     |
   O     |
  /|\    |
         |
         |
============''','''
   +-----+
   |     |
   O     |
  /|\    |
  /      |
         |
============''','''
   +-----+
   |     |
   O     |
  /|\    |
  / \    |
         |
============''']
  if contErros == 0:
    print(forca[0])
    print ("\nChutes errados:%s" %(erradas))
  if contErros == 1:
    print(forca[1])
    print ("\nChutes errados: %s" %(erradas))
  if contErros == 2:
    print(forca[2])
    print ("\nChutes errados: %s" %(erradas))
  if contErros == 3:
    print(forca[3])
    print ("\nChutes errados: %s" %(erradas))
  if contErros == 4:
    print(forca[4])
    print ("\nChutes errados: %s" %(erradas))
  if contErros == 5:
    print(forca[5])
    print ("\nChutes errados: %s" %(erradas))
  if contErros == 6:
    print(forca[6])
    print ("\nChutes errados: %s" %(erradas))
    print("\nVOCE FOI ENFORCADO!!!")
    perde()
  
'''============================CHUTE DAS LETRAS=============================='''
''' Função que verifica se o caracter digitado sao valido.
Caso seja, acrescenta o novo chute �a string de Letras.
Com base na string de possibilidades, verifica que as letras coincidam com aquela.
Caso coincidam, para cada letra coincidente em letras, substitue por um espaco
e o resultado sera� uma nova string de possibilidades apenas com as letras ainda nao usadas.'''
def chute(letras):
  global certas
  global sorteada
  global contErros
  global erradas
  global possibilidades
  while contErros < 7 and set(certas) != set(sorteada):
    palpite = input("\nDigite uma letra: ").lower()   # Variavel de input de chutes.
    if len(palpite) > 1:   # SE1 o chute for maior que 1 ou nao for letras, pede que usuário tente outra letra.
      print("\nDigite uma letra apenas.")
    else:                                           #SENAO1...
      desenha()                               #Chama a funcao desenha atualizada com os chutes.
      if palpite not in letras:   #Se o chute nao foi feito antes, adiciona à 'letras'.
        letras = letras + palpite
      if palpite in sorteada:     #SE2 o chute coincide com uma letra da 'sorteada', adiciona às 'certas' e...
        certas = certas + palpite
        for c in sorteada:        #Para o índice que coincide, SE3 em 'certas'...
          if c in certas:
            print (c, end = ' ')  #Imprime a letra que coincide.
          else:
            print ('_', end = ' ')#SENAO3 imprime um _ no lugar das que nao coincidem.
      else:                       # SENAO2, adiciona �as 'erradas'...
        for c in sorteada:        #Para o indice que coincide, SE3 em 'certas'...
          if c in certas:
            print (c, end = ' ')  #Imprime a letra que coincide.
          else:
            print ('_', end = ' ')#SENAO3 imprime um _ no lugar das que nao coincidem.
        erradas = erradas + palpite
        contErros += 1      # Incrementa o contador de erros.
      for palpite in possibilidades: # Verifica quais as letras ainda nao foram utilizadas.
        if palpite in letras:       #Se o chute ja� estiver em letras, é pq ja foi usado, então substitui a letra por um ''(vazio).
          possibilidades = possibilidades.replace(palpite,'')
          print ('\n\n Voce ainda nao tentou:\n', possibilidades)
  return possibilidades



'''======================JOGAR NOVAMENTE=========================='''
''' Funcao que verifica se a pessoa deseja jogar de novo: '''
def again():
    escolha = input("Deseja jogar novamente(S/N)? ")
    if escolha == "s" or escolha == "S":
      return True
    if escolha == "n" or escolha == "N":
      return False
    else:
      print("Digite 'S' para sim ou 'N' para nao.")
      again()

      

'''===========================VENCEU============================='''
''' Funcao que anuncia se o jogador venceu ou perdeu o jogo, comparando
o set de palavras de 'certas' com o set de 'sorteada'.'''
def win():
  while set(certas) == set(sorteada):
    return True



'''=====================INICIAR================================='''
def iniciar():
  global erradas
  erradas = ''
  global certas
  certas = ''
  global contErros
  contErros = 0
  global sorteada
  sorteada = ''
  sorteada = sorteia()
  print("\nA palavra ja� foi sorteada e contém %i letras.\n Vamos jogar!" %(len(sorteada)))
  chute('')


  
'''=============INICIO DO JOGO================='''
print ("Jogo da Forca")
iniciar()
resultado = win()
escolha = again()
if resultado == True:
  print ("Parabens!!! Voce acertou!")
  escolha = again()
else:
  print("Que pena que voce parou!")
def perde():
  resultado = win()
  escolha = again()
  if resultado == False:
    again()
  if escolha == True:
    print ("Aguarde um momento enquanto sorteamos uma nova palavra.")
    iniciar()
  else:
    print("Que pena que voce parou!")
  exit()
