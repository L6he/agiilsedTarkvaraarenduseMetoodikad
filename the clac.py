def uselessFuckingInformation():
    print("\n\n total times doohickeyed with the thingamabob: ", sum(Array7),
          "\n times added with da thignermerberb: ", Array7[0],
          "\n times subtracted with da thignermerberb: ", Array7[1],
          "\n times multiplied with da thignermerberb: ", Array7[2],
          "\n times divided with da thignermerberb: ", Array7[3],)
    
def Addition(a,b): 
    if isinstance(a,int) and isinstance(b,int):
        return a + b
    else:
        print("mi bomboclaat")
        
def Subtraction(a,b): 
    if isinstance(a,int) and isinstance(b,int):
        return a - b
    else:
        print("mi bomboclaat")
        
def Multiplication(a,b): 
    if isinstance(a,int) and isinstance(b,int):
        return a * b
    else:
        print("mi bomboclaat")
        
def Division(a,b):
    if isinstance(a,int) and isinstance(b,int):
        try:
            return a / b
        except:
            print:("mi bomboclaat")
    else:
        print("mi bomboclaat")

Array7 = [0,0,0,0]

def Main():
    a = int(input("\nawglrh blargh arr first number: "))
    b = int(input("awglrh blargh arr second number: "))
    chchchchchanges = input("Select an operator(1: Addition, 2: Subtraction, 3: Multiplication, 4: Division): ")
    if chchchchchanges == "1":
        Array7[0] += 1
        print(Addition(a,b))
        uselessFuckingInformation()
        Main()
    elif chchchchchanges == "2":
        Array7[1] += 1
        print(Subtraction(a,b))
        uselessFuckingInformation()
        Main()
    elif chchchchchanges == "3":
        Array7[2] += 1
        print(Multiplication(a,b))
        uselessFuckingInformation()
        Main()
    elif chchchchchanges == "4":
        Array7[3] += 1
        print(Division(a,b))
        uselessFuckingInformation()
        Main()
    else:
        print("fuck you")
        Main()

Main()