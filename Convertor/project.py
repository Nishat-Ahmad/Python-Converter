import angle
import currency
import geometry
import temprature
import weight

def main():
    print_value: float = 0.00
    functionality: str = input("What do you want to calculate: angle / currency / geometry / temprature / weight: ").lower().replace(" ", "")

    if functionality == "temprature" or functionality == "angle" or functionality == "weight":
        convert_from = input("what to convert from: ").lower().replace(" ", "")
        convert_to = input("what to convert to: ").lower().replace(" ", "")
        convert_this: float = float(input(f"input the number of {convert_from} that needs to be converted: "))

    match functionality:
        case "temprature":
            print_value = temprature_caller(convert_from, convert_to, convert_this)
        case "angle":
            print_value = angle_caller(convert_from, convert_to, convert_this)
        case "weight":
            print_value = weight_caller(convert_from, convert_to, convert_this)
        case "geometry":
            print_value = geometry_caller()
        case "weight":
            print_value = weight_caller(convert_from, convert_to, convert_this)

        case "currency":
            convert_from: str = input("what to convert from: ").replace(" ", "")
            convert_to: str = input("what to convert to: ").replace(" ", "")
            print_value = currency_caller(convert_from, convert_to)

    print(print_value)


def weight_caller(convert_from, convert_to, convert_this):
    cweight = weight.Weight()
    gram = cweight.gramconverter(convert_this, convert_from)
    return cweight.converter(convert_to, gram)


def currency_caller(convert_from, convert_to):
    return currency.converter(convert_from, convert_to)


def geometry_caller():
    three_dimensional = geometry.Three_dimensional()
    two_dimensional = geometry.Two_dimensional()

    shape = input("Input the shape: ").lower().replace(" ", "")
    find = input("Input what to find: ").lower().replace(" ", "")

    if shape == "sphere" or shape == "cylinder" or shape == "cone" or shape == "hemisphere" or shape == "circle":
        radius = int(input("Input the radius: "))
    if shape == "cube" or shape == "cuboid" or shape == "triangularprism" or shape == "square" or shape == "rectangle":
        length = int(input("Input the length: "))
    if shape == "cylinder" or shape == "triangularprism" or shape == "cuboid":
        height = int(input("Input the height: "))
    if shape == "cuboid" or shape == "triangularprism" or shape == "rectangle":
        width = int(input("Input the width: "))
    if find == "perimeter" and (shape == "trapezium" or shape == "kite" or shape == "triangle"):
        side1 = int(input("Input the length of the first side: "))
        side2 = int(input("Input the length of the second side: "))
    if find == "parallelogram" or find == "triangle" or find == "squarepyramid":
        base = int(input("Input the length of the base: "))

    match shape:
        case "circle":
            return_value = two_dimensional.circle(radius, find)
        case "rectangle":
            return_value = two_dimensional.rectangle(length, width, find)
        case "square":
            return_value = two_dimensional.square(length, find)
        case "sphere":
            return_value = three_dimensional.sphere(radius, find)
        case "cylinder":
            return_value = three_dimensional.cylinder(radius, height, find)
        case "cube":
            return_value = three_dimensional.cube(length, find)
        case "hemisphere":
            return_value = three_dimensional.hemisphere(radius, find)
        case "cuboid":
            return_value = three_dimensional.cuboid(height, length, width, find)

        case "trapezium":
            side1 = int(input("Input the length of the first side: "))
            side2 = int(input("Input the length of the second side: "))

            if find == "area":
                height = int(input("Input the height: "))
                return_value = two_dimensional.trapezium(side1, side2, height, 0, 0, find)
            elif find == "perimeter":
                return_value = two_dimensional.trapezium(side1, side2, 0, side1, side2, find)

        case "parallelogram":
            if find == "area":
                height = int(input("Input the height: "))
                return_value = two_dimensional.parallelogram(base, height, 0, find)
            elif find == "perimeter":
                slanted_height = int(input("Input the slanted height: "))
                return_value = two_dimensional.parallelogram(base, 0, slanted_height, find)

        case "kite":
            if find == "area":
                dioagnal1 = int(input("Input the length of the first diognal: "))
                dioagnal2 = int(input("Input the length of the second diognal: "))
                return_value = two_dimensional.kite(dioagnal1, dioagnal2, 0, 0, find)
            elif find == "perimeter":
                return_value = two_dimensional.kite(0, 0, side1, side2, find)

        case "triangle":
            if find == "area":
                height = int(input("Input the height: "))
                return_value = two_dimensional.triangle(base, height, 0, 0, find)
            elif find == "perimeter":
                return_value = two_dimensional.triangle(base, 0, side1, side2, find)

        case "cone":
            if find == "volume":
                height = int(input("Input the height: "))
                return_value = three_dimensional.cone(height, 0, radius, find)
            elif find == "surfacearea":
                slanted_height = int(input("Input the slanted height: "))
                return_value = three_dimensional.cone(0, slanted_height, radius, find)

        case "triangularprism":
            if find == "volume":
                return_value = three_dimensional.triangular_prism(height, length, 0, width, find)
            elif find == "surfacearea":
                slanted_length = int(input("Input the slanted height: "))
                return_value = three_dimensional.triangular_prism(height, length, slanted_length, width, find)

        case "squarepyramid":
            if find == "equilateralvolume" or find == "equilateralsurfacearea":
                return_value = three_dimensional.squarepyramid(base, 0, find)
            elif find == "isocelesvolume" or find == "isocelessurfacearea":
                height = int(input("Input the height: "))
                return_value = three_dimensional.squarepyramid(base, height, find)

    return (return_value)


def angle_caller(convert_from, convert_to, convert_this_value):
    return_value = 0

    if convert_from == "degree" and convert_to == "radian":
        return_value = angle.degree_to_radian(convert_this_value)
    elif convert_from == "degree" and convert_to == "gradian":
        return_value = angle.degree_to_gradian(convert_this_value)
    elif convert_from == "radian" and convert_to == "degree":
        return_value = angle.radian_to_degree(convert_this_value)
    elif convert_from == "radian" and convert_to == "gradian":
        return_value = angle.radian_to_gradian(convert_this_value)
    elif convert_from == "gradian" and convert_to == "radian":
        return_value = angle.gradian_to_radian(convert_this_value)
    elif convert_from == "gradian" and convert_to == "degree":
        return_value = angle.gradian_to_degree(convert_this_value)

    return (return_value)

def temprature_caller(convert_from, convert_to, value_to_be_converted):
    return_value = 0
    if convert_from == "celsius" and convert_to == "farenheit":
        return_value: float = temprature.celsius_to_farenheit(value_to_be_converted)
    elif convert_from == "celsius" and convert_to == "kelvin":
        return_value = temprature.celsius_to_kelvin(value_to_be_converted)
    elif convert_from == "kelvin" and convert_to == "celsius":
        return_value = temprature.kelvin_to_celsius(value_to_be_converted)
    elif convert_from == "kelvin" and convert_to == "farenheit":
        return_value = temprature.kelvin_to_farenheit(value_to_be_converted)
    elif convert_from == "farenheit" and convert_to == "kelvin":
        return_value = temprature.farenheit_to_kelvin(value_to_be_converted)
    elif convert_from == "farenheit" and convert_to == "celsius":
        return_value = temprature.farenheit_to_celsius(value_to_be_converted)

    return (return_value)


if __name__ == "__main__":
    main()