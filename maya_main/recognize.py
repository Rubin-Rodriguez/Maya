import os, os.path
import speech_recognition as s_r

# print(s_r.__version__) # just to print the version not required
print("INITIALIZING...")
r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1)  # my device index is 1, you have to put your device index
with my_mic as source:
    print("Listening!!!")
    audio = r.listen(source)  # take voice input from the microphone
# print(r.recognize_google(audio)) #to print voice into text
count = len([name for name in os.listdir('./recordings')])
file_name = 'maya' + str(count) + '.wav'
with open('recordings/' + file_name, 'wb') as file:
    wav_data = audio.get_wav_data()
    file.write(wav_data)
