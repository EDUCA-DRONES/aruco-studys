import cv2
import cv2.aruco as aruco
from capturers.contracts.VideoCapturer import VideoCapturer

class ImageCapturerOpenCV(VideoCapturer):
   
    def getFrame(self):
        self.frame = cv2.imread('/home/junior/Documentos/EDUCA DRONES/aruco-study/imgs/test5.jpg')
        self.ret = True
    
    def release(self):
        pass
        
