import unittest
from Manager import Manager
import os
import time
class TestMethods(unittest.TestCase):

    def test_execution(self):
        """The testing process is defined with an end-to-end scenario in which a file located at
        '/input_data/input.mkv' is processed and should generate the expected output in
        /output_data/test_actualtime.mkv'. """
        print("Running test_execution")
        path = os.getcwd()
        # Define paths
        input_video = os.path.realpath(path + '/input_data/input.mkv')
        actual_time = str(time.time_ns())
        output_video = os.path.realpath(path + '/output_data/test_' + actual_time +'.mkv')


        Manager.run(path, input_video, output_video, "initial_conditions.json", "csrt")
        self.assertTrue(os.path.exists(output_video))

if __name__ == '__main__':
    unittest.main()