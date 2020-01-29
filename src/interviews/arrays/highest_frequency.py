"""
    Highest Frequency Element

    Description: Given an array of strings, find the string with maximum frequency.
"""

from src.utils.logger import get_logger

LOGGER = get_logger(__name__)


def highestFrequencyString(strings_arr: list) -> str:
    """
    Given an array of strings, find the string with maximum frequency.

    Arguments:
        strings {list<string>} -- array of strings

    Returns:
        string -- string with max frequency in given array
    """

    maxFreq = 0
    maxFreqString = strings_arr[0]
    stringFreqMap = dict()
    stringFreq = 0

    for current_str in strings_arr:
        stringFreq = stringFreqMap.get(current_str)
        if stringFreq:
            stringFreq = stringFreq + 1
        else:
            stringFreq = 1

        stringFreqMap[current_str] = stringFreq

        # Update string with max frequency
        if stringFreq > maxFreq:
            maxFreq = stringFreq
            maxFreqString = current_str

    return maxFreqString


inputs = ["a", "b", "c", "d", "b", "a", "d", "a"]
LOGGER.info("Input Array Of Strings : %s", inputs)

output = highestFrequencyString(inputs)
LOGGER.info("Output String With Max Frequency : %s", output)
