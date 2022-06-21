class Node:
    """
    An object for storing a single node for a linked list.

    Attributes:
        data: data stored in the node.
        next_node: reference to the next node in linked list.
    """

    def __init__(self, data = None):
        """
        Parameters:
            data: data stored in the node.
        """
        self.data = data
        self.next_node = None

    def __repr__(self):
        """
        Print the value stored in the node.
        """
        return "<Node data: %s>" % self.data

class LinkedList:
    """
    An object for singly linked list.

    Attributes:
        head: the node the linked list has reference to.

    Methods:
        is_empty()
            Determine if the linked list is empty.
        size()
            Calculate the number of nodes in the linked list.
        add(data)
            Prepend, add new node containing data to head of the linked list.
        search(key)
            Search for the first node containing data that matches the key.
        insert(data, index)
            Inserts a new node containing data at index position.
        node_at_index(index)
            Returns the node at specified index.
        remove(key)
            Removes node containing data that matches the key.
        remove_at_index(index)
            Removes node at specified index.
    """

    def __init__(self):
        self.head = None

    def __repr__(self):
        """
        Print a string representation of the linked list.
        """

        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append("[Head: %s]" % current.data)
            elif current.next_node is None:
                nodes.append("[Tail: %s]" % current.data)
            else:
                nodes.append("[%s]" % current.data)
            
            current = current.next_node
        
        return "-> ".join(nodes)

    def is_empty(self):
        """
        Determine if the linked list is empty.

        Returns:
            True if the linked list is empty .
        """

        return self.head == None

    def size(self):
        """
        Calculate the number of nodes in the linked list.

        Returns:
            the number of nodes in the linked list.
        """

        current = self.head
        count = 0

        while current:
            count += 1
            current = current.next_node
        
        return count

    def add(self, data):
        """
        Prepend, add new node containing data to head of the linked list.

        Parameters:
            data: data stored in the new node.
        """

        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node

    def search(self, key):
        """
        Search for the first node containing data that matches the key.

        Parameters:
            key: the value we want to search in the linked list.
        
        Returns:
            the node or None if not found.
        """

        current = self.head

        while current:
            if current.data == key:
                return current
            else:
                current = current.next_node
        
        return None

    def insert(self, data, index):
        """
        Inserts a new node containing data at index position.

        Parameters:
            data: data stored in the new node.
            index: the position the node insert in
        """

        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)
            current = self.head
            position = index

            while position > 1:
                current = current.next_node
                position -= 1

            previous_node = current
            next_node = current.next_node

            previous_node.next_node = new
            new.next_node = next_node

    def node_at_index(self, index):
        """
        Returns the node at specified index.

        Parameters:
            index: the position we want to find.

        Returns:
            the node at specified index.
        """

        if index == 0:
            return self.head

        current = self.head
        position = 0
           
        while position < index:
            current = current.next_node
            position += 1

        return current

    def remove(self, key):
        """
        Removes node containing data that matches the key.

        Parameters:
            key: the value we want to remove.

        Returns:
            the node or None if key doesn't exist.
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current == self.head:
                found = True
                self.head = current.next_node
                return current
            if current.data == key:
                found = True
                previous.next_node = current.next_node
                return current
            else:
                previous = current
                current = current.next_node
        
        return None


    def remove_at_index(self, index):
        """
        Removes node at specified index.

        Parameters:
            index: the position we want to remove.

        Returns:
            the node we remove.
        """
        
        current = self.head
    
        if index == 0:
            self.head = current.next_node
            return current

        position = index

        while position > 1:
            current = current.next_node
            position -= 1
        
        previous_node = current
        current = current.next_node
        next_node = current.next_node

        previous_node.next_node = next_node

        return current
