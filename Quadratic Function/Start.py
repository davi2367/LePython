print("Insert Quadratic Fuction")
print("Example: ax^2+bx+c")

#Collects the fuction from user. 
strQuadratic = input("f(x)=")

def quadraticSplitter(strToSplit):
    import re
    match = re.search(r"\d{1,5}x\^2[+|-]\d{1,5}x[+|-]\d{1,5}",strQuadratic)
    return splitResult