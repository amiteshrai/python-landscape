""" Calc Module """


def add(x: float, y: float) -> float:
    """ Add Function """

    return x + y


def subtract(x: float, y: float) -> float:
    """ Subtract Function """

    return x - y


def multiply(x: float, y: float) -> float:
    """ Multiply Function """

    return x * y


def divide(x: float, y: float) -> float:
    """ Divide Function """

    if y == 0:
        raise ValueError("Cannot Divide By Zero!")

    return x // y


def remainder(x: float, y: float) -> float:
    """ Remainder Function """

    return x % y
