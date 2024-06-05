class Weight:
    def gramconverter(self, value:float, convert_from:str):
        """
        Description: converts any of the weight type to grams.
        """
        match convert_from:
            case "ounce":
                gram = value * 28.34952
            case "pound":
                gram = value *  453.59237
            case "kilogram":
                gram = value * 1000
            case "gram":
                gram = value * 1
            case "tonne":
                gram = value *  1000000

        return (gram)


    def converter(self, convert_to, gram):
        """
        Description: converts grams to other type of weights.
        :return: returns the converted value
        """
        match convert_to:
            case "ounce":
                output = gram * 0.035274
            case "pound":
                output = gram * 0.00220462
            case "kilogram":
                output = gram * 0.001
            case "gram":
                output = gram * 1
            case "tonne":
                output = gram * 0.000001

        return (output)