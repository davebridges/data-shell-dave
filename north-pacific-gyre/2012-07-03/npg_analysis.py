# take all NENE files ending with AB.txt list out the filename, then run goostats on every file
import os

for file in os.listdir(os.curdir):
 if file.startswith('NENE'): 
  print("Starting the analysis")
  print(file)
  os.system('bash goostats %s stats-%s') %str(file)
  print("Complete the analysis")

