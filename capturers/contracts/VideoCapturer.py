from abc import ABC, abstractmethod

class VideoCapturer(ABC):
    
    @abstractmethod
    def colorToGray(self):
        pass
    
    @abstractmethod
    def getFrame(self):
       pass
    
    @abstractmethod
    def release(self):
        pass
        
