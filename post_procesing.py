"""
Image post-processing
Only works on Windows, to work on Linux change the \\ to /
Must be placed in the photos directory
"""
from pathlib import Path
from PIL import Image
import os

dir_path = Path(__file__).parent.resolve()

def VegetationHealth(image):
    
    
    im = Image.open(image)
    n = 0
    ndvi = 0
    pixels = im.getdata()
    black_thresh = 20;
    white_thresh = 400
    blue_thresh = 212

    nondvi = 0
    lowndvi = 0
    mediumndvi = 0
    highndvi = 0

    for pixel in pixels:
        
       s=pixel[0]+pixel[1]+pixel[2] 
       # nblue = 0
       nblack = 0
       # nwhite = 0
       if s < black_thresh: # check only for black pixels on the edges
            nblack = 1
       
       """ cloud and water checks were left out
       ok=0
       if pixel[0]-pixel[1]<=15 and pixel[0]-pixel[1]>=-15:
           ok+=1
       if pixel[0]-pixel[2]<=15 and pixel[0]-pixel[2]>=-15:
           ok+=1
       if pixel[1]-pixel[2]<=15 and pixel[1]-pixel[2]>=-15:
           ok+=1
       s=pixel[0]+pixel[1]+pixel[2]
       if s >= white_thresh:
           ok+=2
       if ok>=4:
           nwhite=1
    
       ok=0
       if pixel[1]-pixel[0]>=12:
           ok+=1
       if pixel[2]-pixel[0]>=30:
           ok+=1
       if pixel[2]-pixel[1]>=12:
           ok+=1
       s=pixel[0]+pixel[1]+pixel[2]
       if s >= blue_thresh:
           ok+=2
       if ok>=4:
           nblue+=1
       """
           
       if nblack==0:
            
            n+=1 #add valid pixel
            
            #ndvi calculus
            blue = pixel[2]
            red = pixel[0]
            
            s=red+blue
            if s==0:
                s=0.001
            ndvindex=(red-blue)/s
            
            #check type of vegetation
            if ndvindex <= 0:
                nondvi += 1
            elif (ndvindex > 0) and (ndvindex < 0.1):
                lowndvi += 1
            elif (ndvindex >= 0.1) and (ndvindex < 0.2):
                mediumndvi += 1
            elif (ndvindex >= 0.2):
                highndvi += 1
                
    print("rocks clouds and other: ", nondvi/(n)*100,"%")
    print("low vegetation: ", lowndvi/(n)*100,"%")
    print("medium vegetation: ", mediumndvi/(n)*100,"%")
    print("rich vegetation: ", highndvi/(n)*100,"%")


image_numbers = [2,3,10,11,12,13,14]

for i in image_numbers:
    j=i
    print("Image number ",j)
    image_file = f"{dir_path}\\photo_{j:03d}.jpg"
    VegetationHealth(image_file)
    print()
