# TDT17 mini project
Object detection from LiDAR data. The project is a part of the class TDT17 at NTNU. This repository is only to show how we solved this task. 


## Structure

    .
    ├── statistics              # Code to obtain statistics about the object classes
    ├── preprocessing           # Code for preprocessing of video and annotations
    ├── yolov5                  # Reposetory from ultralytics that is adapted to our task
    ├── run.py                  # Code to run the model in Google Colaboratory
    └── README.md

## Data
The data is not uploaded because of privacy issues, and the code can therefore not run as it is. The data was organized with the following folder names.


    ├── datasets           
        ├── train
            ├── images
            └── labels
        └── val
            ├── images
            └── labels
