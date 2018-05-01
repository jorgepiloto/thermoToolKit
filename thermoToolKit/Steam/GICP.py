Rg = 0
Gamma = 0
Cv = 0
Cp = 0

def inputPropertiesAir():
    
    print("""
             1) Rg
             2) Cv
             3) Cp
             4) Gamma
                    
             Choose two variables: 
        """)
       
    op1 = int(input("VAR 1: "))
    op2 = int(input("VAR 2: "))
    
    #(SELECCIONADA Rg y Cv)
    if (op1 == 1 or op1 == 2) and (op2 == 1 or op2 == 2) and (op1 != op2):
        
        Rg = float(input("Input Rg: "))
        Cv = float(input("Input Cv: "))
        
        Cp = Rg + Cv
        Gamma = Cp/Cv
        
        printPropertiesAir(Cp, Cv, Rg, Gamma)
        
    elif (op1 == 1 or op1 == 3) and (op2 == 1 or op2 == 3) and (op1 != op2):
        
        Rg = float(input("Input Rg: "))
        Cp = float(input("Input Cp: "))
        
        Cv = Cp - Rg
        Gamma = Cp/Cv
        
        printPropertiesAir(Cp, Cv, Rg, Gamma)
        
    elif (op1 == 1 or op1 == 4) and (op2 == 1 or op2 == 4) and (op1 != op2):
        
        Rg = float(input("Input Rg: "))
        Gamma = float(input("Input Gamma: "))
        
        Cv = Rg/(Gamma - 1)
        Cp = Cv + Rg
        
        printPropertiesAir(Cp, Cv, Rg, Gamma)
        
    elif (op1 == 2 or op1 == 3) and (op2 == 2 or op2 == 3) and (op1 != op2):
        
        Cp = float(input("Input Cp: "))
        Cv = float(input("Input Cv: "))
        
        Rg = Cp - Cv
        Gamma = Cp/Cv
        
        printPropertiesAir(Cp, Cv, Rg, Gamma)
        
    elif (op1 == 2 or op1 == 4) and (op2 == 2 or op2 == 4) and (op1 != op2):
        
        Cv = float(input("Input Cv: "))
        Gamma = float(input("Input Gamma: "))
        
        Cp = Gamma * Cv
        Rg = Cp - Cv
        
        printPropertiesAir(Cp, Cv, Rg, Gamma)
        
    elif (op1 == 3 or op1 == 4) and (op2 == 3 or op2 == 4) and (op1 != op2):
        
        Cp = float(input("Input Cp: "))
        Gamma = float(input("Input Gamma: "))
        
        Cv = Cp/Gamma
        Rg = Cp - Cv
        
        printPropertiesAir(Cp, Cv, Rg, Gamma)
        
    else:
        print("ERROR: number selected is not in list or propertie selected is the same")
        
        
def printPropertiesAir(Cp, Cv, Rg, Gamma):
    
        print("\n\nCp: ", Cp)
        print("Cv: ", Cv)
        print("Rg: ", Rg)
        print("Gamma: ", Gamma)
    