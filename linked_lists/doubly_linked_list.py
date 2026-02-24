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


