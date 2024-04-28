

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
###  *************** 14 ************************       Tuple     Collection which is ordered and unchangeable   ######1.32.50
#
"""
applier = ("Bro" , 21, "male")

print(applier.count("Bro"))       #Return number of Bro´s
print(applier.index("male"))      #Return Position / Index (ter em conta que começa em 0 sempre)

for x in applier:                 #Return all the data inside the Tuple
    print(x)

if "Bro" in applier:              #Confirm if "Bro" is in Tuple 
    print("Bro inside")
"""

##
###  *************** 15 ************************       SET    acts like a List but has no order or index, which means when print they dont always come the same position
#                                                             U can see whats different between 2 Set´s and put together without a specific order

"""
clothesup = {"belt", "gloves", "t-shirt","jacket"}
clothesdown = {"belt","pants","boots", "socks"}

#clothesup.add("something")
#clothesdown.remove("boots") 
#clothesup.clear()
#clothesup.update(clothesdown)                                  #Add one Set to another, adds all of clothes down to clothes up
#clothesall = clothesup.union(clothesdown)                      #Create one Set interally different with both other Sets

print(clothesup.difference(clothesdown))                       # what clothesup has that clothesdown does not
print(clothesup.intersection(clothesdown))                     # Comun stuff in both sets
#for x in clothesall:
#    print(x)
"""


##
###  *************** 16 ************************       Dictionary´s             Changable, unordered collection of unique key: value pairs
#                                                                               Fast because they use hashing, allow us to accsess a value Quickly

"""

capitals = {"Italy":"Rome",
            "India":"New Dehli",
            "Spain":"Madrid",
            "Russia":"Moscow"}

#print(capitals["Russia"])                            # Print the value of the key "Russia
#print(capitals["Germany"])                           #Dont use this because gives an error
#print(capitals.get("Germany"))                       # Returns None if Capitals does not countain Germany
#print(capitals.keys())                               # Print of the keys
#print(capitals.values())                             # Print of the values
#print(capitals.items())                              # Prints everything on the Dictionary

capitals.update({"Germany":"Berlin"})                 #Adds Germany to the Dictionary with is respective value
capitals.update({"Italy":"Milano"})                   #Changes Italy capital+
capitals.pop("Germany")
capitals.clear()

for key,value in capitals.items():                    # Prints everything
    print(key,value) 

"""


##
### ********************************* 17    Indexing
##

"""

name = "leandro Cardoso!"

if(name[0].islower()):                     # Capitalize the letter with index 0
    name = name.capitalize()

first_name = name[:6].upper()
last_name = name [8:].lower()
print(first_name)
print(last_name)

last_character = name [-1]          # last thing in string
"""


##
### ********************************* 18   Fucntion = a block of code which is executed ONLY when called
##

"""
def hi():
    print("hello!")
    print("teste")

hi()                    #calling a function           Needed to have the same amount of arguments called

def hello(name):
    print("hello "+name)
    print("works")

name = input("Write your name here: ")
hello(name)

def complete(first, second,age):
    print("Hello: "+first+" "+second+" You are "+str(age)+" years old")

complete("21","22",23)
  """  

##
### ********************************* 19    Return Statement   Function send Python values/objects back to the calller
##                                                             These values/objects are known as the function´s return value.
"""
def multiply(number1,number2):
    return number1 * number2

x = multiply(6,8)
print(x)
"""

##
### ********************************* 20   Keyword Arguments
##

"""
def Hi(first,middle,last):
    print("Hello " +first +" "+middle +" " +last)

Hi(last="Car", middle="mar", first="leandro")
"""



##
### ********************************* 21       Nested Function calls   ===== functions calls inside other functions and soo on
###                                                                          1 usable function is the one inside all the ( )
##
"""
print(round(abs(float(input("Enter a positive number: ")))))

## Replaces the use of 4 or 5 lines of code to do every step of the convertion, num=input....+ num = float(num) ..+ num = abs(num) ... + num = round(num) + print(num)
"""

##
### ********************************* 22       Variable scope       its a variable that only exists inside the region that was created
##

"""
def display_name():
    name = "leandro"              #scope variable
    print(name)

#print(name)  does not work because name is not a global variable
"""

##
### ********************************* 23        *Args   (can be any name, just needs *)               Packs all Arguments into a tuple  , useful so that a function can accept a varying amount of arguments
##

"""
def add(*stuff):
    sum = 0
    stuff = list(stuff)        # needed to convert to a list to change an outside value once the function is called, Tuples content cannot be changed
    stuff[0] = 0 
    for i in stuff:
        sum+= i
    return sum

print(add(1,2,3,4,5,6))
"""

##
### ********************************* 24      **kwargs  ===== packs all arguments into a dictionary
###                                                           useful so that a  funtion can accept a varying amount of keyword arguments(kwargs)
##

"""
def hello(**names):
    #print("Hello " + names["first"] + " " + kwargs["last])
    print("Hello",end=" ")                                                       # Will write in the same line
    for key,value in names.items():                                              # for each key / value in "hello", writes it
        print(value,end=" ")

hello(title = "Mr." ,first = "Leandro" ,middle = "Something" ,last = "Cardoso")
"""




##
### ********************************* 25     str.format()    = optional method that gives users                    Purelly optional format fields
##                                                           more control when displaying output

"""
animal = "dog"
item = "fence"

#print("The " +animal +" jumped over the " +item)
print("The {} jumped over the {}".format(animal,item))
print("The {1} jumped over the {0}".format(animal,item))
#print("The {} jumped over the {}".format(animal="dog",item="fence"))
#print("The {animal} jumped over the {item}".format(animal="dog",item="fence"))
#print("The {animal} jumped over the {animal}".format(animal="dog",item="fence"))

text = "The {} jumped over the {}"            # Cleaner way of doing a str format
print(text.format(animal,item))

"""



##
### ********************************* 25.1       Format fields  str.format
##

"""
name = "leandro"

print("Hello, my name is {:10}. Nice to mmet you".format(name))                #This will make 10 spaces bettween name and Nice to..
print("Hello, my name is {:<10}. Nice to mmet you".format(name))                # same as above (defalut)
print("Hello, my name is {:>10}. Nice to mmet you".format(name))                # 10 spaces before bro
print("Hello, my name is {:^10}. Nice to mmet you".format(name))                #This will make 1name in middle of 10 spaces
"""



##
### ********************************* 25.2        Format fields  str.format
##

"""
number = 3.14159
number2 = 1000
print("The number Pi is {:.2f}".format(number))     # This will print pi with only 2 floating numbers  (3.14) and also rounds if needed

print("The number is {:,}".format(number2))     # This will print 1000 has 1,000

print("The number is {:b}".format(number2))     # This will print a represantation of the number in binary

print("The number is {:x}".format(number2))     # This will print as hexadecimal

print("The number is {:E}".format(number2))     # This will print as cientific notation  Exemp 1.00000E +03
print("The number is {:e}".format(number2))     
"""

##
### ********************************* 26    Generate random numbers    ####2.34h
##

"""
import random  #module random
x = random.randint(1,6) # between 1 and 6
y = random.random()     # between 0 and 1

myList = ["rock" , "paper" , "scissors"]
z = random.choice(myList)                     # random

cards = [1,2,3,4,5,6,7,8,9,"J","Q","K","A"]   #random order
random.shuffle(cards)

print(x)
print(z)
print(cards)
"""

##
### ********************************* 27      Exception      -.---- event detected during the execution of the code that interrupts the flow of the program
##

"""
try:
    numerator = int(input.("Enter a number to divide: "))
    denominator = int(input.("Enter a number to divide by: "))
    result = numerator / denominator
    print(result)
except ZeroDivisionError:
    print("You can´t divide by zero!")    # Writing number "0"
except ValueError:                    
    print("Enter only numbers")           # Writing something that ain´t numbers
except Exception:
    print("Something went wrong")         # Global exception
else:
    print(result)                         # if there is no exception

finally:                                  # Always executes, with or without exception
    print("End")

#except Exception as e:  /  except ValueError as e:  /   except ZeroDivisionError as e:     WAY of showing with a print(e) what was the problem
"""

##
### ********************************* 28     File detection  - basic
##

"""
import os     #already in python library

path = "C:\\Users\\leand\\Downloads\\testepython.txt"   # Double \  

if os.path.exists(path):                             # if location exists
    print("File exists!")
    if os.path.isfile(path):                         # if is file
        print("Thats a file")
    elif os.path.isdir(path):                     # If Direcory (paste) exists
        print("That is a directory") 
else:
    print("Does not exist!")
"""


##
### ********************************* 29       Read File Contents
##

"""
# with open("testepython") as file: if is already in project

try:

    with open("C:\\Users\\leand\\Downloads\\testepython.txt") as file:                # Should always use the try function to prevent errors
        print(file.read())
        
#print(file.closed)                          # automatically closes the file with the "with open" function , the print can confirm the state of the file
except FileNotFoundError:
    print("That file was not found. ")
"""


##
### ********************************* 30     Writing  text files             2h:53min
##

"""
text = "Have a good one \n New line command \n New line command "
text1 = "Just writing a new line"

with open("test.txt","w") as file:        # W stands for write (default is "r" - read)
    file.write(text)
    print("Done")

with open("test.txt","a") as file:
    file.write(text1)
"""

##
### ********************************* 31    Copying some files content
##

"""
#copyfile() = copies content of file
#copy() = copyfile() + permission mode + destination can be a directory
#copy2() = copy() + copies metadata (file´s creation and modification times)

import shutil

shutil.copyfile('test.txt','copy.txt')     # Creates a new copied file inside visual studio project
shutil.copyfile('test.txt','C:\\Users\\leand\\Downloads\\copy.txt')    # creates a new copied file in windows path
"""


##
### ********************************* 32     Moving Files or folders in pc
##


"""
import os

source = "test.txt"
destination = "C:\\Users\\leand\\Downloads\\test.txt"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(source, destination)
        print(source+ " was moved.")
except FileNotFoundError:
    print(source+" was not found. ")
"""


## 
### ********************************* 33     Deleting files with Python
##


"""
import os
import shutil                   # needed to remove a directory that contains files

#path = "test.txt"
path = "empty_folder"

try:
    os.remove(path)             # This function does not remove empty Folders
    os.rmdir(path)              # How to remove folders
    #shutil.rmtree(path):       # dangerous function, because it removes the directory and all files within

except FileNotFoundError:
    print("That file was not found")

except PermissionError:         # Might happen trying to remove a directory with the os.remove function
    print("You do not have permission do delete that.")

except OSError:                 # cwhen trying to delete a folder that has content,,,, the OSError shows up
    print("You cannot delete that using that function")

else:                           # If there is no exceptions
    print(path+ " was deleted.")
"""


##
### ********************************* 34    Modules   = a file containing python code. May contain functions, classes, etc.
##                                                      used with modular programming, which is to separate a program into parts.

#  Nota: So funcionar depois de encontrar Python na Cmd, pip3 instalado, e modificar o tipo de file do module do projeto para messages.py

#help("modules")   to help , also on web


"""
#import messages
#import messages as msg
from messages import hello,helloo
#from messages import *                   '''''' Imports all

#messages.helloo()
#msg.helloo()
helloo()
"""
   
## 
### ********************************* 35     Rock Paper scissors game
##

"""
import random


while True: 
    choices = ["rock", "paper" , "scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("Rock, paper or scissors? : ").lower()

    if player == computer:
        print("Computer: ",computer)
        print("Player: ",player)

    elif player == "rock":
        if computer == "paper":
            print("Computer: ",computer)
            print("Player: ",player)
            print("U lose! ")

        if computer == "scissors":
            print("Computer: ",computer)
            print("Player: ",player)
            print("U Win! ")

    elif player == "scissors":
        if computer == "rock":
            print("Computer: ",computer)
            print("Player: ",player)
            print("U lose! ")

        if computer == "paper":
            print("Computer: ",computer)
            print("Player: ",player)
            print("U Win! ")

    elif player == "paper":
        if computer == "scissors":
            print("Computer: ",computer)
            print("Player: ",player)
            print("U lose! ")

        if computer == "rock":
            print("Computer: ",computer)
            print("Player: ",player)
            print("U Win! ")

    play_again = input("Play again? ( yes/no): ").lower()


    if play_again != "yes":
        break
print("Bye!!!")
"""


##
### ********************************* 36      Basic Quiz game
##












##
### ********************************* 37   
##

##
### ********************************* 38   
##

##
### ********************************* 39   
##

