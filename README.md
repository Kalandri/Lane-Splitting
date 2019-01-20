# ![alt text](https://raw.githubusercontent.com/Kalandri/Lane-Splitting/master/pictures/header.jpeg)

# About
Lane splitting is riding a motorcycle between lanes or rows of slow moving or stopped traffic moving in the same direction. The purpose of this project was to create a video recognition service that can detect motorcylists that are lane-splitting near your car. Some of the cars today can already detect when there is another car next to you, but detecting a motorcyclist lane-splitting through traffic is still not that easy. My motivation for this project is the numerous amount of videos on Youtube of motorcycles crashes that happened because the driver of the car didn't see the lane-splitting motorcyclist.

# ![alt_text](https://raw.githubusercontent.com/Kalandri/Lane-Splitting/master/pictures/detection.jpeg)

# Problem
The main problem with image or video recognition is speed. Services like Amazon Rekognition and Google's Vision API are great for offloading the heavy computing of image recognition to another system. However, our cars unfortunately are not always connected to the internet. This is why I searched for an offline solution like ImageAI. I wanted to make a device that didn't take up too much space and was still fast enough to handle image recognition. 

# Future
This project uses the ImageAI library available for Python and currently uses the YOLOv3 model.  In the future, I would like to train my own model for specifically identifying the front of a motorcycle. I also want to come up with a way to calculate the distance of the motorcycle so that I notify the driver of how far away the vehicle is. 
