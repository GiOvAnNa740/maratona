qtd = int(input())
result =""
mai=0
men=0

def mmi(a):
    for b in range(a):
        if b == 0:
            mai=men =a[b]
    else:
        if a[b]>mai:
            mai=a[b]
        if a[b]<men:
            men=a[b]
    return mai,men

for n in range(qtd):
    num = input().split(" ")
    n1=str((mmi(num)))

for x in result:
    if qtd>1:
        print(x)
        qtd=qtd-1
    else:
        print(x, end="")