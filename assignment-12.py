#Question1:->Print the current day using Datetime module.
from datetime import datetime
print(datetime.today())
print()

#Question2:->Open your browser and play a video using webbrowser module in python.
import webbrowser
print("Motivational video")
webbrowser.open_new_tab("https://www.youtube.com/watch?v=JG9Ii3MyOzw")
print()

#Question3:-> Write a program to rename all the files in a directory and convert them into .jpg file format.
import os,sys
folder = r'C:\Users\HP\Desktop\Module project'
for file in os.listdir(folder):    
    file1 = os.path.join(folder,file)
    if not os.path.isfile(file1):
        continue
    oldbase = os.path.splitext(file)
    newname = file1.replace('.txt', '.jpg')
    output = os.rename(file1, newname)
print()
