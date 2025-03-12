userReply = input("Você precisa enviar um pacote? (Digite sim ou não) ")
if userReply == "sim":
    print("Podemos ajudá-lo a enviar esse pacote!")
else:
    print("Volte quando precisar enviar um pacote. Obrigado..")


userReply = input("Gostaria de comprar selos, comprar um envelope ou fazer uma cópia? (Insira selos, envelope ou cópia)) ")
if userReply == "selos":
    print("Temos muitos designs de carimbos para você escolher.")
elif userReply == "envelope":
    print("Temos vários tamanhos de envelopes para você escolher.")
elif userReply == "cópia":
    copies = input("Quantos exemplares você gostaria? (Digite um número) ")
    print("Aqui estão {} cópias.".format(copies))
else:
    print("Obrigado, por favor, volte novamente.")