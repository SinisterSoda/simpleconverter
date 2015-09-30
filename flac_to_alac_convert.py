import os
import subprocess

#this is the default folder it traverses
default = r'C:\Users\Mikey\Music\The_Strokes'
print ("Default Directory is: " + default)
rootdir = input("Input the Directory (Or leave blank for default directory): ")

#this is the directory where ffmpeg is located
ffmpeg = "C:\\Users\\Mikey\\Desktop\\ffmpeg\\bin\\ffmpeg"
i = 0

#will set the folder to default if no folder is input by the user
if rootdir == "":
    rootdir = default

print("Traversing directory: " + rootdir)

#loop that traverses the folder iteratively
outputfile = open(r'C:\Users\Mikey\Desktop\temp.txt','w')    
for subdir, dirs, files in os.walk(rootdir):
    #goes through each file in the subfolder
    print("Going through directory: " + subdir)
    for file in files:
        f = os.path.join(subdir, file)
        #get the base name of the file without extension
        basef = os.path.splitext(f)[0]
        print("Converting: " + f)

        #the ffmpeg command that actually does the converting
        command = ffmpeg + " -i \"" + f + "\" -acodec alac \"" + basef + ".m4a\""
        print("Running command: ")
        print(command)

        #runs the actual command
        subprocess.call(command, shell=True, stdout=outputfile)
        i+=1
        print("Converted file # " + str(i))
    
outputfile.close()

print ("A total of " + str(i) + " files have been converted")
