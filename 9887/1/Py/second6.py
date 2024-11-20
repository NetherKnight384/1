





ls = [input(),input(),input(),input()]
ls = [int(i) for i in ls]

for i in ls:
    if i < 0:
        print(ls.index(i))
        exit()
