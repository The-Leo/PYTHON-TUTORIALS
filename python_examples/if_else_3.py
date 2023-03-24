"""A Scalene triangle: ALl sides have different lengths.
Isosceles triangle: Two sides have the same length
Equilateral triangle: All sides have equal lengths"""
a = None 
while not isinstance(a, (int, float)) or a <= 0:
     try:
         a = float(input("Enter the length of the first side of the triangle: "))
         if a <= 0:
             print("The length must be a positive number.")
     except ValueError:
             print("Invalid input. The length must be a number.") 

b = None
while not isinstance(b, (int, float)) or b <= 0:
     try:
         b = float(input("Enter the length of the second side of the triangle: "))
         if b <= 0:
            print("The length must be a positive number.")
     except ValueError:
            print("Invalid input. The length must be a number.")

c = None 
while not isinstance(c, (int, float)) or c <= 0:
     try:
         c = float(input("Enter the length of the third side of the triangle: "))
         if c <= 0:
            print("The length must be a positive number.")
     except ValueError:
            print("Invalid input. The length must be a number.")


if a+b > c and a + c > b and c+b > a:
            print("These side lengths can form a valid triangle")
else:
            print("These side lengths cannot form a valid triangle")


if a != b and b != c and a != c:
    print("This is a scalene triangle")
if a == b == c:
    print("Equilateral triangle")
else: 
    print("Isosceles Triangle")



