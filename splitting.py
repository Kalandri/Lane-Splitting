from imageai.Detection import VideoObjectDetection
import os
import cv2

execution_path = os.getcwd()

camera = cv2.VideoCapture(0)

detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path , "yolo.h5"))
detector.loadModel("fastest")

def forFrame(frame_number, output_array, output_count):
    for object in output_array:
        if object['name'] == 'motorcycle':
            print ('Motorcycle spotted!')

video_path = detector.detectObjectsFromVideo(camera_input=camera,
    output_file_path=os.path.join(execution_path, "camera_detected_video")
    , frames_per_second=10, log_progress=True, minimum_percentage_probability=10, per_frame_function=forFrame)

print(video_path)