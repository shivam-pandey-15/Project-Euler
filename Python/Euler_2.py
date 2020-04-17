

a = 1 
b = 2

s = 0

while a<4*10**6:
    if a%2==0:
        s+=a
    a,b = b,a+b

print(s)

