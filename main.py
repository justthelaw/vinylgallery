import numpy as np
import time
import random
import csv
import myConfig
import webscrape

csvFile = myConfig.filename

with open(csvFile) as infile:
    reader = csv.reader(infile) # Create a new reader
    lst = [row for row in reader]

# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])

jsonFile = []

for album in lst:
    # print('album[1]: ', album[1], ' album[2]: ', album[2])
    artURL = webscrape.get_album_art([album[1], album[2]])
    time.sleep(0.7)
    jsonFile.append([album[1], album[2], artURL])


print(jsonFile)