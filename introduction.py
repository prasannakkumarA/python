# mini calculator
a=int(input())
b=int(input())
ope=input("add/sub/mul/div:")

if (ope=="add"):
    print(a+b)
elif (ope=="sub"):
    print(a-b)
elif (ope=="mul"):
    print(a*b)
elif (ope=="div"):
    print(a/b)
else:
    print("invalid values")
 
