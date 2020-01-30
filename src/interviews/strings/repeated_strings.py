"""
    Repeated String
    (Hackerrank => https://www.hackerrank.com/challenges/repeated-string/problem)

    Lila has a string, , of lowercase English letters that she repeated infinitely many
    times. Given an integer, N, find and print the number of letter a's in the first N
    letters of Lilah's infinite string.

    For example, if the string s=`abca` and N=10, the substring we consider is
    `abcacabcac`, the first  characters of her infinite string.
    There are 4 occurrences of a in the substring.

    Constraints:
        1<= |s| <= 100
        1 <= n <= 10^12
"""
import math

from src.utils.logger import get_logger

LOGGER = get_logger(__name__)


def repeated_char_counter(s: str, n: int) -> int:
    """ Repeated String Counter Function """

    LOGGER.info("Input Parameters : s=%s, n=%d", s, n)

    s_length = len(s)
    # Validate input parameters
    if not 1 <= s_length <= 100:
        raise ValueError(
            """
            Invalid Input String {} With Length {}.
            Expected String Of Length Between {}""".format(
                s, len(s), "1 to 100",
            )
        )
    if not 1 <= n <= 10 ** 12:
        raise ValueError(
            "Invalid Repeating Parameter {}. Expected A Value Between {}".format(
                n, "1 to 10^12"
            )
        )

    # Initialize Counter
    a_count = 0
    s_repeated = math.ceil(n / s_length)
    repeated_s = s * s_repeated
    repeated_s = repeated_s[:n]
    list_of_a = [char for char in repeated_s if char == "a"]
    a_count = len(list_of_a)
    LOGGER.info("Output : %d", a_count)

    return a_count


def repeated_char_counter_optimized(s: str, n: int) -> int:
    """ Repeated String Counter Function """

    LOGGER.info("Input Parameters : s=%s, n=%d", s, n)

    s_length = len(s)
    # Validate input parameters
    if not 1 <= s_length <= 100:
        raise ValueError(
            """
            Invalid Input String {} With Length {}.
            Expected String Of Length Between {}""".format(
                s, len(s), "1 to 100",
            )
        )
    if not 1 <= n <= 10 ** 12:
        raise ValueError(
            "Invalid Repeating Parameter {}. Expected A Value Between {}".format(
                n, "1 to 10^12"
            )
        )

    # Initialize Counter
    a_count = len([char for char in s if char == "a"])
    quotient = int(n / s_length)
    a_count = a_count * quotient
    remainder = n - (s_length * quotient)
    remainder_a_count = len([char for char in s[:remainder] if char == "a"])
    a_count = a_count + remainder_a_count
    LOGGER.info("Output : %d", a_count)

    return a_count


s1 = "aba"
n1 = 10
output1 = repeated_char_counter(s1, n1)

s2 = "a"
n2 = 1000000000000
output2 = repeated_char_counter_optimized(s2, n2)
output3 = repeated_char_counter(s2, n2)
