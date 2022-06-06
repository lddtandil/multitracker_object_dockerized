import Constants
import Helper
import time
from TrackerManager import TrackerManager
from Media import MediaOutput, MediaInput
import os
import json
import logging


#######################################################################################################################
class Manager:
    @staticmethod
    def run(path: str, input_video: str, output_video: str, json_name: str, tracker_name: str):
        # Load video
        logging.info("Opening video...")
        media_manager_input = MediaInput(input_video)
        media_manager_output = MediaOutput(media_manager_input.get_fps(), media_manager_input.get_width(),
                                           media_manager_input.get_height())
        input_json = os.path.realpath(path + '/input_data/' + json_name)
        if not os.path.exists(input_json):
            logging.error("Sorry, ", json_name, " was not found in input_data folder")
            Helper.print_files_in_folder(path + '/input_data')
            return

        with open(input_json, 'r') as j:
            tracker_manager = TrackerManager(json.loads(j.read()), Constants.OPENCV_TYPE)

        frame_counter = 0
        logging.info("Start to process...")
        start = time.time()
        # Apply detection for each frame
        while True:
            ret, frame = media_manager_input.read()
            frame_counter += 1
            if not ret:
                logging.info("Can't receive frame (stream end?). Exiting ...")
                break

            if frame_counter == 1:
                tracker_manager.init_trackers(tracker_name.lower(), frame)
                media_manager_output.start_save(output_video)
            frame = tracker_manager.update_all(frame)
            media_manager_output.update(frame)

        logging.info("End process...")
        logging.debug("Total time expended: " + str(time.time() - start))
        logging.debug("Frames processed: " + str(frame_counter))

        # Release allocated resources
        media_manager_output.release()
        media_manager_input.release()


#######################################################################################################################