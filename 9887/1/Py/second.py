a = int(input())
b = int(input())
c = 0
even =[]
if b > a:
    c = b
    b = a
    a = c
q = a - b
q_ = 0
while q >= 0:
    if ((a - q_) % 2) == 0:
        even.append(a - q_)
    q -= 1
    q_ += 1
q = len(even)
even.sort
print("even:",sorted(even),"average:",sum(even)//len(even))
even.clear()
q = a - b
q_ = 0
while q >= 0:
    if ((a - q_) % 2) != 0:
        even.append(a - q_)
    q -= 1
    q_ += 1
even.sort
print("odd:",sorted(even),"average:",sum(even)//len(even))
even.clear()
q = a - b
q_ = 0
while q >= 0:
    if (a - q_)%9==0:
        even.append(a-q_)
    q -= 1
    q_ += 1
print("%9:",even)





