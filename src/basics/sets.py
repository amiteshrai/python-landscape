"""Sets In Python """

from src.utils.logger import get_logger

LOGGER = get_logger(__name__)

# Defining a set
fruits = {"apple", "banana", "cherry"}
# OR
fruits = set(("apple", "banana", "cherry"))
LOGGER.info("Fruits : %s", fruits)

# Adding an element
fruit_to_add = "orange"
fruits.add(fruit_to_add)
LOGGER.info("Fruits after adding '%s' : %s", fruit_to_add, fruits)

# Adding an existing element
fruits.add(fruit_to_add)
LOGGER.info("Fruits after adding an existing fruit '%s' : %s", fruit_to_add, fruits)

# Removing an existing element
fruit_to_remove = "banana"
fruits.remove(fruit_to_remove)
LOGGER.info("Fruits after removing '%s' : %s", fruit_to_remove, fruits)

# Removing a non-existing element
try:
    fruits.remove(fruit_to_remove)
    LOGGER.info(
        "Fruits after removing non-existing fruit '%s' : %s", fruit_to_remove, fruits
    )
except KeyError:
    LOGGER.error("KeyError : '%s' is not present in set", fruit_to_remove)


# Removing a non-existing element without raising error
try:
    fruits.discard(fruit_to_remove)
    LOGGER.info(
        "Fruits after removing non-existing fruit '%s' : %s", fruit_to_remove, fruits
    )
except KeyError:
    LOGGER.error("KeyError : '%s' is not present in set", fruit_to_remove)

# Removing the last element from set
fruits.pop()
LOGGER.info("Fruits after removing last fruit using 'pop' : %s", fruits)

fruits.clear()
LOGGER.info("Fruits after clearing all the fruits in it : %s", fruits)

# Updating set with values in another set
fruits_extended = {"papaya", "guava", "mango"}
fruits.update(fruits_extended)
LOGGER.info(
    "Fruits after updated with fruites from set `%s` : %s", fruits_extended, fruits
)

# OR
fruits_extended = {"apple", "banana", "cherry"}
fruits = fruits.union(fruits_extended)
LOGGER.info(
    "Fruits after union with another set of fruits `%s` : %s", fruits_extended, fruits
)

# Deleting the set
del fruits
try:
    LOGGER.info("Fruits after deletion : %s", fruits)
except NameError as e:
    LOGGER.error(e)
