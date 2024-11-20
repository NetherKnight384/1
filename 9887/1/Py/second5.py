char = "*"

print("\n","A", )
q = 10
while q > 0:
    q_ = 10
    print()
    while q_ > 0:
        if q >= q_ :
            print(char, end="")
        else:
            print(" ", end="")
        q_ -= 1
    q -= 1

print("\n","\n","B", )
q = 10
while q > 0:
    q_ = 10
    print()
    while q_ > 0:
        if q <= q_ :
            print(char, end="")
        else:
            print(" ", end="")
        q_ -= 1
    q -= 1


print("\n","\n","C", )
q = 10
q__ = 0
print(" q_ ", end="")
while q > 0:
    print( q-1, " ", end="")
    q -= 1
print("\nq", end="")
q = 10
while q > 0:
    q_ = 10
    q_i = 0
    print()
    print(q-1, "  ", end="")
    while q_ > 0:
        if q > 0 and ((q_ > 5 and q_+q__ < 11) or (q_ <= 5 and q_i+q__ < 10)):
            print(char, end="  ")
        else:
            print(" ", end="  ")
        q_ -= 1
        q_i += 1
    print(" ",q__, end="  ")
    q__ += 1
    q -= 1
    


print("\n","\n","D", )
q = 10
q__ = 0
q__i = 10
print(" q_ ", end="")
while q > 0:
    print( q-1, " ", end="")
    q -= 1
print("\nq", end="")
q = 10
while q > 0:
    q_ = 10
    q_i = 0
    print()
    print(q-1, "  ", end="")
    while q_ > 0:
        if (q > 5 and ((q_ > 5 and q_+q__ < 11) or (q_ <= 5 and q_i+q__ < 10))) or (q <= 5 and ((q_ > 5 and q_+q__i < 12) or (q_ <= 5 and q_i+q__i < 11))):
            print(char, end="  ")
        else:
            print(" ", end="  ")
        q_ -= 1
        q_i += 1
    print(" ",q__, end="  ")
    q__ += 1
    q__i -= 1
    q -= 1





print("\n","\n","K", )
q = 10
q__ = 0
q__i = 10
print(" q_ ", end="")
while q > 0:
    print( q-1, " ", end="")
    q -= 1
print("\nq", end="")
q = 10
while q > 0:
    q_ = 10
    q_i = 0
    print()
    print(q-1, "  ", end="")
    while q_ > 0:
        if (q_ > 5 and ((q > 5 and q+q__ < 11) or (q <= 5 and q__+q__ < 10))) or (q_ <= 5 and ((q > 5 and q+q_i < 12) or (q <= 5 and q__i+q_i < 11))):
            print(char, end="  ")
        else:
            print(" ", end="  ")
        q_ -= 1
        q_i += 1
    print(" ",q__, end="  ")
    q__ += 1
    q__i -= 1
    q -= 1
   