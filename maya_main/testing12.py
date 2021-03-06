#print("\n\nINITIALIZING FEATURE EXTRACTION...\n\n")
import numpy as np
import librosa
# import librosa.display
from tqdm import tqdm
from tkinter import filedialog

# import pandas as pd
import os
import csv
# import sys
import warnings
import time

start_time = time.time()

warnings.filterwarnings("ignore")  # warnings are ignored
SR = 100
DURATION = 4
file_count = 0

filename = filedialog.askopenfilename(initialdir="/",title="Select a file", filetypes = (("Text files","*.*"),("all files","*.*")))

if filename[-3:] != "wav":
    print(
        "WARNING!\nFile extension Missmatch!(" + filename + ")\n Files with other than .wav extension cannot be processed!\n The above mentioned file will be skipped!.\n\n\n")
y, sr = librosa.load(filename, duration=DURATION, sr=SR, mono=True)
arr = list(y)
arr.insert(0, filename)


file_time_series = open('chords_time_series_dataset.csv', 'a', newline='')

with file_time_series:
    writer = csv.writer(file_time_series)
    writer.writerow(arr)
#g = folder

chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
rmse = librosa.feature.rms(y=y)
spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
zcr = librosa.feature.zero_crossing_rate(y)
mfcc = librosa.feature.mfcc(y=y, sr=sr)
to_append = f'{np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'
for e in mfcc:
    to_append += f' {np.mean(e)}'
#to_append += f' {g}'

file = open('test13.csv', 'w', newline='')
with file:
    writer2 = csv.writer(file)
    writer2.writerow(to_append.split())



