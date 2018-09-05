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


