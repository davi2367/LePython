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
    quadraticVarA = re.search(r"[-]?[0-9,]{1,5}(?=x\^2)",strToSplit)
    quadraticVarB = re.search(r"[-]?[0-9,]{1,5}(?=x[^^])",(strToSplit+" "))
    quadraticVarC = re.search(r"[-]?[0-9,]{1,5}$",strToSplit)

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

#Calculates the vertex points
def findVertex(discriminant,fltQuadraticVarA,fltQuadraticVarB):
    fltVertexX = (-(fltQuadraticVarB))/(2*fltQuadraticVarA)
    fltVertexY = (-(discriminant))/(4*fltQuadraticVarA)

    return float(fltVertexX),float(fltVertexY)

#Roots
def findQuadraticSolutions(discriminant, fltQuadraticVarA, fltQuadraticVarB):
    import math

    fltSqrtDisc = math.sqrt(discriminant)

    fltQuadraticRootX1 = (-(fltQuadraticVarB)+fltSqrtDisc)/(2*fltQuadraticVarA)
    fltQuadraticRootX2 = (-(fltQuadraticVarB)-fltSqrtDisc)/(2*fltQuadraticVarA)

    return float(fltQuadraticRootX1),float(fltQuadraticRootX2)


def findQuadraticRoots(arSolutions,fltQuadraticVarA,fltQuadraticVarB,fltQuadraticVarC):
    arRoot1 = [arSolutions[0],(fltQuadraticVarA*(arSolutions[0]**2)+(fltQuadraticVarB*arSolutions[0])+(fltQuadraticVarC))]
    arRoot2 = [arSolutions[1],(fltQuadraticVarA*(arSolutions[1]**2)+(fltQuadraticVarB*arSolutions[1])+(fltQuadraticVarC))]

    return arRoot1,arRoot2


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
print("The discriminant is: "+str(fltQuadraticVarDisc))

#Calculates and displays the vertex points to the user with 2 decimals. 
arVertexPoint = findVertex(fltQuadraticVarDisc,arQuadraticVars[0],arQuadraticVars[1])
print("The vertex point is: ("+str(round(arVertexPoint[0],2))+","+str(round(arVertexPoint[1],2))+")")


if(fltQuadraticVarDisc >= 0):
    #Find the values where Y=0
    arQuadraticSolutions = findQuadraticSolutions(fltQuadraticVarDisc,arQuadraticVars[0],arQuadraticVars[1])
    print("The solutions to the functions is: X="+str(arQuadraticSolutions[0])+", X="+str(arQuadraticSolutions[1]))

    #Find the Y values to the X points
    arQuadraticRoots = findQuadraticRoots(arQuadraticSolutions,arQuadraticVars[0],arQuadraticVars[1],arQuadraticVars[2])
    print("The roots of the function are: ("+str(arQuadraticRoots[0][0])+","+str(arQuadraticRoots[0][1])+"), ("+str(arQuadraticRoots[1][0])+","+str(arQuadraticRoots[1][1])+")")









