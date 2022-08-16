while True:
    try:
        for i in range(0,2):
            D=str(input())
            S=str(input())
            if(D.find(S)!=-1):
                print("Resistente")
            else:
                print("Nao resistente")
    except EOFError:
        break
