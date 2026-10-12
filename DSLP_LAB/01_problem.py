print("----Menu---\n" \
"1.find area of triangle\n" \
"2.find area of rectangle\n" \
"3.find area of circle")

choice=int(input("Enter choice:"))

if choice==1:
    a = int(input("Enter base of triangle:"))
    b = int(input("Enter height of triangle:"))

    print("Area of triangle is",a*b*0.5)

elif choice==2:
    a = int(input("Enter breath of rectanglele:"))
    b = int(input("Enter length of rectangle:"))
    print("Area of Rectangle is",a*b)

elif choice==3:
    a = float(input("Enter radius of circle:"))
    
    print("Area of Rectangle is",a**2*3.14)

else:
    print("Invalid choice!")
    