x=int(input())
s1=input()
y=int(input())
s2=input()
z=int(input())
n1=int
n2=int


if s1==s2:
    if s1=="/":
        n1=x/y
        n2=n1/z
    if s1=="*":
        n1=x*y
        n2=n1*z
    if s1=="+":
        n1=x+y
        n2=n1+z
    if s1=="-":
        n1=x-y
        n2=n1-z
    
if s1!= s2:
    if s1=="/":
        n1=x/y   
        if s2=="*":
            n2=n1*z
        if s2=="+":
            n2=n1+z
        if s2=="-":
            n2=n1-z
    if s1=="*":
        n1=x*y
        if s2=="/":
            n2=n1/z
        if s2=="+":
            n2=n1+z
        if s2=="-":
            n2=n1-z
    if s2=="/":
        n1=y/z
        if s1=="+":
            n2=x+n1
        if s1=="-":
            n2=x-n1
    if s2=="*":
        n1=y*z
        if s1=="+":
            n2=x+n1
        if s1=="-":
            n2=x-n1




print(int(n2), end="")
