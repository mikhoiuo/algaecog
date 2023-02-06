import cv2
import csv
import os

path = 'unprocessed'

for filename in os.listdir(path):
    img = cv2.imread(os.path.join(path, filename))
    cv2.imshow('Algae Count', img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    num_algae = input("How many algae are in this image? ")

    with open('algae_data.csv', 'a', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([os.path.join(path, filename), num_algae])