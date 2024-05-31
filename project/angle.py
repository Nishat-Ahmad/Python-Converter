def degree_to_radian(degree: float) -> float:
    """
    Description: converts degree to radians
    :param degree: this value is converted to raidan
    :type degree: float
    :raise TypeError: when the parameter is not float
    :return: the value that is converted to radian
    :rtype: float
    """
    return (degree * 3.141592653589793238/180)


def radian_to_degree(radian: float) -> float:
    """
    Description: converts radians to degrees
    :param radian: this value is converted to degree
    :type radian: float
    :raise TypeError: when the parameter is not float
    :return: the value that is converted to degree
    :rtype: float
    """
    return (radian * 180/3.141592653589793238)


def gradian_to_radian(gradian: float) -> float:
    """
    Description: converts gradians to radians
    :param gradian: this value is converted to raidan
    :type gradian: float
    :raise TypeError: when the parameter is not float
    :return: the value that is converted to radian
    :rtype: float
    """
    return (gradian * 3.141592653589793238/200)


def radian_to_gradian(radian: float) -> float:
    """
    Description: converts radians to gradians
    :param radian: this value is converted to graidan
    :type radian: float
    :raise TypeError: when the parameter is not float
    :return: the value that is converted to gradian
    :rtype: float
    """
    return (radian *  200/3.141592653589793238)


def gradian_to_degree(gradian: float) -> float:
    """
    Description: converts gradians to degrees
    :param gradian: this value is converted to degree
    :type gradian: float
    :raise TypeError: when the parameter is not float
    :return: the value that is converted to degree
    :rtype: float
    """
    return (gradian * 180/200)


def degree_to_gradian(degree: float) -> float:
    """
    Description: converts degree to gradians
    :param degree: this value is converted to graidan
    :type degree: float
    :raise TypeError: when the parameter is not float
    :return: the value that is converted to gradian
    :rtype: float
    """
    return (degree * 200/180)