# SCALE IDENTIFIER MAYA MANTRA

def strings_melody():
    import numpy as np
    import librosa
    from tkinter import filedialog
    import random
    import os
    import csv
    import warnings
    import sounddevice as sd
    from scipy.io.wavfile import write
    import wavio as wv
    from playsound2 import playsound

    warnings.filterwarnings("ignore")  # warnings are ignored

    SR = 100
    DURATION = 4

    # Root Directory for audio clips and drafts
    directory_path = 'D:/Project Maya/Maya/maya_main/'

    # Sampling frequency
    freq = 44100

    # Recording duration
    duration = 4

    try:
        playsound(directory_path + 'maya_recordings/listen.wav')
        print("Listening!!!")

        # Start recorder with the given values
        # of duration and sample frequency
        recording = sd.rec(int(duration * freq),samplerate=freq, channels=2)

        # Record audio for the given number of seconds
        sd.wait()

        # This will convert the NumPy array to an audio
        # file with the given sampling frequency
        write(directory_path + "recordings/recording0.wav", freq, recording)

        # Convert the NumPy array to audio file
        wv.write(directory_path + "recordings/recording1.wav", recording, freq, sampwidth=2)
        filename = directory_path + "recordings/recording1.wav"

        # filename = filedialog.askopenfilename(initialdir="/", title="Select a audio file", filetypes=(("wav files", "*.wav"), ("mp3 files", "*.mp3")))
    except RuntimeError:
        print("RUN TIME ERROR!")
        return "", ""

    y, sr = librosa.load(filename, duration=DURATION, sr=SR, mono=True)
    arr = list(y)
    arr.insert(0, filename)

    file_time_series = open('chords_time_series_dataset.csv', 'a', newline='')

    with file_time_series:
        writer = csv.writer(file_time_series)
        writer.writerow(arr)
    # g = folder

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
    # to_append += f' {g}'

    file = open('chord_test_dataset.csv', 'w', newline='')
    with file:
        writer2 = csv.writer(file)
        writer2.writerow(to_append.split())

    # ----------------KNN--------------
    import pandas as pd
    df = pd.read_csv('maya_dataset/chords_dataset_feature.csv')
    df1 = df.drop(df.columns[0], axis=1)
    print('df', df1)
    df2 = df1.iloc[:, :-1]
    print('df2', df2)
    df2.to_csv('chords_final_dataset.csv', index=False)

    import csv
    import math
    import operator

    def euclideanDistance(instance1, instance2, length):
        distance = 0
        for x in range(length):
            distance += (pow((float(instance1[x]) - float(instance2[x])), 2))
        return math.sqrt(distance)

    def getNeighbors(trainingSet, testInstance, k):
        distances = []
        length = len(testInstance) - 1

        for x in range(len(trainingSet)):
            dist = euclideanDistance(testInstance, trainingSet[x], length)
            distances.append((trainingSet[x], dist))
        distances.sort(key=operator.itemgetter(1))
        neighbors = []
        for x in range(k):
            neighbors.append(distances[x][0])
        return neighbors

    def getResponse(neighbors):
        classVotes = {}
        for x in range(len(neighbors)):
            response = neighbors[x][-1]
            if response in classVotes:
                classVotes[response] += 1
            else:
                classVotes[response] = 1
        sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
        return sortedVotes[0][0]

    def getAccuracy(testSet, predictions):
        predictions = predictions[0]
        correct = 0
        for x in range(len(testSet)):
            if testSet[x] == predictions:
                correct += 1

        return (correct / float(len(testSet))) * 100.0

    trainingSet = []
    testSet = []
    with open('chords_final_dataset.csv', 'r') as csvfile:
        lines = csv.reader(csvfile)
        dataset = list(lines)
        # print(dataset)



        for x in range(len(dataset) - 1):
            for y in range(25):
                dataset[x][y] = float(dataset[x][y])
            trainingSet.append(dataset[x])

    with open('chord_test_dataset.csv', 'r') as csvfile1:
        lines1 = csv.reader(csvfile1)
        # print(lines1)
        dataset1 = list(lines1)
        # print(dataset1)

        for p in range(len(dataset1)):
            for q in range(25):
                dataset[p][q] = float(dataset[p][q])
            testSet.append(dataset1[p])

    print("\ntrainingset:", trainingSet)
    print("\ntestingset:", testSet)
    # print("1:",len(trainingSet))
    # print("2:",len(testSet))

    k = 1

    predictions = []
    for x in range(len(testSet)):
        neighbors = getNeighbors(trainingSet, testSet[x], k)
        response = getResponse(neighbors)
        print("\nNeighbors:", neighbors)
        print('\n\nResponse:', response)

        predictions.append(response)

    testset1 = pd.read_csv('chord_response_dataset.csv')

    testset1 = testset1.iloc[:, 0]

    accuracy = getAccuracy(testset1, predictions)
    print('Accuracy: ' + repr(accuracy) + '%\n\n')

    file = open('chord_response_dataset.csv', 'a', newline='')
    writer3 = csv.writer(file)
    writer3.writerow([response])

    response = response.replace("_", " ")
    import matplotlib.pyplot as plt

    x = [0, 1, 2]
    y = [accuracy, 0, 0]
    plt.title('Accuracy')
    plt.bar(x, y)
    plt.show()
    return response, accuracy
