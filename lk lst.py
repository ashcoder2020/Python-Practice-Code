class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Linked_list:
    def __init__(self):
        self.head=None

    def insert(self,data):
        if self.head is None:
            self.head=newnode
        else:
            lastnode=self.head
            while True:
                if lastnode.head is None:
                    lastnode=self.head
                    self.head=self.head.next
                    self.head.next=newnode



newnode=Node()
insert(10)