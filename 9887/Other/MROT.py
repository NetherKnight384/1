import math
m = int(2) 
a = int(1012)
q = len(str(a))
c = []
r = []
q_ = 0
print("q_, q, c, r")
print(q_, q, c, r)
r.append(a-(m*(a//m)))
c.append(a//m)

while c[q_]//m > 0:
    print(q_, q, c, r)
    r.append(c[q_]-(m*(c[q_]//m)))
    c.append(c[q_]//m)
    q -= 1
    q_ += 1

print(r[::-1])




