

a = {1:"tt", 2:"aa", 3:"rr"}
c = list(a.keys())
b = []
for i in range(len(c)):
    b.append(a[c[i]])
d = {}
for i in range(len(c)):
    d.update(b[i])

print(d)