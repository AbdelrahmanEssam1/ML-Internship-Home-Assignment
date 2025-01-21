from abc import ABC , abstractmethod

class AbstractComponent(ABC):
    
    @abstractmethod
    def render(self):
        pass
