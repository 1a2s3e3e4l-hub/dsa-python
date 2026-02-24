from typing import TypeVar, Generic ,List
T = TypeVar ('T')
class ListStack(Generic[T]):
    def __init__(self) -> None:

        self.items: List[T] = []
    
    def size(self) -> int:
        return len(self.items)
    
    def push(self,item :T) -> None:
        self.items.append(self.items)


   
