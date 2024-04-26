import cv2
import cv2.aruco as aruco
from capturers.contracts.VideoCapturer import VideoCapturer

class VideoCapturerOpenCV(VideoCapturer):
    def __init__(self) -> None:
        self.cam_id = 0
        self.cap = cv2.VideoCapture(self.cam_id)
        self.ret = None
        self.frame = None
        
    def colorToGray(self):
        return cv2.cvtColor(self.frame, cv2.COLOR_BGR2GRAY)
    
    def getFrame(self):
        self.ret, self.frame = self.cap.read()
    
    def release(self):
        self.cap.release()
        
