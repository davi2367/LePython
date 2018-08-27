print("Insert Quadratic Fuction")
print("Example: ax^2+bx+c")

#Collects the fuction from user. 
strQuadratic = input("f(x)=")

def quadraticSplitter(strToSplit):
    import re
    match = re.search("EXPRESSION",strQuadratic)
    return splitResult