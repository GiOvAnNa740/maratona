
#def somatorio(n):
    #soma=sum(int(x) for x in n)
    #return soma
        
#l= int(input()) #quantidade de testes

#for c in range(l):
   # a = input().split(";")
   # print(somatorio(a), end="")

qtd = int(input())
result =[]

def somatorio(n):
    soma=sum(int(x) for x in n)
    return soma

for n in range(qtd):
    num = input().split(";")
    result.append(somatorio(num))

for x in result:
    if qtd>1:
        print(x)
        qtd=qtd-1
    else:
        print(x, end="")
