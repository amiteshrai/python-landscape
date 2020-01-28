"""
    Array Flattener Module

    Given and N-dimensional input array, convert it to 1-dimensional array
"""

from src.utils.logger import get_logger

LOGGER = get_logger(__name__)


def flatten(input_arr: list) -> list:
    """
    Given an input of N-dimensional array, convert it to 1-dimensional array while
    preserving element positions

    Arguments:
        input_arr {list} -- N-dimensional input array

    Returns:
        list -- 1-dimensional output array
    """

    LOGGER.info("Input Array : %s ", input_arr)

    output_arr = []

    # Iterate through each element
    for element in input_arr:
        if isinstance(element, list):
            # Recursive call to extract elements from array
            flattened_elements = flatten(element)

            for value in flattened_elements:
                output_arr.append(value)
        else:
            output_arr.append(element)

    return output_arr


in_arr = [1, [2, 3], [[4, 5], [[6, 7], [8, [9, 10]]]]]
out_arr = flatten(in_arr)
LOGGER.info("Output Array : %s ", out_arr)
