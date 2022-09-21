#a) Se idade é maior que 60, escreva: 'Você tem direito aos benefícios!'
if(idade > 60):
    print('Você tem direito aos benefícios')

#Se dano é maior do que 10 e escuto é igual a  0, escreva: "Você está morto!"
if(dano > 10 and escudo == 0):
    print('Você está morto!')

#Se pelo menos uma das variáveis booleanas, norte, sul, leste, oeste, escreva: "Você escapou!"
if(norte == True or sul == True or leste == True or oeste == True):
    print('Você escapou!')
#Outra forma de escrever seria:
if(norte or sul or leste or oeste):
    print('Você escapou!')

