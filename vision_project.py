import cv2
import numpy as np

# Initial Gaussian blur sigma value
#This variable controls the amount of blur applied using the Gaussian filter.
sigma = 1.0

# Initialize webcam
#opens the default webcam
cap = cv2.VideoCapture(0)

# Default mode
#This stores the current mode (original)
mode = 'o'
#This function blurs an image with a Gaussian filter.
#ksize is calculated from sigma (it must be an odd number)
def apply_gaussian_blur(frame, sigma):
    ksize = int(2 * np.ceil(3 * sigma) + 1)  # Kernel size depends on sigma
    return cv2.GaussianBlur(frame, (ksize, ksize), sigma)
#This keeps running until you press 'q'.
while True:
    
#ret is True if a frame is captured.
#frame is the actual image from the webcam.
#If ret is False, the camera isn't working or is disconnected.
    ret, frame = cap.read()
    if not ret:
        break

    # Convert to grayscale
    #Converts the frame to grayscale. Edge detection usually works better in one channel.
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply Gaussian blur
    #Apply Gaussian blur to remove noise. All edge detection uses this blurred image.
    blurred = apply_gaussian_blur(gray, sigma)

    if mode == 'o':
        output = frame
    elif mode == 'x':
        #horizontal sobel
        grad_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
        output = cv2.convertScaleAbs(grad_x)
    elif mode == 'y':
        #vertical sobel
        grad_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
        output = cv2.convertScaleAbs(grad_y)
    elif mode == 'm':
        grad_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
        grad_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
        magnitude = cv2.magnitude(grad_x, grad_y)
        output = cv2.convertScaleAbs(magnitude)
    elif mode == 's':
        grad_x = cv2.Sobel(blurred, cv2.CV_64F, 1, 0, ksize=3)
        grad_y = cv2.Sobel(blurred, cv2.CV_64F, 0, 1, ksize=3)
        magnitude = cv2.magnitude(grad_x, grad_y)
        _, output = cv2.threshold(magnitude, 100, 255, cv2.THRESH_BINARY)
        output = np.uint8(output)
    elif mode == 'l':
        log = cv2.Laplacian(blurred, cv2.CV_64F)
        output = cv2.convertScaleAbs(log)
    else:
        output = frame

    cv2.imshow("Edge Detection", output)
    #Waits 1ms for a key press.
    #& 0xFF ensures compatibility across systems.
    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('o'):
        mode = 'o'
    elif key == ord('x'):
        mode = 'x'
    elif key == ord('y'):
        mode = 'y'
    elif key == ord('m'):
        mode = 'm'
    elif key == ord('s'):
        mode = 's'
    elif key == ord('l'):
        mode = 'l'
    elif key == ord('+'):
        sigma = min(sigma + 0.2, 10.0)
        print(f"Sigma increased to {sigma:.2f}")
    elif key == ord('-'):
        sigma = max(sigma - 0.2, 0.1)
        print(f"Sigma decreased to {sigma:.2f}")
#cap.release() closes the webcam.
#destroyAllWindows() closes all OpenCV windows.
cap.release()
cv2.destroyAllWindows()
