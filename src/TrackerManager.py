import logging
import Constants
from TrackerOpenCV import TrackerOpenCV
from cv2 import cv2

class TrackerManager:
    def __init__(self, input_json, tracker_type=Constants.OPENCV_TYPE, threshold_objects=10):
        self.tracker_type = tracker_type.lower()
        if tracker_type == Constants.OPENCV_TYPE:
            self.trackers = cv2.MultiTracker_create()
        else:
            logging.error("Pls, implement MultiTracker for", tracker_type)
            raise Exception("Pls, implement MultiTracker for", tracker_type)
            return
        self.threshold_objects = threshold_objects
        self.input_json = input_json

    def update_all(self, frame):
        # grab the updated bounding box coordinates (if any) for each
        # object that is being tracked
        (success, boxes) = self.trackers.update(frame)
        # loop over the bounding boxes and draw then on the frame
        for box in boxes:
            (x, y, w, h) = [int(v) for v in box]
            # Draw rectangles
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        return frame

    def init_trackers(self, tracker_name, frame):
        # read json and initiate objects
        cnt = 0
        for element in self.input_json:
            box = (element['coordinates'][0], element['coordinates'][1],
                   element['coordinates'][2], element['coordinates'][3])
            try:
                if cnt + 1 <= self.threshold_objects:
                    if self.tracker_type == Constants.OPENCV_TYPE:
                        # check the most common trackers (kcf, csrt or tld)
                        if tracker_name == Constants.KCF or tracker_name == Constants.CSRT or \
                                tracker_name == Constants.TLD:
                            tracker = TrackerOpenCV(tracker_name)
                            logging.info(tracker_name + " tracker inited!")
                    else:
                        logging.error("Pls, implement Tracker for", self.tracker_type)
                        raise Exception("Pls, implement Tracker for", self.tracker_type)
                        return
                    self.trackers.add(tracker.tracker, frame, box)
                    cnt += 1  # increase the number of tracked objects
            except:
                logging.error("Error while initializing the tracker", self.tracker_type)
                raise Exception("Error while initializing the tracker", self.tracker_type)
                return
