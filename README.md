# Border Detection and Removal
This project provides two Python scripts powered by OpenCV for advanced image border analysis and processing, designed to enhance digital images with precision and efficiency. The Border Detection Script identifies uniform color borders in images from an input directory, measures border sizes on all four sides, and generates a detailed CSV report (border_detection_report.csv) with filenames, border dimensions, and sides with significant borders (>5 pixels). The Border Removal Script detects and crops borders, preserving a 5-pixel content margin, and saves the refined images to an output directory with comprehensive console feedback on removed border metrics. Supporting common image formats (JPG, PNG, BMP, TIFF) and featuring robust directory handling, these scripts offer a seamless solution for automated image optimization.

## Features
Border Detection: Identifies borders by analyzing uniform color regions in grayscale images.
Border Removal: Crops detected borders while maintaining a 5-pixel margin around content.
Comprehensive Reporting: Generates a CSV report for border detection results and detailed console output for both scripts.
Wide Format Support: Processes JPG, JPEG, PNG, BMP, and TIFF images.
Automatic Directory Management: Creates input/output directories as needed.

## Requirements
Python 3.8 or above
OpenCV (cv2) - pip install opencv-python
NumPy - pip install numpy

## Installation

### Clone the repository:
git clone https://github.com/TanishSharma2004/Border_detection_removal


### Navigate to the project directory:
cd ODN_border_assignment


### Install dependencies:
pip install opencv-python numpy



## Usage

Place images in the input directory. 

Run the scripts:

For border detection and CSV report generation:
python border_detection.py

Output: border_detection_report.csv in the project directory.

For border removal and cropped image output:
python border_removal.py

Output: Cropped images in the output directory.



Check console output for processing status and results.


## Project Structure

border_detection.py: Detects borders and generates a CSV report.
border_removal.py: Detects and removes borders, saving cropped images.
input/: Directory for input images (created automatically).
output/: Directory for cropped images (created automatically).
border_detection_report.csv: Output CSV file with border detection results.

## Example Output
### Border Detection
Border Detection Script
Processing: image1.jpg
  - Borders detected: top, left
Processing: image2.png
  - Borders detected: None

Processed 2 images
image1.jpg: top; left
image2.png: No borders

### Border Removal
Border Removal Script
Processing: image1.jpg
  - Removed borders: top, left
  - Border sizes: {'top': 10, 'bottom': 0, 'left': 15, 'right': 0}
  - Saved to: output/image1.jpg

Successfully processed 1 images
Cropped images saved to 'output' folder

## Notes

Ensure images are placed in the input directory before running the scripts.
The scripts use a threshold of 5 pixels to identify significant borders.
Border detection relies on low standard deviation (<10) in grayscale pixel values to identify uniform borders.
