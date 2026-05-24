class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    
class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node
        
    def delete(self, data):
        pass
    
    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")



ll = LinkedList()
ll.insert_at_beginning(10)
ll.insert_at_end(20)
ll.display()