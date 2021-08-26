from gtts import gTTS
#import os
from playsound2 import playsound
import speech_recognition as s_r
import os, random
#from pynput.keyboard import Key, Listener

language = 'en-us'
# print(s_r.__version__) # just to print the version not required
print("INITIALIZING MAYA...\nPOWERED BY RUINTEL IN ASSOCIATION WITH GOOGLE")
r = s_r.Recognizer()
my_mic = s_r.Microphone(device_index=1)  # my device index is 1, you have to put your device index
try:
    while (1):
        with my_mic as source:
            playsound('./maya_recordings/listen.wav')
            print("Listening!!!")
            audio = r.listen(source)  # take voice input from the microphone
        try:
            voice = (r.recognize_google(audio))  # to print voice into text
        except s_r.UnknownValueError:
            voice = ""
        print('Rubin:' + voice)
        if "hey Maiya" in voice or "hi" in voice:
            file = open("./maya_drafts/greeting1.txt", "r").read().replace("\n", " ")
            speech = gTTS(text=str(file), lang=language, slow=False)
            speech.save("./maya_recordings/voice.mp3")
            print('Maya:' + file)
            playsound('./maya_recordings/voice.mp3')
        elif voice == "when is my birthday":
            file = open("./maya_drafts/mybirthdate.txt", "r").read().replace("\n", " ")
            speech = gTTS(text=str(file), lang=language, slow=False)
            speech.save("./maya_recordings/voice.mp3")
            print('Maya:' + file)
            playsound('./maya_recordings/voice.mp3')
        elif voice == "hey Google":
            file = open("./maya_drafts/heygoogle.txt", "r").read().replace("\n", " ")
            speech = gTTS(text=str(file), lang=language, slow=False)
            speech.save("./maya_recordings/voice.mp3")
            print('Maya:' + file)
            playsound('./maya_recordings/voice.mp3')
        elif "bye Maya" in voice or "bye" in voice:
            file = open("./maya_drafts/exit.txt", "r").read().replace("\n", " ")
            speech = gTTS(text=str(file), lang=language, slow=False)
            speech.save("./maya_recordings/voice.mp3")
            print('Maya:' + file)
            playsound('./maya_recordings/voice.mp3')
            playsound('./maya_recordings/logout.wav')
            exit()
        elif voice == "":
            file = open("./maya_drafts/regret1.txt", "r").read().replace("\n", " ")
            speech = gTTS(text=str(file), lang=language, slow=False)
            speech.save("./maya_recordings/voice.mp3")
            print('Maya:' + file)
            playsound('./maya_recordings/voice.mp3')
        elif "who created you" in voice or "who is your father" in voice:
            speech_text = "Rubin is my father, and everyone at RuIntel is my family. Wait! you are also in our family now."
            speech = gTTS(text=speech_text, lang=language, slow=False)
            speech.save("./maya_recordings/voice.mp3")
            print('Maya:' + speech_text)
            playsound('./maya_recordings/voice.mp3')
        elif "play music" in voice or "music" in voice or "play song" in voice:
            file = open("./maya_drafts/music.txt", "r").read().replace("\n", " ")
            speech = gTTS(text=str(file), lang=language, slow=False)
            speech.save("./maya_recordings/voice.mp3")
            print('Maya:' + file)
            basedir = "maya_music"
            playsound('./maya_recordings/voice.mp3')
            music_count = 1
            while 1:
                try:
                    random_file = random.choice([x for x in os.listdir(basedir) if os.path.isfile(os.path.join(basedir, x))])
                    if music_count > 1:
                        print('Maya:Wanna play another song?')
                        playsound('./maya_recordings/wanna_play_again.mp3')
                        with my_mic as source:
                            print("Listening!!!")
                            playsound('./maya_recordings/listen.wav')

                            audio = r.listen(source)  # take voice input from the microphone
                        try:
                            voice = (r.recognize_google(audio))  # to print voice into text
                        except Exception:
                            file = open("./maya_drafts/regret1.txt", "r").read().replace("\n", " ")
                            speech = gTTS(text=str(file), lang=language, slow=False)
                            speech.save("./maya_recordings/voice.mp3")
                            print('Maya:' + file)
                            playsound('./maya_recordings/voice.mp3')
                        print('Rubin:' + voice)
                        if 'no' in voice:
                            playsound('./maya_recordings/sign_out_maya.mp3')
                            exit()
                    if random_file[-3:] == "wav" or random_file[-3:] == "mp3":
                        print(random_file)
                        playsound('./maya_music/' + random_file)
                        music_count += 1
                except FileNotFoundError:
                    playsound('./maya_recordings/music_not_found.mp3')
                    exit()



        else:
            file = open("./maya_drafts/development.txt", "r").read().replace("\n", " ")
            speech = gTTS(text=str(file), lang=language, slow=False)
            speech.save("./maya_recordings/voice.mp3")
            print('Maya:' + file)
            playsound('./maya_recordings/voice.mp3')
except s_r.RequestError:
    print("\n\n\nNETWORK CONNECTION UNAVALILABLE!\n\n")
    playsound('./maya_recordings/networkerror.wav')
