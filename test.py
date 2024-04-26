# teste com img,  comentar o com video
from capturers.opencv.ImageCapturerOpenCV import ImageCapturerOpenCV as VideoCapturer

# teste com video, comentar o com img
# from capturers.opencv.ImageCapturerOpenCV import ImageCapturerOpenCV as VideoCapturer

import cv2
import cv2.aruco as aruco
from aruco.opencv.ArucoDetectorOpenCV import ArucoDetectorOpenCV as ArucoDetector, aruco_dict, parameters
from presenters.opencv.OpenCVPresenter import OpenCVPresenter as PresenterDetails

arucoDetecor = ArucoDetector(aruco_dict=aruco_dict, parameters=parameters)
videoCapturer = VideoCapturer()
presenterDetails = PresenterDetails()

while True:
    videoCapturer.getFrame()
    if not videoCapturer.ret:
        break
    gray = cv2.cvtColor(videoCapturer.frame, cv2.COLOR_BGR2GRAY)
    arucoDetecor.detectMarkers(gray, videoCapturer.frame)
    
    presenterDetails.printDetails(arucoDetecor)
    if presenterDetails.showVideo(videoCapturer).onCloseClick():
        break

videoCapturer.release()
presenterDetails.destroyWindows()