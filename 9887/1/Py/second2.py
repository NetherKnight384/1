

"""
def pas(passw):
    if len(str(passw)) > 5:
        print("\033[1;31;40m")
        raise ValueError("len passw err")


try:
    pas(1919)
    with open("logs.txt", "w") as file:
        print(file.write("lox"))
        file.close()
except ValueError as a:
    print(a)
except FileNotFoundError as a:
    print("am")
"""
while True:

    try:
        a = int(input("a:"))
        b = int(input("b:"))
        print(a + b)
    except ValueError:
        print("\033[1;31;40minput != int\033[0;37;40m")
    