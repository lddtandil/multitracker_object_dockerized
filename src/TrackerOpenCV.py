from Tracker import Tracker
from cv2 import cv2
import Constants


#######################################################################################################################
class TrackerOpenCV(Tracker):
    """Opencv Tracker implementation"""
    def __init__(self, tracker_name=Constants.KCF):
        Tracker.__init__(self, tracker_name)
        # initialize a dictionary that maps strings to their corresponding
        # OpenCV object tracker implementations
        self.OPENCV_OBJECT_TRACKERS = {
            Constants.CSRT: cv2.TrackerCSRT_create,
            Constants.KCF: cv2.TrackerKCF_create,
            Constants.BOOSTING: cv2.TrackerBoosting_create,
            "mil": cv2.TrackerMIL_create,
            Constants.TLD: cv2.TrackerTLD_create,
            "medianflow": cv2.TrackerMedianFlow_create,
            "mosse": cv2.TrackerMOSSE_create
        }
        self.tracker = self.OPENCV_OBJECT_TRACKERS[tracker_name]()
#######################################################################################################################
