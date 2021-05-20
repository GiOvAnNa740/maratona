# aspas duplas ou simples são indiferentes
# não precisa de ';' no fim

#conversão se strings
A=int(input())
b=float(input())

#prints

print("O valor é: "+ str(A))
print('A = %i' % A)
print("a", end="") #'end' impede que o print quebre linha
print("a","b")

print('We are the {} who say "{}!"'.format('knights', 'Ni'))
#We are the knights who say "Ni!"

##
exemplo= "abcd"

# '[]' pega a posição da string
# a contagem se inicia na posição 0
print(exemplo[1])
print(exemplo[2])
print(exemplo[3])
print(exemplo[4])
print(exemplo[0:2]) # string que vai da posição de 0 a 2 sem incluir a 2
print(exemplo[0:]) # se não especificar na direita ele vai até o limite

print(exemplo[-1]) # é possível pegar índices negativos, contando da direita para a esquerda a contagem se inicia no -1


