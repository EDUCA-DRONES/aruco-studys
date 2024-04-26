import cv2
import cv2.aruco as aruco
from capturers.opencv.VideoCapturerOpenCV import VideoCapturerOpenCV as VideoCapturer
from aruco.opencv.ArucoDetectorOpenCV import ArucoDetectorOpenCV as ArucoDetector
from presenters.contract.PresenterDetails import PresenterDetails

class OpenCVPresenter(PresenterDetails):
    def printDetails(self, arucoDetecor: ArucoDetector):
        print("Cantos detectados:", arucoDetecor.corners)
        print("IDs detectados:", arucoDetecor.ids)

    def showVideo(self, videoCapturer: VideoCapturer): 
        cv2.imshow("Marcadores ArUco", videoCapturer.frame)
        return self
    
    def onCloseClick(self):
        return cv2.waitKey(1) & 0xFF == ord('q')
    
    def destroyWindows(self):
        cv2.destroyAllWindows()
        
