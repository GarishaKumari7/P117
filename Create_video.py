import os
import cv2
path="Images/"
Images=[]

for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        print(file_name)
               
        Images.append(file_name)
        
print("Images found:", len(Images))
count = len(Images)

if Images:
    frame=cv2.imread(Images[0])
    height,width,channels=frame.shape
    size= (width,height)
    print(size)
    
    video_name="Project.avi"
    fourcc = cv2.VideoWriter_fourcc(*'DIVX')
    fps = 0.8
    Size = size
    out=cv2.VideoWriter('Projecct.avi', cv2.VideoWriter_fourcc(*'DIVX'),0.8,size)

#Create a for loop to add images to a video writer#
for i in range(0,count-1):
    img=cv2.imread(Images[i])
    out.write(img)
print('Done!')
