import requests


def converter(to_convert_from: str, to_convert_to:str) -> None:
    """
    Description: takes both the currency that needs to be converted and to what it is to be converted to.
    :param to_convert_from: from which currency is the value to be derived
    :param to_convert_to: currency to which the currency needs to be converted
    """
    rate: str = requests.get(f"https://api.exchangerate-api.com/v4/latest/{to_convert_from}").json()

    _ = (rate["rates"][to_convert_to])
    return (f"1 {to_convert_from} is {_} {to_convert_to}") 