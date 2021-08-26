print("\n\nINITIALIZING FEATURE EXTRACTION...\n\n")
import numpy as np
import librosa
# import librosa.display
from tqdm import tqdm

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

try:
    if os.path.exists("chords_time_series_dataset.csv"):
        os.remove("chords_time_series_dataset.csv")
    if os.path.exists("chords_dataset_feature.csv"):
        os.remove("chords_dataset_feature.csv")
    for folder in tqdm(os.listdir("Maya_Dataset2/"), ncols=100, desc="Exracting Features"):

        if folder == ".DS_Store":
            continue
        for filename in os.listdir("Maya_Dataset2/" + folder):

            if filename[-3:] != "wav":
                print(
                    "WARNING!\nFile extension Missmatch!(" + filename + ")\n Files with other than .wav extension cannot be processed!\n The above mentioned file will be skipped!.\n\n\n")
                continue
            file_count = file_count + 1
            y, sr = librosa.load("Maya_Dataset2/" + folder + "/" +
                                 filename, duration=DURATION, sr=SR, mono=True)
            arr = list(y)
            arr.insert(0, filename)
            arr.insert(1, folder)

            file_time_series = open('chords_time_series_dataset.csv', 'a', newline='')

            with file_time_series:
                writer = csv.writer(file_time_series)
                writer.writerow(arr)

            g = folder

            chroma_stft = librosa.feature.chroma_stft(y=y, sr=sr)
            rmse = librosa.feature.rms(y=y)
            spec_cent = librosa.feature.spectral_centroid(y=y, sr=sr)
            spec_bw = librosa.feature.spectral_bandwidth(y=y, sr=sr)
            rolloff = librosa.feature.spectral_rolloff(y=y, sr=sr)
            zcr = librosa.feature.zero_crossing_rate(y)
            mfcc = librosa.feature.mfcc(y=y, sr=sr)
            to_append = f'{filename} {np.mean(chroma_stft)} {np.mean(rmse)} {np.mean(spec_cent)} {np.mean(spec_bw)} {np.mean(rolloff)} {np.mean(zcr)}'
            for e in mfcc:
                to_append += f' {np.mean(e)}'
            to_append += f' {g}'

            file = open('chords_dataset_feature.csv', 'a', newline='')

            with file:
                writer2 = csv.writer(file)
                writer2.writerow(to_append.split())
    time = int((time.time() - start_time))
    print("FEATURE EXTRACTION COMPLETED SUCCESSFULLY\n\n " + str(file_count) + " items processed in %s Seconds" % time)

except Exception:
    print(
        "Dataset Not Found!\n Either the dataset is deleted or Renamed or moved to the new location!\n\n\n FEATURE EXTRACTION FAILED!!!")
