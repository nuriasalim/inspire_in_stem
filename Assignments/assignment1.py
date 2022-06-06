#area of a circle
r =input("Enter radius of the circle ")
pi = 3.142
area_of_a_circle = int(r) * int(r) * pi
print("The area of a circle is " + str(area_of_a_circle))


#volume of a cylinder
r = input("Enter the radius")
h = input("Enter the height of cylinder")
pi = 3.142
vol_of_cylinder =  pi * int(r)**2 * int(h)
print("The volume of a cylinder is " + str(vol_of_cylinder))


#surface area of a cylinder
r = input("Enter the radius")
pi = 3.142
h = input("Enter the height")
constant = input("Enter constant")
areaOfACylinder= int(constant) * pi * int(h) * int(r)
areaOfACircle= int(constant) * pi * int(r)**2
sum_of = areaOfACircle + areaOfACylinder
surfaceAreaOfACylinder = sum_of
print("The surface area of a cylinder is " + str(surfaceAreaOfACylinder))

