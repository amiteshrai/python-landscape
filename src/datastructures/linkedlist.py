"""
    Implementing Linked List In Python

    A linked list is a data structure made of a chain of data node objects.
    Each data node contains a value and a pointer to the next data node in the chain.

    Linked lists are preferred over arrays due to their dynamic size and ease of
    insertion and deletion properties.
"""

from src.datastructures.datanode import DataNode
from src.utils.logger import get_logger

LOGGER = get_logger(__name__)


# SinglyLinkedList Class Implementation
class SinglyLinkedList:
    """
        The class contains actual implementation class of the linked list.
        This contains methods to insert/remove/traverse/sort/search.
    """

    def __init__(self):
        # Define a variable to hold the reference to the start data node
        self.node = None

    def traverse(self) -> None:
        """
            Traverse through linked list and print the elements
        """

        if self.node is None:
            LOGGER.info("List is empty")
            return
        else:
            current_node = self.node
            index = 0
            while current_node is not None:
                LOGGER("Index: %d, Value: %s", index, current_node.value)
                index += 1
                current_node = current_node.next

    def insert(self, value) -> None:
        """
        Insert a new data node at the end of linked list with given data value

        Arguments:
            value {any} -- The value of the new node element
        """

        # Create new node with the given data value
        new_node = DataNode(value)

        # If no data node is found, create
        if self.node is None:
            self.node = new_node
            return

        # Get reference to the start of the linked list
        current_node = self.node

        # Iterate through the data nodes till last node present
        while current_node.next is not None:
            current_node = current_node.next

        # Point the last data node's next to the new data node
        current_node.next = new_node

    def insert_start(self, value) -> None:
        """
        Insert a data node at the beginning of the linked list with gievn value

        Arguments:
            value {any} -- The value of the new node element
        """

        # Create new data node with the given value
        new_node = DataNode(value)

        # Assign new node's next to the current start of the linked list
        new_node.next = self.node

        # Assign the linkedlist start to the new node
        self.node = new_node

    def insert_after(self, new_value, current_value) -> None:
        """
        Insert a new data node with the given value after the node with given value

        Arguments:
            new_value {any} -- The value of the new node element
            current_value {any} -- The value of the existing node
        """

        # Get reference to the start of the linked list
        current_node = self.node

        # Iterate through the each node element, untill desired node is not found
        while current_node is not None:
            if current_node.value == current_value:
                break
            current_node = current_node.next

        # Create new node after the desired node
        if current_node is None:
            LOGGER.error("Item not present in the list")
        else:
            new_node = DataNode(new_value)
            new_node.next = current_node.next
            current_node.next = new_node

    def insert_befor(self, new_value, current_value) -> None:
        """
        Insert a new data node after the node with given value

        Arguments:
            new_value {any} -- The value of the new node element
            current_value {any} -- The value of the existing node
        """

        # TODO

    def insert_at_index(self, value, index) -> None:
        """
        Insert a new data node with the given value at the given index

        Arguments:
            value {any} -- The value of the new node element
            index {int} -- The value of the index at which the new node will be inserted
        """

        # Check if index is a positive and non-zero value
        if index < 1:
            LOGGER.error("Index cannot be a negative value")

        node_index = 1
        current_node = self.node

        # Iterate through the linked list while index is not reached
        while current_node is not None and node_index < (index - 1):
            current_node = current_node.next
            node_index += 1

        # Insert the new data node at the specified index
        if current_node is None:
            LOGGER.error("Index out of bound error %s.", node_index)
        else:
            new_node = DataNode(value)
            new_node.next = current_node.next
            current_node.next = new_node

    def __str__(self) -> str:
        """
        Override str method to print the list

        Returns:
            str -- String representation of the list
        """

        # list string start
        list_str = "SinglyLinkedList [ "
        while self.node is not None:
            list_str = "{}{}".format(list_str, self.node)
            self.node = self.node.next

            if self.node is not None:
                list_str = "{} -> ".format(list_str)

        # list string end
        list_str = "{} ]".format(list_str)

        return list_str


list1 = SinglyLinkedList()
list1.insert(20)
list1.insert_start(15)
list1.insert_start(10)
LOGGER.info("%s", list1)
