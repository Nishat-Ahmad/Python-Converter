from math import sqrt

class Three_dimensional:
    def squarepyramid(self, base_len:float=0, height:float=0, find:str="") -> float:
        # for isoceles triangle
        if find == "isocelesvolume":
            return_value =  (base_len ** 2 + base_len * sqrt(base_len ** 2 + (2 * height) ** 2))
        elif find == "isocelessurfacearea":
            return_value = (1/3 * base_len ** 2 * height)

        #for equilateral triangle
        elif find == "equilateralvolume":
            return_value = ((1 + sqrt(3)) * base_len ** 2)
        elif find == "equilateralsurfacearea":
            return_value = ((sqrt(2) / 6) * base_len ** 3)

        return (return_value)


    def sphere(self, radius:float, find:str) -> float:
        # finds volume and surface area of sphere
        if find == "volume":
            return ((4 / 3) * (radius ** 3) * 3.141592653589793238)
        elif find == "surfacearea":
            return ((4 * 3.141592653589793238 * radius ** 2))


    def cylinder(self, radius:float, height:float, find:str) -> float:
        # finds volume and surface area of cylinder
        if find == "volume":
            return ((3.141592653589793238 * (radius ** 2)) * height)
        elif find == "surfacearea":
            return((2 * 3.141592653589793238 * radius ** 2) + (2 * 3.141592653589793238 * radius * height))


    def cone(self, height:float=0, slanted_height:float=0, radius:float=0, find:str="") -> float:
        # finds volume and surface area of cone
        if find == "volume":
            return (((1 / 3) * 3.141592653589793238) * ((radius ** 2) * height))
        elif find == "surfacearea":
            return ((3.141592653589793238 * radius * slanted_height) + (3.141592653589793238 * (radius ** 2)))


    def cuboid(self, height:float, length:float, width:float, find:str) -> float:
        # finds volume and surface area of cuboid
        if find == "volume":
            return (length * height * width)
        elif find == "surfacearea":
            return (2*(length * width + width * height + width * height))


    def triangular_prism(self, height:float=0, length:float=0, slanted_length:float=0, breadth:float=0, find:str=0) -> float:
        # finds volume and surface area of triangular prism
        if find == "volume":
            return (1 / 2 * breadth * length * height)
        elif find == "surfacearea":
            return ((breadth * height) + (2*(slanted_length * length)) + (length * breadth))


    def cube(self, length:float, find:str) -> float:
        # finds volume and surface area of cube
        if find == "volume":
            return (length ** 3)
        elif find == "surfacearea":
            return (6 * (length ** 2))


    def hemisphere(self, radius:float, find:str) -> float:
        # finds volume and surface area of hemisphere
        if find == "volume":
            return (2 / 3 * 3.141592653589793238 * radius ** 3)
        elif find == "surfacearea":
            return (3 * 3.141592653589793238 * radius ** 2)


class Two_dimensional:
    def square(self, side: float, find: str) -> float:
        # finds perimeter and area of square
        if find == "area":
            return side * side
        elif find == "perimeter":
            return side * 4


    def rectangle(self, length: float, width: float, find:str) -> float:
        # finds perimeter and area of rectangle
        if find == "area":
            return length * width
        elif find == "perimeter":
            return (2 * length) + (2 * width)


    def parallelogram(self, base:float=0, height:float=0, slanted_height:float=0, find:str="") -> float:
        # finds perimeter and area of parallelogram
        if find == "area":
            return base * height
        elif find == "perimeter":
            return (2*(slanted_height + base))


    def trapezium(self, side1:float=0, side2:float=0, height:float=0, slanted_side1:float=0, slanted_side2:float=0, find:str="") -> float:
        # finds perimeter and area of trapezium
        if find == "area":
            return 0.5 * (side1 + side2) * height
        elif find == "perimeter":
            return (side1 + side2 + slanted_side1 + slanted_side2)


    def circle(self, radius:float, find:float) -> float:
        # finds circumfrence and area of trapezium
        if find == "area":
            return radius * radius * 3.141592653589793238
        elif find == "circumfrence":
            return 2 * radius * 3.141592653589793238


    def triangle(self, base:float=0, height:float=0, side1:float=0, side2:float=0, find:str="") -> float:
        # finds area and perimeter of triangle
        if find == "area":
            return base * height * 0.5
        elif find == "perimeter":
            return side1 + side2 + base


    def kite(self, diognal1:float=0, diognal2:float=0, side1:float=0, side2:float=0, find:str="") -> float:
        # finds area and perimeter of kite
        if find == "area":
            return 0.5 * diognal1 * diognal2
        elif find == "perimeter":
            return (side1 * 2) + (side2 * 2)