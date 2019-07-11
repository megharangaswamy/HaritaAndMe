import asr_evaluation
import subprocess
import csv
import pandas as pd
subprocess.call("wer -r -a neujahr_transcript.txt neujahr_prediction.txt >> output_neujahr.txt ",shell=True)

# opens original file
file1 = open("output_neujahr.txt" , "r")
# opens new file
file2 = open("summary_neujahr.txt" , "w")
#for each line in old file
lines=file1.readlines()
for line in lines[-4::]:
#write that line to the new file
    file2.write(line)
#close file 1
file1.close()
#close file2
file2.close()
f = open("output_neujahr.txt", "r")

lines=f.readlines()
col1=lines[0:-4:5]
col2=lines[1:-4:5]
col3=lines[2:-4:5]
col4=lines[3:-4:5]
col5=lines[4:-4:5]

df= pd.DataFrame({'sentence_no':col3,'accuracy':col4, 'error_rate':col5,  'predication':col2, 'original':col1})
export_csv = df.to_csv (r'neujahr_output.csv', index = None, header=True)
