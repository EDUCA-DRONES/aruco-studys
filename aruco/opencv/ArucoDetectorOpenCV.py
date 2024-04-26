import cv2
import cv2.aruco as aruco
from aruco.contracts.ArucoDetector import ArucoDetector

aruco_dict = aruco.getPredefinedDictionary(aruco.DICT_ARUCO_ORIGINAL)
parameters = aruco.DetectorParameters()

class ArucoDetectorOpenCV():
    def __init__(self, aruco_dict, parameters) -> None:
        self.aruco_dict = aruco_dict
        self.parameters = parameters
        self.corners, self.ids = None, None
        
    def detectMarkers(self, img, frame):
        self.corners, self.ids, _ = aruco.detectMarkers(img, self.aruco_dict, parameters=self.parameters)
        self._drawMarkers(frame)
        
    def _drawMarkers(self, frame):
        aruco.drawDetectedMarkers(frame, self.corners, self.ids)
