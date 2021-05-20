n=input().split(" ") #quebrando a string nos espaços, nesse momento ela vira um vetor

a= int (n[0])
b= int (n[1])
c= int (n[2])

m1 = (a +b + abs(a - b)) // 2 # calculo do ponto medio

m2 = (c + m1 +abs(m1 - c))//2

print (m2, end="")



