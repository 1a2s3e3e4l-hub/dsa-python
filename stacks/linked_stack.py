from typing import TypeVar, Generic, List
T = TypeVar('T')
class Node(Generic[T]):
    def __init__(self, data:T):
        self.data = data
        self.next = None

class LinkedStack (Generic[T]):
    def __init__(self) -> None:
        self.top = None
        self.count : int = 0
        


