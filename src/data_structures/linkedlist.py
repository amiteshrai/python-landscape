"""
    Implementing Linked List In Python

    A linked list is a data structure made of a chain of node objects.
    Each node contains a value and a pointer to the next node in the chain.

    Linked lists are preferred over arrays due to their dynamic size and ease of
    insertion and deletion properties.
"""


from src.utils.logger import get_logger

LOGGER = get_logger(__name__)

# Data Node Class
class Node:
    """
        The object of this class will be the actual nodes that will hold the data and
        the reference to the next node.
    """

    def __init__(self, data):
        # Define varibles to hold data and reference to next node
        self.data = data
        self.next = None


# Actual Linked List Class
class LinkedList:
    """
        The class contains actual implementation class of the linked list.
        This contains methods to insert/remove/traverse/sort/search.
    """

    def __init__(self):
        # Define a variable to hold the reference to the start node
        self.node = None

    def traverse(self):
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
                LOGGER("Index: %d, Value: %s", index, current_node.data)
                index += 1
                current_node = current_node.next

    def insert(self, data):
        """
        Insert a new data node at the end of linked list

        Arguments:
            data {str/int/float} -- The value of the new node element
        """

        # Create new node with the given data value
        new_node = Node(data)

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

    def insert_start(self, data):
        """
        Insert a data node at the beginning of the linked list

        Arguments:
            data {str/int/float} -- The value of the new node element
        """

        # Create new node with the given data value
        new_node = Node(data)

        # Assign new node's next to the current start of the linked list
        new_node.next = self.node

        # Assign the linkedlist start to the new node
        self.node = new_node

    def insert_after(self, node_data, after_data):
        """
        Insert a new data node after the node with given value

        Arguments:
            node_data {str/int/float} -- The value of the new node element
            after_data {str/int/float} -- The value of the existing node
        """

        # Get reference to the start of the linked list
        current_node = self.node

        # Iterate through the each node element, untill desired node is not found
        while current_node is not None:
            if current_node.data == after_data:
                break
            current_node = current_node.next

        # Create new node after the desired node
        if current_node is None:
            LOGGER.error("Item not present in the list")
        else:
            new_node = Node(node_data)
            new_node.next = current_node.next
            current_node.next = new_node

    def insert_befor(self, node_data, before_data):
        """
        Insert a new data node after the node with given value

        Arguments:
            node_data {str/int/float} -- The value of the new node element
            after_data {str/int/float} -- The value of the existing node
        """

    def insert_at_index(self, data, index):
        """
        Insert a new data node at the given index

        Arguments:
            node_data {str/int/float} -- The value of the new node element
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

        # Insert the new node at the specified index
        if current_node is None:
            LOGGER.error("Index out of bound error %s.", node_index)
        else:
            new_node = Node(data)
            new_node.next = current_node.next
            current_node.next = new_node
