def console(s):
    while s > 0:
        print("console:", end=" ")
        consol = input()
        
        if consol == "hi":
            print("console: name:", end=" ")
            consol = input()
            print("console: Hi", consol + "!")
        elif consol == "stop":
            s = 0
        elif consol == "help":
            print("console: help hi stop")
        else:
            print("console: err")


