

#float = numero com decimal
#int = numero inteiro
#str = String - conjunto de carateres
#Type = tipo de conteudo (str / float / int.... )
#bool = True or false

#name, age, color, branco = "Leandro", 23, Azul, True
#print(name +age +color +branco)


#Contas*****************************************************************************************
#int = 21
#int += 5
#print(int)  ===== 26

#***********************************************************************************************

#######
############# ****** Funções ***********
#######

#print(name)  Funciona
#print = name   Nao funciona ( Fica como se print = a uma Variavel )

#print (len(name))         #Quantidade de Caracteres
#print(name.find("d"))     #Localizacao na String = Começa em zero, um , dois..... lean"D" = 4
#print(name.capitalize())  #Primeira aparicao na String aparece em maiusculo = "L"eandro
#print(name.upper())       #Tudo Maiusculo
#print(name.lower())       #Tudo Minusculo

#print(name.isdigit())     #Digito / numero ?
#print(name.isalpha())     #Alfatetico ?
#print(name.count("o"))    #Quantidade de o´s
#print(name.replace("l","24"))  #Substitui
#print(name*3)             #Multiplica 

#######
############# ***************************
#######







##
###  *************** Exe 1 ************************+
##
"""
name=str("Leandro")
name = "leandro Cardoso"
print(name)


altura = 176.5
print("Eu meço ")
print("Eu meço: "+str(altura))
print("Eu meço: "+str(altura)+" centimetros")
print(type(altura))

##*
###  *************** Exe 2 ************************
##

Monitor, idade, casaT3 = "AOC", 23, True

Eu = Ela = Ele = Eles = 30
"""
##
###  *************** Exe 3 ************************
##
"""
print (len(name))         #Quantidade de caracteres

print(name.find("d"))     #Nota = Começa em zero

print(name.capitalize())  # Primeira aparição em Maiusculo

print(name.upper())       #Tudo Maiusculo
print(name.lower())       #Tudo Minusculo

print("O meu nome é composto por digitos ?")
print(name.isdigit())     #Digito / numero ?

print("O meu nome é composto por Letras ?")
print(name.isalpha())     #Alfatetico ?

print(name.count("o"))    #Quantidade de o´s
print(name.replace("o","24"))  #Substitui
print(name*3)             #Multiplica 
"""
##
###  *************** Exe 4 ************************
###  ************ Type Casting ********************          # Converter data de um tipo em outro
###  *************** Exe 4 ************************
##
"""
idade1 = 2      #int
idade2 = 45.4   #float  
idade3 = "4"    #str

idadeSoma = idade1+int(idade2)+int(idade3)          #Conversao para Inteiros
print(idadeSoma)
"""

##*
###  *************** Exe 5 ************************   #Inputs   
##                                                    Nota: Vem sempre como String , necessario converter
"""
input("Qual é o meu nome do meio?: ")

NomeMeio = input("Qual é o meu nome do meio?: ")
print(NomeMeio)

DiaHoje = int(input("Qual é o dia de Hoje?: "))
Amanha = DiaHoje + 1
print("Amanha é dia "+str(Amanha))          #Nao esquecer converter Int de "Amanha" para String para poder fazer print a tudo
"""
##
###  *************** Exe 6 ************************      MATEMATICA
##                                              

import math
"""
pi = 3.14
Num24 = 24
Num25 = 25
Num26 = 26


print(round(pi))           #Numero redondo
print(math.ceil(pi))       #Arredonda para cima , ou seja 3.14 passa a 4
print(math.floor(pi))      #Arredonda para baixo, ou seja 3.14 passa a 3
print(abs(pi))             # Quanto falta para 0 ?  No caso da variavel ser um numero negativo, fica positivo por falta 3.14 para 0  / Numero Absoluto /
print(pow(pi,2))           # Elevado a:
print(math.sqrt(27))       # Raiz Quadrada

print(max(Num24,Num25,Num26))   # Numero maior
(min(Num24,Num25,Num26))   # Numero Menor
"""
##
###  *************** Exe 7 ************************         Dividir uma String  # [x,y,z] em que x = start point, y = end point , z = steps
##  
"""
Nombre =  "Leandro Cardoso"
PrimeiroNome = Nombre[3]              #Seleciona o representativo de index 3 na string (Comeca sempre em 0)
print(PrimeiroNome)

PrimeiroNome = Nombre[0:7]            #Seleciona o representativo dos priemrios 8 digitos
PrimeiroNome = Nombre[:7]            #igual
print("First name is "+PrimeiroNome)

print("Nome dividido por steps é "+Nombre[0:15:2])   # Divide a variavel de 2 em 2... 3 em 3...
                                                     # [x,y,z] em que x = start point, y = end point , z = steps

reversed_Nombre = Nombre[::-1]
print("O meu nome invertido é "+reversed_Nombre)
"""
##
###  *************** Exe 7.1 ************************         Dividir uma String  
#
"""
website = "http://localhost.com"
website2 = "http://google.com"

slice = slice(7,-4,1)     # Corta .com e http

print(website[slice])
print(website2[slice])
"""
##
###  *************** Exe 8 ************************         Condições if e Else
#

"""
Age = int(input("I old are you? "))        #Nota assim faz so a primeira condicao correta
if Age >= 18:
    print("Verdade")
elif Age == 100:
    print("Senior")
elif Age < 0:
       print("Esquece")
else:
   print("Mentira")

"""

##
###  *************** Exe 8.1 ************************         Logic Logica   (and,or,not)
#
"""
Age = int(input("I old are you? "))        #Nota assim faz so a primeira condicao correta
if Age >= 18 and Age <= 30 or Age >= 40 and Age <=50: 
   print("Prime Time ")

if not(Age >= 18 and Age <= 30 or Age >= 40 and Age <=50):
   print("Odd Time")

"""
##
###  *************** 9 ************************         Loop   while loop (unlimited)        Nao para enquanto a afirmacao nao for verdade , neste caso ate escrever algo
#

"""
Quantity = None
      
while not Quantity:                                    
    Quantity = input("Enter your quantity: ")

print("tyty")

"""

##
###  *************** 10 ************************        For loop For (limited)    exe:for i in range(50, 100+1)  em que 50 = number inclusive, 100 = number exclusive
##                                                                                                     Pode ter step (,,2)
#

"""
for i in range(10):
    print(i+1)


for i in "Leandro":
  print(i)

for seconds in range (10,0,-1):                    #Contagem decrescente   
    print(seconds)
    time.sleep(1)                                   # EM segundos / verificar posicao caso esteja em for ou while
"""

##
###  *************** 11 ************************      # Nested loop  - 1 loop dentro de outro  / loop inside loop
#

"""

rows = int(input("How many rows: "))
columns = int(input("How many columns: "))
symbol = input("Enter a symbol to use: ")

for i in range(rows):                 # For each Row, write X symbols according to number of columns ou seja, a fazer a primeira row, vai fazer todas as colunas... 
    for j in range(columns):
        print(symbol, end="")
    print()

"""

##
###  *************** 12 ************************       Loop Control Statements  Break, continue, pass
#

"""

while True:
    name = input("Enter name: ")               #used to terminate the loop entirely
    if name != "":                       
        break

Number = "4510-707"

for i in Number:                               # Retirar os "-"  Skips to the next iteration of the loop
    if i == "-":
        continue
    print(i, end="")



for i in range(1,21):                 # Pass acts as a place holder ou seja, faz skipp ao 13
    
    if i == 13:
        pass
    else: 
        print(i)

"""

##
###  *************** 13 ************************       Lists   Listas , used to store multiple items
#

"""
food = ["onion", "orange", "blueberry","water"]    #começa em 0 ,  

food[3] = "kebab"
print(food[3])

for x in food:
    print(x)

food.append("soda")                          #Adicionar a lista
food.remove("orange")                        # Remove X
food.pop()                                   # Remove o ultimo
food.insert(0,"cake")                        # Adiciona na posição X, a new value
food.clear()                                 # Limpa a lista

"""

##
###  *************** 13.1 ************************       2D lists / multidimensional lists listas , lists inside lists
#
"""
drinks = ["soda" , "water", "milk"]
dinner = ["fish", "meat", "soop"]
dessert = ["cake", "wine"]

food = [drinks, dinner, dessert]

print(food[1][2])   # Vai buscar soop
"""

##
###  *************** 14 ************************       Tuple     Collection which is ordered and unchabgeable   ######1.32.50
#

##testetesteteste teste outra vez








##
###  *************** 15 ************************       
#

##
###  *************** 16 ************************       
#

##
###  *************** 17 ************************       
#