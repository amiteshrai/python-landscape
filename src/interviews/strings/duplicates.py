"""
    Remove Duplicate Characters From String

    Description: Given a input string, remove all the duplicate characters and
    return a new string with unique characters
"""

from src.utils.logger import get_logger

LOGGER = get_logger(__name__)


def remove_duplicates(input_str: str) -> str:
    """
    Convert an input string into a new string with unique characters

    Arguments:
        input_str {string} -- input string with repeating/non-repeating characters

    Returns:
        string -- string with unique characters
    """

    unique_chars_str = ""
    unique_chars = list()
    chars_map = dict()

    # Iterate through each character in string
    for character in input_str:  # O(n)
        if not chars_map.get(character):  # O(1)
            chars_map[character] = True
            unique_chars.append(character)

    # Join all the unique characters in the list to form a string
    unique_chars_str = unique_chars_str.join(unique_chars)

    return unique_chars_str


input_value = "dsdhsjkkakdjs"
LOGGER.info("Input String : %s", input_value)

output_value = remove_duplicates(input_value)
LOGGER.info("Output Unique String : %s", output_value)

# Shorhand for the above function
output_value = "".join({char for char in input_value})
LOGGER.info(
    "Output Unique String (Single Line Solution, but without the original order) : %s",
    output_value,
)
