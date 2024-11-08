import cv2, os, sys
import numpy as np

def augment_image(image_path, output_folder, rotation=[15,30], flip=True):
    image = cv2.imread(image_path)
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    
    if not os.path.splitext(output_folder):
        os.makedirs(output_folder)
        
    for angle in rotation:
        rotated = cv2.warpAffine(image, cv2.getRotationMatrix2D((image.shape[1] // 2, image.shape[0] // 2), angle, 1), (image.shape[1], image.shape[0]))
        cv2.imwrite(f"{output_folder}/{base_name}_rot_{angle}.jpg", rotated)

    if flip:
        cv2.imwrite(f"{output_folder}/{base_name}_hflip.jpg", cv2.flip(image, 1))  
        cv2.imwrite(f"{output_folder}/{base_name}_vflip.jpg", cv2.flip(image, 0))
        
    resized = cv2.resize(image, (200,200))
    cv2.imwrite(f"{output_folder}/{base_name}_resize.jpg", resized)
    
    corpped = image[0:100, 0:100]
    cv2.imwrite(f"{output_folder}/{base_name}_resize.jpg", corpped)
    
def process_folder(input_folder, output_folder):
    for filename in os.listdir(input_folder):
        if filename.endswith(('.jpg', '.jpeg', '.png')):
               image_path = os.path.join(input_folder, filename)
               augment_image(image_path, output_folder)
            
input_folder = r'C:\Users\SBA\Desktop\googleai'
output_folder = './augmented_images'

process_folder(input_folder, output_folder)