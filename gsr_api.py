#!/usr/bin/env python3
# Requires PyAudio and PySpeech.
import os
import speech_recognition as sr
import asr_evaluation
import subprocess
import csv
import pandas as pd
import shutil

# Record Audio
r = sr.Recognizer()
if os.path.exists("C:/Users/Sri/Results"):
    shutil.rmtree("C:/Users/Sri/Results")
    os.mkdir("C:/Users/Sri/Results")
else:
    os.mkdir("C:/Users/Sri/Results")
file1 = open("C:/Users/Sri/Results/prediction.txt","a")

for folder in os.listdir("C:/Users/Sri/test_data"):
    
    for file in os.listdir("C:/Users/Sri/test_data/"+folder):
        if file.endswith(".flac"):
        
            with sr.AudioFile("C:/Users/Sri/test_data/"+ folder +"/"+file) as source:
                audio = r.listen(source)


# Speech recognition using Google Speech Recognition
            try:
                ans=r.recognize_google(audio, language='de-DE')
                base=os.path.basename("C:/Users/Sri/test_data/"+ folder +"/"+file)
                name=os.path.splitext(base)[0]
                file1.write(name+" "+ans+"\n") 
                    
            except sr.UnknownValueError:
                print("Google Speech Recognition could not understand audio")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))
file1.close()
file2 = open("C:/Users/Sri/Results/transcript.txt","w")
for folder in os.listdir("C:/Users/Sri/test_data"):
    for file in os.listdir("C:/Users/Sri/test_data/"+folder):
        if file.endswith(".txt"):
            f = open("C:/Users/Sri/test_data/"+folder+"/"+file, "r")
            lines=f.readlines()
            for line in lines:
                #file2.write(line.split(" ", 1)[1])
                file2.write(line)          
file2.close()
with open("C:/Users/Sri/Results/prediction.txt", "r+") as f:
    lines = f.readlines()
    lines.sort()        
    f.seek(0)
    f.writelines(lines)
with open("C:/Users/Sri/Results/transcript.txt", "r+") as f:
    lines = f.readlines()
    lines.sort()        
    f.seek(0)
    f.writelines(lines)

#Evaluation
subprocess.call("wer -r -a --head-ids C:/Users/Sri/Results/transcript.txt C:/Users/Sri/Results/prediction.txt >> C:/Users/Sri/Results/output.txt ",shell=True)

# opens original file
file3 = open("C:/Users/Sri/Results/output.txt" , "r")
# opens new file
file4 = open("C:/Users/Sri/Results/summary.txt" , "a")
#for each line in old file
lines=file3.readlines()
for line in lines[-4::]:
#write that line to the new file
    file4.write(line)
#close file 1
file3.close()
#close file2
file4.close()
f = open("C:/Users/Sri/Results/output.txt", "r")

lines=f.readlines()
col1=lines[0:-4:5]
col2=lines[1:-4:5]
col3=lines[2:-4:5]
col4=lines[3:-4:5]
col5=lines[4:-4:5]

df= pd.DataFrame({'sentence_no':col3,'accuracy':col4, 'error_rate':col5,  'predication':col2, 'original':col1})
export_csv = df.to_csv (r'C:/Users/Sri/Results/output.csv', index = None, header=True)


    
