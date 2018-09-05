#############################################################################
# Global Variables
#############################################################################

strQuadratic = ""


#############################################################################
# Functions
#############################################################################

#Verifyes that the user imputted Quadratic Function, is in correct format. 
def quadraticStrVerifyer(strToVerify):
    import re
    verifyResult = re.search(r"[0-9,]{1,5}x\^2[+|-][0-9,]{1,5}x([+|-][0-9,]{1,5})?",strToVerify)
    return verifyResult

#Splits the Quadratic functions into 3 variables, and returs them as float(decimal).
def quadraticSplitter(strToSplit):
    import re
    #Finds A, B and C, and saves them in Variables
    quadraticVarA = re.search(r"[0-9,]{1,5}(?=x\^2)",strToSplit)
    quadraticVarB = re.search(r"[0-9,]{1,5}(?=x[^^])",(strToSplit+" "))
    quadraticVarC = re.search(r"[0-9,]{1,5}$",strToSplit)

    #Filters out the exact number, and saves it as a decimal (float)
    fltQuadraticVarA = float(quadraticVarA.group(0))
    fltQuadraticVarB = float(quadraticVarB.group(0))
    fltQuadraticVarC = 0

    #If "C" has been defined, specifies it to use the defined number. 
    if(quadraticVarC):
        fltQuadraticVarC = float(quadraticVarC.group(0))

    return fltQuadraticVarA, fltQuadraticVarB, fltQuadraticVarC


#Finds discriminant and prints how many solutions there are based on the discriminant
def findDiscriminant(fltQuadraticVarA,fltQuadraticVarB,fltQuadraticVarC):
    disciminant = fltQuadraticVarB**2-4*fltQuadraticVarA*fltQuadraticVarC

    if(disciminant < 0):
        print("Equation has no solution!")
    elif (disciminant > 0):
        print("Equation has two solutions!")
    else:
        print("Equation has one solution!")

    return float(disciminant)

#Vertex
def findVertex(discriminant,fltQuadraticVarA,fltQuadraticVarB):
    fltVertexX = (-(fltQuadraticVarB))/(2*fltQuadraticVarA)
    fltVertexY = (-(discriminant))/(4*fltQuadraticVarA)

    return float(fltVertexX),float(fltVertexY)



#############################################################################
# Defunctionised code
#############################################################################

print("Insert Quadratic Fuction")
print("Example: ax^2+bx+c")

#Collects the fuction from user. 
strQuadratic = input("f(x)=")

#Verifying user inputted Quadratic Function
if not quadraticStrVerifyer(strQuadratic):
    print("Invalid Quadratic Function")
    quit()

#Splitting Quadratic Function into an array "arQuadraticVars"
arQuadraticVars = quadraticSplitter(strQuadratic)

#Finds the discriminant
fltQuadraticVarDisc = findDiscriminant(arQuadraticVars[0],arQuadraticVars[1],arQuadraticVars[2])

