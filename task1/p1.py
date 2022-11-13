def areaRectangle(a, b):
    return (a * b)

def perimeterRectangle(a, b):
    return (2 * (a + b))
a = int(input("Enter a width: "))
b =  int(input("Enter a lenth: "))
print ("Area = ", areaRectangle(a, b))
print ("Perimeter = ", perimeterRectangle(a, b))
