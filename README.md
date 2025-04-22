Real-Time Edge Detection with OpenCV:
--------------------------------------
This Python script captures video from your webcam and allows real-time edge detection using various filters like
Sobel, Laplacian, and gradient magnitude. It also supports dynamic Gaussian blur adjustment for noise reduction before edge detection.

Features:
-----------
Live webcam feed processing

Switch between different edge detection modes:

Original (o) – Shows the raw webcam feed.

Sobel X (x) – Highlights vertical edges.

Sobel Y (y) – Highlights horizontal edges.

Magnitude (m) – Combines Sobel X and Y to show overall edge strength.

Binary Edges (s) – Thresholds the magnitude for binary edge map.

Laplacian (l) – Detects edges using the Laplacian operator.

Adjustable Gaussian blur using + and - keys.

Requirements:
--------------
Python 3

OpenCV (cv2)

NumPy

Install dependencies with:
---------------------------
bash
Copy
Edit
pip install opencv-python numpy
Usage:
--------
Run the script:

bash
Copy
Edit
python edge_detection_webcam.py
Use the following keys during execution:


Key	Function
o	Original frame
x	Sobel X (vertical edges)
y	Sobel Y (horizontal edges)
m	Gradient magnitude
s	Binary edge map (threshold)
l	Laplacian filter
+	Increase Gaussian blur
-	Decrease Gaussian blur
q	Quit the program
Notes:
-------
Gaussian blur helps to reduce noise before applying edge detection.

You can fine-tune the sigma value using + and - to improve edge clarity.
