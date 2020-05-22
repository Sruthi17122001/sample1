t=int(input("Enter nth position to terminate the series="))
a,b,c,i=0,1,1,0
while i<t:
    print(a, end=" ")
    a=b
    b=c
    c=a+b
    i+=1
