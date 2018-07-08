class Node(object):
    """Represents a singly linked node."""

    def __init__(self, data, next=None):
        """Instantiates a Node with a default next to None."""
        self.data = data
        self.next = next

class TwoWayNode(Node):
    def __init__(self, data, previous = Node, next  = None):
        """Instantiates a Two Way Node"""
        Node.__init__(self, data, next)
        self.previous = previous

