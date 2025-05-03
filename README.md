🖥️ Real-Time Edge Detection with OpenCV:
----------------------------------------
A real-time Python application that captures live video from your webcam and applies various edge detection techniques using OpenCV. It provides interactive controls to switch between edge detection modes and adjust the amount of Gaussian blur applied.

📸 Features
📷 Live webcam feed with real-time video processing.

🧠 Interactive edge detection modes:
-------------------------------------

o – Original (no processing)

x – Sobel (X-direction)

y – Sobel (Y-direction)

m – Sobel Magnitude (combined X and Y)

s – Sobel + Threshold (binary edges)

l – Laplacian of Gaussian (LoG)

🔧 Real-time Gaussian blur control with + and - keys.

⚙️ Requirements:
-----------------
Python 3.x

OpenCV

NumPy

📦 Install dependencies:
------------------------
bash
Copy
Edit
pip install opencv-python numpy

🚀 How to Run:
---------------
Save the script as edge_detection.py, then run:
bash
Copy
Edit
python edge_detection.py
Ensure your webcam is connected and accessible.

🎮 Controls
Key	Action:
------------
o	Show original video (no filtering)
x	Apply Sobel edge detection (X-axis)
y	Apply Sobel edge detection (Y-axis)
m	Show gradient magnitude (Sobel XY)
s	Thresholded gradient magnitude
l	Apply Laplacian of Gaussian (LoG)
+	Increase Gaussian blur sigma
-	Decrease Gaussian blur sigma
q	Quit application

🧠 How It Works:
-----------------
Webcam Capture: Opens the default webcam and reads each frame.

Preprocessing: Converts frames to grayscale and applies Gaussian blur (tunable).

Edge Detection Modes:
----------------------

Sobel (X/Y): Highlights vertical or horizontal edges.

Magnitude: Combines X and Y gradients to show total edge strength.

Thresholded: Binarizes the magnitude for clearer edge outlines.

Laplacian of Gaussian: Detects edges based on second-order derivatives.

Dynamic Interaction: Users can adjust the blur strength (sigma) and change modes instantly.

Live Display: Updates processed output in a window titled "Edge Detection".

📝 Notes:
----------
The Gaussian sigma value controls the blur:
Higher sigma = smoother image = less noise but weaker edges.

Kernel size for Gaussian blur is automatically calculated from sigma.

All edge detection operations run in real time for seamless interaction.

📄 License:
------------
This project is licensed under the MIT License.
Feel free to use, modify, and distribute!
