# teste com img,  comentar o com video
# from capturers.opencv.ImageCapturerOpenCV import ImageCapturerOpenCV as VideoCapturer

# teste com video, comentar o com img
from capturers.opencv.VideoCapturerOpenCV import VideoCapturerOpenCV as VideoCapturer

from aruco.opencv.ArucoDetectorOpenCV import ArucoDetectorOpenCV as ArucoDetector, aruco_dict, parameters
from presenters.opencv.OpenCVPresenter import OpenCVPresenter as PresenterDetails

arucoDetecor = ArucoDetector(aruco_dict=aruco_dict, parameters=parameters)
videoCapturer = VideoCapturer()
presenterDetails = PresenterDetails()

while True:
    videoCapturer.getFrame()
    if not videoCapturer.ret:
        break
    gray = videoCapturer.colorToGray()
    arucoDetecor.detectMarkers(gray, videoCapturer.frame)
    
    presenterDetails.printDetails(arucoDetecor)
    if presenterDetails.showVideo(videoCapturer).onCloseClick():
        break

videoCapturer.release()
presenterDetails.destroyWindows()