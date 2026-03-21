def trag():
    a=int(input("Enter the first side of the triangle: "))
    b=int(input("Enter the second side of the triangle: "))
    c=int(input("Enter the third side of the triangle: "))
    d=a+b>c and a+c>b and b+c>a
    print(d)
trag()