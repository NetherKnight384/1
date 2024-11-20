import math



def get_md(acc):
    q = len(acc)
    while q > 0:
        if acc[abs(q-len(acc))] == "*":
            acc.insert((int(abs(q-len(acc)))-1),(int(acc[abs(q-len(acc))-1]) * int(acc[abs(q-len(acc))+1])))
            del acc[int(abs(q-len(acc)))]
            del acc[int(abs(q-len(acc))+1)]
            del acc[int(abs(q-len(acc))+1)]
        elif acc[abs(q-len(acc))] == "/":
            acc.insert((int(abs(q-len(acc)))-1),(int(acc[abs(q-len(acc))-1]) / int(acc[abs(q-len(acc))+1])))
            del acc[int(abs(q-len(acc)))]
            del acc[int(abs(q-len(acc))+1)]
            del acc[int(abs(q-len(acc))+1)]
        q -= 1
def get_as(acc):
    q = len(acc)
    while q > 0:
        if acc[abs(q-len(acc))] == "+":
            acc.insert((int(abs(q-len(acc)))-1),(int(acc[abs(q-len(acc))-1]) + int(acc[abs(q-len(acc))+1])))
            del acc[int(abs(q-len(acc)))]
            del acc[int(abs(q-len(acc))+1)]
            del acc[int(abs(q-len(acc))+1)]
        elif acc[abs(q-len(acc))] == "-":
            acc.insert((int(abs(q-len(acc)))-1),(int(acc[abs(q-len(acc))-1]) - int(acc[abs(q-len(acc))+1])))
            del acc[int(abs(q-len(acc)))]
            del acc[int(abs(q-len(acc))+1)]
            del acc[int(abs(q-len(acc))+1)]
        q -= 1




def get_mdL(lcc):
    q = len(lcc)
    while q > 0:
        if lcc[abs(q-len(lcc))] == "*":
            lcc.insert((int(abs(q-len(lcc)))-1),(int(lcc[abs(q-len(lcc))-1]) * int(lcc[abs(q-len(lcc))+1])))
            del lcc[int(abs(q-len(lcc)))]
            del lcc[int(abs(q-len(lcc))+1)]
            del lcc[int(abs(q-len(lcc))+1)]
        elif lcc[abs(q-len(lcc))] == "/":
            lcc.insert((int(abs(q-len(lcc)))-1),(int(lcc[abs(q-len(lcc))-1]) / int(lcc[abs(q-len(lcc))+1])))
            del lcc[int(abs(q-len(lcc)))]
            del lcc[int(abs(q-len(lcc))+1)]
            del lcc[int(abs(q-len(lcc))+1)]
        q -= 1
def get_asL(lcc):
    q = len(lcc)
    while q > 0:
        if lcc[abs(q-len(lcc))] == "+":
            lcc.insert((int(abs(q-len(lcc)))-1),(int(lcc[abs(q-len(lcc))-1]) + int(lcc[abs(q-len(lcc))+1])))
            del lcc[int(abs(q-len(lcc)))]
            del lcc[int(abs(q-len(lcc))+1)]
            del lcc[int(abs(q-len(lcc))+1)]
        elif lcc[abs(q-len(lcc))] == "-":
            lcc.insert((int(abs(q-len(lcc)))-1),(int(lcc[abs(q-len(lcc))-1]) - int(lcc[abs(q-len(lcc))+1])))
            del lcc[int(abs(q-len(lcc)))]
            del lcc[int(abs(q-len(lcc))+1)]
            del lcc[int(abs(q-len(lcc))+1)]
        q -= 1





def get_sl(acc):
    q = len(acc)
    sl_1 = {}
    lcc = []
    while q > 0:
        
        if acc[abs(q-len(acc))] == "(":
            sl_1[acc[abs(q-len(acc))]] = abs(q-len(acc))
        elif acc[abs(q-len(acc))] == ")":
            sl_1[acc[abs(q-len(acc))]] = abs(q-len(acc))
            lcc = acc[(sl_1["("] + 1):(sl_1[")"])]
            #print("000",lcc)
            get_mdL(lcc)
            get_asL(lcc)
            #print("+000",lcc)
            #print(lcc[0],sl_1["("])
            del acc[(sl_1["("]+1):(sl_1[")"]+1)]
            acc.insert(sl_1["("],lcc[0])
            del acc[(sl_1["("]+1)]
            lcc.clear()
            #print("111",acc)
            return
        q -= 1
    #print(acc)
    

        




#b = "7 + 9 / 2 - ( 9 * ( 7 * 9 - 8 ) + 1 ) + 82 / ( 8 * 8 )"
#input().split()
# "7 + 9 / 2 ( 9 * 9 - 8 ) + 1"
d = 0
acc = input().split()
if acc[0] == "d":
    acc.pop(0)
    d = 1
#print(acc)
#['4', '+', '9', '(', '9', '-', '20', '*', '8', ')', '/', '3']
#print("111",acc)
q = len(acc)
while q > 0:
    get_sl(acc)
    q-=1
get_md(acc)
#print(acc)
get_as(acc)
if d == 1:
    print(acc)
else:
    print(acc[0])


#get_md(acc)
#get_as(acc)
#print(acc)
#print(384 + 3283 - 94 * 4 / 95 + 30 - 94 * 34)