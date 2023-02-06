import cv2
import csv
import os

# Define the path to the folder containing the images
folder_path = 'unprocessed'

# Loop over all the images in the folder
for filename in os.listdir(folder_path):
    # Load the image using OpenCV
    img = cv2.imread(os.path.join(folder_path, filename))
    cv2.imshow('Algae Count', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    # Ask the user for the number of algae in the image
    num_algae = input("How many algae are in this image? ")

    # Write the data to a CSV file
    with open('algae_data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([os.path.join(folder_path, filename), num_algae])