import time
import os
import sys
import Helper
import logging
from Manager import Manager

def main():
    """This program proposes a simple way to detect and track multiple objects using OpenCV.
    After checking routes, it loads the video indicated by parameter and in the first frame it initializes the objects to
    follow also given by parameter, and then iterates for each frame of the video, updating the position of the trackers.
    Once the trackers are updated, the current position is obtained, the rectangles are drawn and the frame is stored in the
    output video.
    Terminates when it cannot receive a frame, releasing the allocated resources"""

    # Init Logger
    path = os.getcwd()
    logging.basicConfig(filename=os.path.realpath(path + '/output_data/' + str(time.time_ns()) + ".log"),
                        filemode='a',
                        format='%(asctime)s %(levelname)s: %(message)s',
                        datefmt='%H:%M:%S',
                        level=logging.DEBUG)
    logging.getLogger().addHandler(logging.StreamHandler())

    # Load Args
    args = Helper.load_args()
    # Check args
    if len(args) < 3:
        logging.error("Sorry, 'VIDEO_NAME, JSON_NAME & TRACKER_NAME' parameters was expected")
        return

    # Check folders
    logging.info("Checking folders...")
    if not (Helper.check_folders(path)):
        logging.error("Sorry, input_data was not found")
        return

    # Define paths
    input_video = os.path.realpath(path + '/input_data/' + sys.argv[1])
    output_video = os.path.realpath(path + '/output_data/' + str(time.time_ns()) + ".mkv")
    if not os.path.exists(input_video):
        logging.error("Sorry, ", sys.argv[1], " was not found in input_data folder")
        return


    # Run detection
    Manager.run(path, input_video, output_video, sys.argv[2], sys.argv[3])


if __name__ == '__main__':
    main()
