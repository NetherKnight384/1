

a = int(input())
b = int(input())

if b > a:
    c = b
    b = a
    a = c
q = a-b
while q >= 0:
    c = 2
    g = a-q
    while c != 12:
        
        print(g, end=" ")
        g = (a-q )*c
        c += 1
    q -= 1
    print()


