import cv2
import numpy as np
import os
import csv
from pathlib import Path

def detect_border(image_path):
    img = cv2.imread(image_path)
    if img is None:
        return None
    
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    
    height, width = gray.shape
    
    border_info = {
        'filename': os.path.basename(image_path),
        'top_border': 0,
        'bottom_border': 0,
        'left_border': 0,
        'right_border': 0,
        'sides_with_border': []
    }
    
    for i in range(height):
        row = gray[i, :]
        if np.std(row) < 10:
            border_info['top_border'] = i + 1
        else:
            break
    
    for i in range(height-1, -1, -1):
        row = gray[i, :]
        if np.std(row) < 10:
            border_info['bottom_border'] = height - i
        else:
            break
    
    for j in range(width):
        col = gray[:, j]
        if np.std(col) < 10:
            border_info['left_border'] = j + 1
        else:
            break
    
    for j in range(width-1, -1, -1):
        col = gray[:, j]
        if np.std(col) < 10:
            border_info['right_border'] = width - j
        else:
            break
    
    if border_info['top_border'] > 5:
        border_info['sides_with_border'].append('top')
    if border_info['bottom_border'] > 5:
        border_info['sides_with_border'].append('bottom')
    if border_info['left_border'] > 5:
        border_info['sides_with_border'].append('left')
    if border_info['right_border'] > 5:
        border_info['sides_with_border'].append('right')
    
    return border_info

def process_images(input_dir='input'):
    Path(input_dir).mkdir(exist_ok=True)
    
    image_extensions = ['.jpg', '.jpeg', '.png', '.bmp', '.tiff']
    
    results = []
    
    for filename in os.listdir(input_dir):
        file_path = os.path.join(input_dir, filename)
        
        if any(filename.lower().endswith(ext) for ext in image_extensions):
            print(f"Processing: {filename}")
            
            border_info = detect_border(file_path)
            if border_info:
                results.append(border_info)
                print(f"  - Borders detected: {', '.join(border_info['sides_with_border']) if border_info['sides_with_border'] else 'None'}")
    
    return results

def save_to_csv(results, output_file='border_detection_report.csv'):
    if not results:
        print("No results to save!")
        return
    
    with open(output_file, 'w', newline='') as csvfile:
        fieldnames = ['filename', 'top_border', 'bottom_border', 'left_border', 
                     'right_border', 'sides_with_border']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        
        writer.writeheader()
        for result in results:
            result['sides_with_border'] = '; '.join(result['sides_with_border'])
            writer.writerow(result)
    
    print(f"Results saved to {output_file}")

def main():
    print("Border Detection Script")
    print("=" * 30)
    
    results = process_images()
    
    if results:
        save_to_csv(results)
        
        print(f"\nProcessed {len(results)} images")
        for result in results:
            print(f"{result['filename']}: {result['sides_with_border'] if result['sides_with_border'] else 'No borders'}")
    else:
        print("No images found or processed!")

if __name__ == "__main__":
    main() 