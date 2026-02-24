from typing import TypeVar, Generic ,List
T = TypeVar ('T')
class ListStack(Generic[T]):
    def __init__(self) -> None:
        self.items: List[T] = []
    
    def size(self) -> int:
        return len(self.items)
    
    def is_empty(self)->bool:
        return len(self.items) == 0
    
    def push(self,item :T) -> None:
        self.items.append (item)

    def pop(self) -> T:
        if self.is_empty():
            raise IndexError("pop from Empty Stack ")
        return self.items.pop()

   
