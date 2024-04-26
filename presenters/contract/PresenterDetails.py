from abc import ABC, abstractmethod
from capturers.contracts.VideoCapturer import VideoCapturer
from aruco.contracts.ArucoDetector import ArucoDetector

class PresenterDetails(ABC):
    
    @abstractmethod
    def printDetails(self, arucoDetecor: ArucoDetector):
        pass
    
    @abstractmethod
    def showVideo(self, videoCapturer: VideoCapturer): 
        pass
        
    @abstractmethod
    def onCloseClick(self):
        pass
    
    @abstractmethod
    def destroyWindows(self):
        pass
