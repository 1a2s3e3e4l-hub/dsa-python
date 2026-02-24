from typing import TypeVar, Generic
T = TypeVar('T')
class DoublyNode (Generic[T]):
    def __init__(self, data :T) :
        self.data  = data
        self.next : DoublyNode[T] = None
        self.prev : DoublyNode[T] = None

class DoublyLinkedList (Generic[T]):
    def __init__(self):
        self.head : DoublyNode[T] = None
        self.tail : DoublyNode[T] = None
        self.size :int = 0

    def __len__(self) -> int:
        return self.size

    def insert_at_head(self,data:T) ->None:
        new_node = DoublyNode(data)
        new_node.data = data
        if self.size == 0:
            self.head=self.tail = new_node
            new_node.next=new_node.prev=None
        else:
            new_node.next = self.head
            new_node.prev = None
            self.head.prev = new_node
            self.head= new_node
        self.size +=1