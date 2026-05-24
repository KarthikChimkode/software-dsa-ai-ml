from typing import Optional

class Node:
    def __init__(self, data):
        self.data = data
        self.next: Optional['Node'] = None


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

    def insert_after(self, prev_data, data):
        current = self.head
        while current and current.data != prev_data:
            current = current.next
        if not current:
            print("Node not found!")
            return
        new_node = Node(data)
        new_node.next = current.next
        current.next = new_node


    def delete(self, key):
        current = self.head

        if not current:
            return
        
        if current.data == key:
            self.head = current.next
            current = None
            return 
        
        prev = None
        while current and current.data != key:
            prev = current
            current = current.next

        if not current:
            print("Node not found!")
            return
        
        if prev is not None:
            prev.next = current.next
        current = None

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" ->")
            current = current.next 
        print("None")

ll = LinkedList()
ll.insert_at_end(10)
ll.insert_at_end(20)
ll.display()
ll.insert_after(10, 30)
ll.display()