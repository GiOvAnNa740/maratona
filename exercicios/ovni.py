qtd = int(input())
resp=int
result =[]


def calculo(n):
    r1= int (n[0])*2
    r2= int (n[1])*2
    r3= int (n[2])*2

    if r3 >= r1+r2:
        return "CABE!"

    if r3 < r1+r2:
        return "NAO CABE!"


for n in range(qtd):
    p = input().split(" ")
    result.append(calculo(p))



for x in result:
    if qtd>1:
        print(x)
        qtd=qtd-1
    else:
        print(x, end="")
