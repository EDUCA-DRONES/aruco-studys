from abc import ABC, abstractmethod

class ArucoDetector():

    @abstractmethod        
    def detectMarkers(self, img, frame):
       pass
       
    @abstractmethod 
    def _drawMarkers(self, frame):
        pass
