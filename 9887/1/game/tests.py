
"""
def rand(seed, max):
    seed = seed * 1103515245 + 12345
    return((seed//65536) % (max + 1))
"""

"""
def randd(seed):
    out = ((seed**6536 << 2)+(seed**6536 >> 2)//65536) % (6536 + 1)
    q = 0
    while q<100:
        out = ((out**6536 << 2)+(out**6536 >> 2)//65536) % (6536 + 1)
        q +=1
    return(out)
"""
"""def randd(seed,max):
    out = ((seed**6536 << 2)+(seed**6536 >> 2)//65536) % (max + 1)
    q = 0
    while q<1:
        out = ((out**6536 << 2)+(out**6536 >> 2)//65536) % (max + 1)
        q +=1
    return(out)
"""

class LCG:
    def __init__(self, seed, max_value, a=1664525, c=1013904223):
        self.seed = seed
        self.max_value = max_value
        self.a = a
        self.c = c
        self.current = seed

    def random(self):
        self.current = (self.a * self.current + self.c) % self.max_value
        return self.current

    def set_max_value(self, new_max_value):
        self.max_value = new_max_value

# Пример использования
seed = 42
max_value = 2**32 # Начальный модуль
lcg = LCG(seed, max_value)

print("Старый max_value:", max_value)
for _ in range(5):
    print(lcg.random())

# Изменение max_value
new_max_value = 1000
lcg.set_max_value(new_max_value)
print("\nНовый max_value:", new_max_value)
for _ in range(5):
    print(lcg.random())
