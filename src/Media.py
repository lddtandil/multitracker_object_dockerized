from cv2 import cv2


#######################################################################################################################
class MediaInput:
    """This class encapsulates methods related to reading a video file"""
    def __init__(self, input_video):
        self.vs = cv2.VideoCapture(input_video)

    def get_width(self):
        return int(self.vs.get(3))

    def get_height(self):
        return int(self.vs.get(4))

    def get_fps(self):
        return self.vs.get(cv2.CAP_PROP_FPS)

    def read(self):
        return self.vs.read()

    def release(self):
        self.vs.release()


#######################################################################################################################
class MediaOutput:
    """This class encapsulates methods related to writing a video file"""
    def __init__(self, video_fps, frame_width, frame_height):
        self.fourcc = cv2.VideoWriter_fourcc('M', 'J', 'P', 'G')  # Define the codec and create VideoWriter object
        self.frame_width = frame_width
        self.frame_height = frame_height
        self.video_fps = video_fps

    def start_save(self, output_path):
        self.out = cv2.VideoWriter(output_path, self.fourcc, self.video_fps,
                                   (self.frame_width, self.frame_height))

    def update(self, frame):
        # Save frame with rectangles
        self.out.write(frame)

    def release(self):
        self.out.release()
