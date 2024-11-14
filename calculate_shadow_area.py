def calculate_shadow_area(D):
    pi=3.14
    area=pi*D*D
    return round(area)

D=int(input("Enter value of radius: "))
print("The area of given circle is",calculate_shadow_area(D))


