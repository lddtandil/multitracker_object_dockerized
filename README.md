# Multi-Object Tracking Project with OpenCV, dockerized
### Simple detector & multiobject tracker
***
This program proposes a simple way to detect and track multiple objects using OpenCV.
After checking routes, it loads the video indicated by parameter and in the first frame it initializes the objects to 
follow also given by parameter, and then iterates for each frame of the video, updating the position of the trackers.
Once the trackers are updated, the current position is obtained, the rectangles are drawn and the frame is stored in the
output video. 
Terminates when it cannot receive a frame, releasing the allocated resources

***

[![Watch the video](https://img.youtube.com/vi/uoxC7VEnVZY/maxresdefault.jpg)](https://www.youtube.com/watch?v=uoxC7VEnVZY)

***
### Prerequisities

In order to run this container you'll need docker and docker-compose installed.

* [Windows](https://docs.docker.com/windows/started)
* [OS X](https://docs.docker.com/mac/started/)
* [Linux](https://docs.docker.com/linux/started/)

***

### Usage
* Place your input files in: ./input_data
  * **Video:** For the video, 'input.mkv' was used as the default name. You can change it in docker-compose.yml
  * **JSON:** For the file with the objects to follow, 'initial_conditions.json' was used as the default name. You can change it in docker-compose.yml
  
* The resulting video will be in: ./output_data
  * **Note:** By default the resulting video will have a '.mkv' extension 

* Copy .env-example to .env (replace the values if you need)
```shell
 docker-compose build && docker-compose up
```
After running, you will find the result in the ./output_data folder along with a log file

**NOTE:** if you want you can change input video name, json file name and tracker type in docker-compose.yml file. 

**By default the CSRT tracker is used since time is not a problem**

***

The options for tracking are:
* **KCF (util)**: 

     **Fast and accurate.**
     This tracker works by training a filter with patches containing the object as well as nearby patches that do not. This allows the tracker to search the area around the previous position and exploit the fact that nearby patches are likely to contain the object.
  

    Pros:
      - 1.5–2x faster than CSRT and ~10x faster than TLD
      - Adapts to scale and rotation
      - Trained on a single image patch
      - Aggressive failure reporting
      - Manually adjustable parameters
      - Supports custom feature extractor

    Cons:
      - Does not recover from failures well
      - Does not recover when objects are changed out of view
      - Does not recover from multiple consecutive failures
      - Does not incorporate motion into estimation


* **CSRT**: 

    **More accurate than KCF but slower**
    This tracker works by training a correlation filter with compressed features (HoG and Colornames). The filter is then used to search the area around the last known position of the object in successive frames.
  

    Pros:
      - Slower but more accurate than KCF
      - Robust to unpredictable motion
      - Trained on a single image patch
      - Can recover from failures when the object hasn’t moved much
      - Can tolerate intermittent frame drops
      - Reports unrecoverable failures
      - Adapts to scale, deformation and rotation
      - Manually adjustable parameters

    Cons:
      - Does not recover well from failures due to full occlusion
      - Latches onto surrounding regions when partially occluded resulting in drift
      - Does not recover when objects are changed out of view
      - Does not recover from multiple consecutive failures
      - Does not incorporate motion into estimation


* **TLD**: 

    This tracker works by training a classifier that is used to re-detect the object and correct tracking errors.
  

    Pros:
    - Recovers from from full occlusion
    - Trained on a single image patch
    - Adapts to scale and deformation
    - Searches the entire image on failures making it good for ‘general location’ reporting

    Cons:
    - Very frequent false positives
    - Very unstable scale estimation
    - Does not report failures well
    - Very slow comparatively (60–100ms)

See: [Comparing state of the art...](https://medium.com/teleidoscope/comparing-state-of-the-art-region-of-interest-trackers-906ba420e80d) for the comparison of the algorithms
***
### Testing
The testing process is defined with an end-to-end scenario in which a file located at '/input_data/input.mkv' is processed and should generate the expected output in '/output_data/test_actualtime.mkv'. e.g.: test_1654542380147684028.mkv

Usage:
```shell
 docker-compose -f docker-compose_Testing.yml build && docker-compose -f docker-compose_Testing.yml up
```
***
### LICENSE
 GPT