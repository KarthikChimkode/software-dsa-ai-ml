class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# class LinkedList:
#     def __init__(self, value):
#         new_node = Node(value)
#         self.head = new_node
#         self.tail = new_node
#         self.length = 1


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def append(self, value): #Time complexity will be O(1) and spcae complexity O(1) 
        new_node = Node(value)  #----------> O(1)
        if self.head is None:   #----------> O(1)
            self.head = new_node  #both
            self.tail = new_node #----------> O(1)
        else:
            self.tail.next = new_node #----------> O(1)
            self.tail = new_node      #----------> O(1)
        self.length += 1 #----------> O(1)

#we can call it insert(insert in last ) ot append both
    # def append(self, value):
    #     new_node = Node(value)
    #     if self.head is None and self.tail is None:
    #         self.head = new_node
    #         self.tail = new_node
    #     else:
    #         self.tail.next = new_node
    #         self.tail = new_node
    #     self.length += 1
      
    
    def prepend(self, value): #Time complexity will be O(1) and spcae complexity O(1) 
        new_node = Node(value) #----------> O(1)
        if self.head is None: #----------> O(1)
            self.head  = new_node#----------> O(1)
            self.tail = new_node
        else:
            new_node.next = self.head #----------> O(1)
            self.head = new_node
        self.length += 1

    def insert(self, index, value): #Time complexity will be O(n) and spcae complexity O(1)
        new_node = Node(value)  #----------> O(1)
        if index < 0 or index > self.length:  #----------> O(1)
            return False 
        elif self.length == 0:      #----------> O(1)
            self.head = new_node
            self.tail = new_node
        elif index == 0:             #----------> O(1)
            new_node.next = self.head
            self.head = new_node
        else:
            temp_node = self.head   #----------> O(1)
            for _ in range(index-1):  #----------> O(n)
                temp_node = temp_node.next    #----------> O(1)
            new_node.next = temp_node.next    #----------> O(1)
            temp_node.next = new_node       #----------> O(1)
            # Update the tail if the new node is added at the end
            if new_node.next is None:
                self.tail = new_node 
        self.length += 1  #----------> O(1)
        return True  #----------> O(1)
       

    

    def traverse(self):
        current = self.head #----------> O(1)
        while current: #we can also use (while cureent is not none) #----------> O(n)
            print(current.value) #----------> O(1)
            current = current.next #----------> O(1)

#Returning searched element as  true and false
    # def search(self, taget):
    #     current = self.head
    #     while current:
    #         if current.value == taget:
    #             return True
    #         current = current.next
    #     return False

#Returning Index of searched element #TIme O(n) space O(1)
    def search(self, taget):
        current = self.head #----------> O(1)
        index = 0  #----------> O(1)
        while current: #----------> O(N)
            if current.value == taget: #----------> O(1)
                return f'the index of {taget } is {index}'
            current = current.next #----------> O(1)
            index += 1 #----------> O(1)
        return -1
    
#Time O(n) Space O(1)
    def get(self, index):
        if index == -1:    #----------> O(1)
            return self.tail
        if index < -1 or index >= self.length:   #----------> O(1)
            return None
        current = self.head  #----------> O(1)
        for _ in range(index):  #----------> O(n)
            current = current.next #----------> O(1)
        return current
#Time O(n) space O(1)
    def set_value(self, index, value):
        temp = self.get(index) #----------> O(N)
        if temp:
            temp.value = value #----------> O(1)
            return True
        return False

#Time O(1) space O(1)    
    def pop_first(self): #pops first element
        popped_node = self.head  #----------> O(1)
        if self.length <= 1:  #----------> O(1)  #this if mehtod returns none if self.length == 1 or self.length == 0 to prevent from having errors the linked list thats not contain any elementes
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next #----------> O(1)
            # popped_node.next = None #----------> O(1)
        self.length -= 1 #----------> O(1)
        return popped_node #----------> O(1)
  
#Time O(n) space O(1)     
    def pop(self): #pops last element
        if self.length == 0: #----------> O(1)
            return None
        popped_node = self.tail  #----------> O(1)
        if self.length == 1:  #----------> O(1)
            self.head = self.tail = None #----------> O(1)
        else:
            temp =  self.head   #----------> O(1)
            while temp.next is not self.tail:  #----------> O(n)
                temp = temp.next
            self.tail = temp  #----------> O(1)
            temp.next = None #----------> O(1)
        self.length -= 1

#Time O(n) space O(1)  
    def remove(self, index):
        if index >= self.length or index < -1: #----------> O(1)
            return None
        if index == 0: #if index is 0 it calls pop_first() to remove the first element 
           return self.pop_first()  #----------> O(1)
        if index == self.length-1 or index == -1: #if index ==1 it removes last element if less than -1 first if will return none
           return self.pop() #----------> O(n) #It remove last element because in below code if we remove the last element but tail still points to it so pop method will remove element and assign tail to previous index
        prev_node = self.get(index-1)  #----------> O(n)
        popped_node = prev_node.next   #----------> O(1)
        prev_node.next = popped_node.next   #----------> O(1)
        popped_node.next = None   #----------> O(1)
        self.length -= 1
        return popped_node

#Time O(1) space O(1)     
    def delete_all(self):
        # self.__init__() #we can use instead of writing code
        self.head = None
        self.tail = None
        self.length = 0

new_linked_list = LinkedList()

# new_linked_list.insert(-1,6)
# new_linked_list.append(10)
# new_linked_list.append(11)
# new_linked_list.append(12)
# new_linked_list.append(15)
new_linked_list.prepend(9)      
new_linked_list.insert(4,13)
new_linked_list.insert(5,14)
new_linked_list.insert(0,8)
new_linked_list.insert(0,7)
new_linked_list.insert(9,16)
print(new_linked_list)
# new_linked_list.traverse()
# print(new_linked_list.search(9))
# print(new_linked_list.search(16))
# print(new_linked_list.search(17))
# print(new_linked_list.get(3))
# print(new_linked_list.get(-1))
# print(new_linked_list.get(20))
# print(new_linked_list.set_value(2,50))
# print(new_linked_list.tail)
# print(new_linked_list.pop_first())
# print(new_linked_list.pop_first())
# print(new_linked_list.pop())
# print(new_linked_list.remove(2))
# print(new_linked_list.remove(0))
# print(new_linked_list.remove(-1))
# # print(new_linked_list.delete_all())
# print(new_linked_list)



