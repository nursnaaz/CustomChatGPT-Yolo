# YOLO-Real-Time-Object-Detection
# Performance on the COCO Dataset
## We Need only three files
- yolov3.weights
- colo-name
- yolov3.cfg

## Download the pre-trained weight file here Or Just run this
```sh
$ wget https://pjreddie.com/media/files/yolov3.weights
```
## Download the coco-name and colo-name file here Or Just run this
```sh
$ git clone https://github.com/pjreddie/darknet
```
- coco-name location:- darknet/data/coco.names
- yolov3.cfg location:- darknet/cfg/yolov3.cfg

# For Webcam Just run this 
```sh
$ python3 yolo_video.py -i o
```
# If you want to Change confidence and threshold value 
```sh
$ python3 yolo_video.py -i o -c 0.6 -t 0.4
```
-  -c for confidence
-  -t for threshold

# For Video file
```sh
$ python3 yolo_video.py -i video_file_name
```
