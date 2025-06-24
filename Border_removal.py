import cv2
import numpy as np
import os
from pathlib import Path

def detect_and_remove_border(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return None, None
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    height, width = gray.shape
    
    top_crop = 0
    bottom_crop = height
    left_crop = 0
    right_crop = width
    
    for i in range(height):
        row = gray[i, :]
        if np.std(row) > 10:
            top_crop = max(0, i - 5)
            break
    
    for i in range(height-1, -1, -1):
        row = gray[i, :]
        if np.std(row) > 10:
            bottom_crop = min(height, i + 5)
            break
    
    for j in range(width):
        col = gray[:, j]
        if np.std(col) > 10:
            left_crop = max(0, j - 5)
            break
    
    for j in range(width-1, -1, -1):
        col = gray[:, j]
        if np.std(col) > 10:
            right_crop = min(width, j + 5)
            break
    
    cropped_img = img[top_crop:bottom_crop, left_crop:right_crop]
    
    border_removed = {
        'top': top_crop,
        'bottom': height - bottom_crop,
        'left': left_crop,
        'right': width - right_crop
    }
    
    return cropped_img, border_removed

def process_and_save_images(input_dir='input', output_dir='output'):
    Path(input_dir).mkdir(exist_ok=True)
    Path(output_dir).mkdir(exist_ok=True)
    
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
    
    processed_count = 0
    
    for filename in os.listdir(input_dir):
        if any(filename.lower().endswith(ext) for ext in image_extensions):
            input_path = os.path.join(input_dir, filename)
            output_path = os.path.join(output_dir, filename)
            
            print(f"Processing: {filename}")
            
            cropped_img, border_info = detect_and_remove_border(input_path)
            
            if cropped_img is not None:
                cv2.imwrite(output_path, cropped_img)
                processed_count += 1
                
                removed_borders = [side for side, size in border_info.items() if size > 5]
                if removed_borders:
                    print(f"  - Removed borders: {', '.join(removed_borders)}")
                    print(f"  - Border sizes: {border_info}")
                else:
                    print(f"  - No significant borders removed")
                    
                print(f"  - Saved to: {output_path}")
            else:
                print(f"  - Error processing {filename}")
    
    return processed_count

def main():
    print("Border Removal Script")
    print("=" * 30)
    
    count = process_and_save_images()
    
    if count > 0:
        print(f"\nSuccessfully processed {count} images")
        print("Cropped images saved to 'output' folder")
    else:
        print("No images found or processed!")

if __name__ == "__main__":
    main()