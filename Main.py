import cv2
import numpy as np

def preprocess_image(image_path):
    # Load image
    image = cv2.imread(image_path)
    
    # Resize image
    resized = cv2.resize(image, (512, 512))
    
    # Convert to grayscale
    gray = cv2.cvtColor(resized, cv2.COLOR_BGR2GRAY)
    
    # Apply Gaussian Blur for noise reduction
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    
    # Perform edge detection using Canny
    edges = cv2.Canny(blurred, 50, 150)
    
    # Find contours
    contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    
    # Draw contours on the image
    processed_image = resized.copy()
    cv2.drawContours(processed_image, contours, -1, (0, 255, 0), 2)
    
    return processed_image, edges

# Example usage
image_path = "damaged_car.jpg"
processed_image, edge_image = preprocess_image(image_path)

# Display results
cv2.imshow("Processed Image", processed_image)
cv2.imshow("Edges", edge_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
