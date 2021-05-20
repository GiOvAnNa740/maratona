n=input().split(" ")

x= int (n[0])
y= int (n[1])

# x+ y+
if 0 < x < 50 and 0 < y < 50:
    print('R1', end="")

# x- y+
if -50 < x < 0 and 0 < y < 50:
    print('R2', end="")

# x- y-
if -50 < x < 0 and -50 < y < 0:
    print('R3', end="")

# x+ y-
if 0 < x < 50 and -50 < y < 0:
    print('R4', end="")

# x0 y0
if x==0 and y==0:
    print('NO ALVO!', end="")
