"""
    Basics Of Command Line Arguments In Python

    Further reading :
    1. Short vs Long Options
    2. Conflictiong Options & Mutually Exclusive Groups
"""

import argparse

from src.utils.logger import get_logger

LOGGER = get_logger(__name__)

# Define a command line arg parser
basic_calculator = argparse.ArgumentParser(
    description="A simple command line calculator",
    epilog="""
        Example usage:
        > python commandline.py add 3 2
        > output: 5
    """,
)
# Define arguments for operator function and operands
basic_calculator.add_argument(
    "operator_func", action="store", help="add/subtract/multiply/divide", type=str,
)
basic_calculator.add_argument("--x", required=True, type=float, help="First operand")
basic_calculator.add_argument("--y", required=True, type=float, help="Second operand")


def calculate(operator_func: str, x: float, y: float) -> float:
    """
    Apply the given operator function on the given operands

    Arguments:
        operator_func {str} -- The funtion to be applied
        x {float} -- First operand
        y {float} -- Second operand

    Raises:
        ValueError: Raise error when operator function is not supported

    Returns:
        float -- Output of the applied function
    """

    value = None

    if operator_func.lower() == "add":
        value = x + y
    elif operator_func.lower() == "subtract":
        value = x - y
    elif operator_func.lower() == "multiply":
        value = x * y
    elif operator_func.lower() == "divide":
        value = x / y
    else:
        raise ValueError(
            "Unsupported Operation {}. Please see help section! ".format(operator_func)
        )

    return value


if __name__ == "__main__":
    # Parse command line arguments
    args = basic_calculator.parse_args()

    # Convert command line arguments to dictionary
    arg_vars = vars(args)
    LOGGER.debug("Input Arguments : %s", arg_vars)
    output = calculate(**arg_vars)
    LOGGER.debug("Calculator Output : %s", output)

# Running the file: python src/basics/comandline.py add -x=3 -y=2
