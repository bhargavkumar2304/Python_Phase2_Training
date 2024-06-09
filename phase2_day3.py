#linkedlist

# Singly linked list node
"""
class Node:
	def __init__(self, x):
		self.data = x
		self.next = None

# A linked list class
class LinkedList:
    def __init__(self, lst=None):
        self.head = None
        self.tail = None
        if lst:
            temp = lst.head
            while temp:
                new_node = Node(temp.data)
                if not self.head:
                    self.head = new_node
                    self.tail = new_node
                else:
                    self.tail.next = new_node
                    self.tail = new_node
                    temp = temp.next

    def insert(self, x):
        temp = Node(x)

        if not self.head:
            self.head = temp
            return
        else:
            temp.next = self.head
            self.head=temp
            
    def print(self):
        if not self.head:
            print("List is empty")
            return
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()
        
    def size(self):
        current=self.head
        c=0
        while current!=None:
            c+=1
            current=current.next
        return c
            
    def find(self,x):
        current=self.head
        while current!=None:
            if current.data==x:
                return True
            current=current.next
        return False

    def position(self,x):
        current=self.head
        c=0
        while current!=None:
            if current.data==x:
                return c
            c+=1
            current=current.next
        return "Not Found"

    def Maximum(self):
        a=self.head
        b=self.head.next
        m=0
        while b!=None:
            if a.data > b.data and a.data > m :
                m=a.data
            elif a.data < b.data and b.data >m:
                m=b.data
            else:
                m=m
            a=a.next
            b=b.next
        return m

    def insert_at_a_position(self,data,pos):
        new=Node(data)
        temp=self.head
        index=0
        if pos==index:
            self.insert(data)
        else:
            while(temp!=None and index+1!=pos):
                index+=1
                temp=temp.next
            if temp!=None:
                new.next=temp.next
                temp.next=new
            else:
                print("Index not Found")

    def remove_at_begining(self):
        self.head=self.head.next

    def remove_at_ending(self):
        if self.head==None:
            return
        temp=self.head
        while temp.next.next:
            temp=temp.next

        temp.next=None

    def remove_at_an_index(self,index):
        if self.head==None:
            return
        
        temp=self.head
        pos=0
        if pos==index:
            self.head=self.head.next
        else:
            while(temp!=None and pos+1!=index):
                pos+=1
                temp=temp.next

            if temp!=None:
                temp.next=temp.next.next

            else :
                print("Index not Found")

    def mid(self):
        if self.head==None:
            return
        a=self.head
        b=self.head
        pos=0
        while b is not None:
            a=a.next
            b=b.next.next
            pos+=1
            
        return pos

    def reverse(self):
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        
        return prev
        
# Driver code
if __name__ == '__main__':
    # Creating object l1 of linked list
    l1 = LinkedList()
    l1.insert(1)
    l1.insert(9)
    l1.insert(5)
    l1.insert(7)
    print("Linked list l1 are: ", end="")
    l1.print()

    # Copying l1 into l2
    l2 = LinkedList(l1)
    print("Linked list l2 are: ", end="")
    l2.print()

    #finding size
    print("size of Linked list l1: ",l1.size())
    print("size of Linked list l2: ",l2.size())

    #searching element
    print(l1.find(5))
    print(l2.find(6))

    #finding maximum element
    print("maximum value of l1 : ",l1.Maximum())
    print("maximum value of l2 : ",l2.Maximum())

    #position of element
    print("index of 9 in l1:",l1.position(9))
    print("index of 7 in l2:",l2.position(7))
    print("index of 6 in l1:",l1.position(6))

    #insert at any position
    l1.insert_at_a_position(6,3)
    print("Linked list l1 are: ", end="")
    l1.print()
    l2.insert_at_a_position(6,3)
    print("Linked list l2 are: ", end="")
    l2.print()

    #deletion of node at begining
    l1.remove_at_begining()
    print("Linked list l1 are: ", end="")
    l1.print()
    l2.remove_at_begining()
    print("Linked list l2 are: ", end="")
    l2.print()

    #deletion of node at ending
    l1.remove_at_ending()
    print("Linked list l1 are: ", end="")
    l1.print()
    l2.remove_at_ending()
    print("Linked list l2 are: ", end="")
    l2.print()
    
    #deletion of node at an index
    l1.remove_at_an_index(2)
    print("Linked list l1 are: ", end="")
    l1.print()
    l2.remove_at_an_index(3)
    print("Linked list l2 are: ", end="")
    l2.print()

    #mid of linked list
    print("Mid of linked list l1 :",l1.mid())

    #reverse a linked list
    l1.print()
    reversed_head=l1.reverse()
    print("linked list l1 after reversing :",end=" ")
    while reversed_head:
        print(reversed_head.data,end=" ")
        reversed_head=reversed_head.next
"""

#Doubly Linked List

class DoublyLinkedList:
    def __init__(self,x):
        self.data=x
        self.next=None
        self.prev=None

    def insert(self,old_node,x):
        new_node=DoublyLinkedList(x)
        new_node.next=old_node.next
        new_node.prev=old_node
        if old_node.next:
            old_node.next.prev=new_node
        old_node.next=new_node
        
        
