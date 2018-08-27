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
    verifyResult = re.search(r"\d{1,5}x\^2[+|-]\d{1,5}x[+|-]\d{1,5}",strToVerify)
    return verifyResult

#
def quadraticSplitter(strToSplit):
    import re

    return splitResult



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

#Splitting Quadratic Function

