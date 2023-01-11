ab = float(input("enter ab = "))
bc = float(input("enter bc = "))
ac = float(input("enter ac = "))

m = (ab + bc)
n = (ab + ac)
q = (bc + ac)

if m >= ac:
    if m == ac :
        print("ac unsuccessful")
    else :
        print("ac successful")
    
else :
    print("ac unsuccessful")

if n >= bc:
    if n == bc :
        print("bc unsuccessful")
    else :
        print("bc successful")

else :
    print("bc unsuccessful")

if q >= ab:
    if q == ab :
        print("ab unsuccessful")
    else :
        print("ab successful")

else :
    print("ab unsuccessful")



