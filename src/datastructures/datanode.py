"""
    The DataNode Class

    This class will be used across multiple data structure implementations and contains
    the data value as well as the references to the next and previous data nodes
"""

# DataNode Class Implementation
class DataNode:
    """
        The object of this class will be the actual nodes that will hold the data and
        the reference to the next data node.
    """

    def __init__(self, value):
        # Define varibles to hold data and reference to next data node
        self._value = value
        self._next = None
        self._previous = None

    @property
    def value(self):
        """
        Defines a property getter for data attribute using decorator

        Returns:
            any -- The data value of the data node
        """

        return self._value

    @property
    def next(self):
        """
        Defines a property getter for next data node using decorator

        Returns:
            DataNode -- The reference of the next data node in the list
        """

        return self._next

    @property
    def previous(self):
        """
        Defines a property getter for previous data node using decorator

        Returns:
            DataNode -- The reference of the previous data node in the list
        """

        return self._previous

    @value.setter
    def value(self, value):
        self._value = value

    @next.setter
    def next(self, next_node):
        if next_node is not None and isinstance(next_node, DataNode):
            raise ValueError("The reference is not of type DataNode")

        self._next = next_node

    @previous.setter
    def previous(self, previous_node):
        if previous_node is not None and isinstance(previous_node, DataNode):
            raise ValueError("The reference is not of type DataNode")

        self._previous = previous_node

    def __str__(self):
        return "DataNode{" + "value={}".format(self._value) + "}"
