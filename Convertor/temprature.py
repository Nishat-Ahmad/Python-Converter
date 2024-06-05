def celsius_to_farenheit(celsius: float) -> float:
    """
    Description: converts celsius to farenheit
    :param celsius: this value is converted to farenheit
    :type celsius: float
    :raise TypeError: when the parameter is not float
    :return: the value that is converted to farenheit
    :rtype: float
    """
    return ((celsius * 9/5) + 32)


def celsius_to_kelvin(celsius: float) -> float:
    """
    Description: converts celsius to kelvin
    :param celsius: this value is converted to kelvin
    :type celsius: float
    :raise TypeError: when the parameter is not float
    :return: the value that is converted to celsius
    :rtype: float
    """
    return (celsius + 273.15)


def kelvin_to_celsius(kelvin: float) -> float:
    """
    Description: converts kelvin to celsius
    :param kelvin: this value is converted to celsius
    :type kelvin: float
    :raise TypeError: when the parameter is not float
    :return: the value that is converted to celsius
    :rtype: float
    """
    return (kelvin - 273.15)


def kelvin_to_farenheit(kelvin: float) -> float:
    """
    Description: converts kelvin to farenheit
    :param kelvin: this value is converted to farenheit
    :type kelvin: float
    :raise TypeError: when the parameter is not float
    :return: the value that is converted to farenheit
    :rtype: float
    """

    return ((kelvin - 273.15) * 9/5 + 32)


def farenheit_to_kelvin(farenheit: float) -> float:
    """
    Description: converts farenheit to kelvin
    :param farenheit: this value is converted to kelvin
    :type farenheit: float
    :raise TypeError: when the parameter is not float
    :return: the value that is converted to kelvin
    :rtype: float
    """
    return ((farenheit - 32) * 5/9 + 273.15)


def farenheit_to_celsius(farenheit: float) -> float:
    """
    Description: converts farenheit to celsius
    :param farenheit: this value is converted to celsius
    :type farenheit: float
    :raise TypeError: when the parameter is not float
    :return: the value that is converted to celsius
    :rtype: float
    """
    return ((farenheit - 32) * 5/9)