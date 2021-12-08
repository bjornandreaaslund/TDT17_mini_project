import os

path = "05_yolo/obj_train_data"
for filename in os.listdir(path):
    new_name = filename[0:6] + "5" + filename[7:]
    os.rename(path+ "/"+filename, path+ "/"+new_name)
