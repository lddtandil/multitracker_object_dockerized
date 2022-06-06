import argparse
import os
import logging

#######################################################################################################################
def load_args():
    # construct the argument parser and parse the arguments
    ap = argparse.ArgumentParser(description='Leonardo Dominguez App.')
    ap.add_argument('VIDEO_NAME', type=str,
                    help="")
    ap.add_argument("JSON_NAME", type=str, default="kcf",
                    help="")
    ap.add_argument("TRACKER_NAME", type=str, default="kcf",
                    help="OpenCV object tracker type")
    args = vars(ap.parse_args())
    logging.info("Actual parameters: " + str(args))
    return args


#######################################################################################################################
def print_files_in_folder(path):
    only_files = [''.join(f) for f in os.listdir(path)]
    logging.info("Actual files in {}:".format(path) + str(only_files))


#######################################################################################################################
def check_folders(path):
    # Check whether the specified path exists or not
    out_path = os.path.realpath(path + '/output_data')
    is_exist = os.path.exists(out_path)

    if not is_exist:
        # Create a new directory because it does not exist
        os.makedirs(path + '/output_data')
        logging.info("The new directory {} is created!".format(out_path))

    is_exist = os.path.exists(path + '/input_data')
    if not is_exist:
        # Create a new directory because it does not exist
        os.makedirs(path + '/input_data')
        return False
    else:
        print_files_in_folder(path + '/input_data')
        return True
#######################################################################################################################
