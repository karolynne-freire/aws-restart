import random

print("Bem-vindo ao Adivinhe o número!")
print("As regras são simples. Vou pensar em um número e você tentará adivinhar.")

number = random.randint(1,10)
isGuessRight = False

while isGuessRight != True:
    guess = input("Adivinhe um número entre 1 e 10: ")
    if int(guess) == number:
        print("Você adivinhou{}. está correto! Você ganha!".format(guess))
        isGuessRight = True
    else:
        print("Você adivinhou {}. desculpe, não é isso. Tente novamente.".format(guess))