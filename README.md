# Haar_Cascade
OpenCV project
Implementation of Haar Cascade for object detection using python 3.0 and OpenCV in Linux enviornment. 
An android phone with IP Webcam is used to detect objects.

Steps followed to create Haar Cascade:
1. Look for an image repository
   I used http://www.image-net.org/index to build a data base of negative and positive images.
2. Convert split the images to positive images(object images) and negative images(background images).
3. Convert the postive and negative colored images to grayscale image.
4. Decide the size of Haar window that will appear around the object.
5. Run OpenCV in Unix.
   I ran the haar cascade for 8 stages. This can be changed as per required.
6. Connect the camera to using IP address and test.

I tested Haar cascade on sport shoes and was able to implement the code such that it would only detect sport shoes and ignore everything else.
For this repository I have attached my python code and XML files generated after running the OpenCV code.

###_______________________________________________________________________________________________________________###
