import glob  # Uses glob to read file names

# User inputs the absolute directory path where the images are stored
readDir = input('Input image directory path:  ')

# Reads the file names of all the .jpg files in the readDir directory
# Stores all of the these file names and paths in a list called readImg
readImg = glob.glob(readDir + '/*.jpg')

# For each file name stored in readImg, print it to console
for img in readImg:
    print(img)

