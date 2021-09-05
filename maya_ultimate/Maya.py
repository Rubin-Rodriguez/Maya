#MAYA VOICE ASSISTANT
def maya_assist():
    import pygame
    from gtts import gTTS
    from playsound2 import playsound
    import speech_recognition as s_r
    import os
    import random

    # Root Directory for audio clips and drafts
    directory_path = 'D:/Project Maya/Maya/maya_main/'

    # Language for voice response
    language = 'en-us'

    print("INITIALIZING MAYA...\nPOWERED BY RUINTEL IN ASSOCIATION WITH GOOGLE")

    # initialize Pygame Mixer
    pygame.mixer.init()

    r = s_r.Recognizer()
    my_mic = s_r.Microphone(device_index=1)  # my device index is 1
    try:

        with my_mic as source:
            pygame.mixer.music.set_volume(0.1)
            playsound(directory_path+'maya_recordings/listen.wav')
            print("Listening!!!")
            audio = r.listen(source)  # take voice input from the microphone
        try:
            voice = (r.recognize_google(audio))  # to print voice into text
        except s_r.UnknownValueError:
            voice = ""
        print('Rubin:' + voice)

        # Hey Maya
        if "hey Maiya" in voice or "hi" in voice or "hello maya" in voice:
            file = open(directory_path+"maya_drafts/greeting1.txt", "r").read().replace("\n", " ")
            speech = gTTS(text=str(file), lang=language, slow=False)
            speech.save(directory_path+"maya_recordings/voice.mp3")
            print('Maya:' + file)
            playsound(directory_path+'maya_recordings/voice.mp3')

        # When is my Birthday
        elif voice == "when is my birthday":
            file = open(directory_path+"maya_drafts/mybirthdate.txt", "r").read().replace("\n", " ")
            speech = gTTS(text=str(file), lang=language, slow=False)
            speech.save(directory_path+"maya_recordings/voice.mp3")
            print('Maya:' + file)
            playsound(directory_path+'maya_recordings/voice.mp3')

        # Calling Hey Google
        elif voice == "hey Google":
            file = open(directory_path+"maya_drafts/heygoogle.txt", "r").read().replace("\n", " ")
            speech = gTTS(text=str(file), lang=language, slow=False)
            speech.save(directory_path+"maya_recordings/voice.mp3")
            print('Maya:' + file)
            playsound(directory_path+'maya_recordings/voice.mp3')

        # Bye Maya
        elif "bye Maya" in voice or "bye" in voice or "Logout" in voice:
            file = open(directory_path+"maya_drafts/exit.txt", "r").read().replace("\n", " ")
            speech = gTTS(text=str(file), lang=language, slow=False)
            speech.save(directory_path+"maya_recordings/voice.mp3")
            print('Maya:' + file)
            playsound(directory_path+'maya_recordings/voice.mp3')
            playsound(directory_path+'maya_recordings/logout.wav')
            return "Logout"

        # heard nothing
        elif voice == "":
            file = open(directory_path+"maya_drafts/regret1.txt", "r").read().replace("\n", " ")
            speech = gTTS(text=str(file), lang=language, slow=False)
            speech.save(directory_path+"maya_recordings/voice.mp3")
            print('Maya:' + file)
            playsound(directory_path+'maya_recordings/voice.mp3')

        # Who Created You
        elif "who created you" in voice or "who is your father" in voice:
            speech_text = "Rubin is my father, and everyone at RuIntel is my family. Wait! you are also in our family now."
            speech = gTTS(text=speech_text, lang=language, slow=False)
            speech.save(directory_path+"maya_recordings/voice.mp3")
            print('Maya:' + speech_text)
            playsound(directory_path+'maya_recordings/voice.mp3')

        # play music
        elif "play music" in voice or "play another song" in voice:
            file = open(directory_path+"maya_drafts/music.txt", "r").read().replace("\n", " ")
            speech = gTTS(text=str(file), lang=language, slow=False)
            speech.save(directory_path+"maya_recordings/voice.mp3")
            print('Maya:' + file)

            # Base dir for songs
            basedir = directory_path+"maya_music"
            # import maya_ultimate.Kukushka as kuku
            # kuku.play()
            pygame.mixer.music.set_volume(1.0)
            # Music playback starts
            try:
                # selecting random file from maya_music dir
                random_file = random.choice(
                    [x for x in os.listdir(basedir) if os.path.isfile(os.path.join(basedir, x))])

                # plays only .mp3 and .wav files
                if random_file[-3:] == "wav" or random_file[-3:] == "mp3":
                    playsound(directory_path + 'maya_recordings/voice.mp3')
                    print(random_file)
                    song = f'D:/Project Maya/Maya/maya_main/maya_music/{random_file}'
                    pygame.mixer.music.load(song)
                    pygame.mixer.music.play(loops=0)
                    return "Playing "+random_file.replace(".mp3", "")
                    # playsound(directory_path+'maya_music/' + random_file)
            except FileNotFoundError:
                playsound(directory_path+'maya_recordings/music_not_found.mp3')
                exit()

        # stop playback
        elif "top" in voice or "stop the music" in voice:
            speech_text = "Copy That!"
            speech = gTTS(text=speech_text, lang=language, slow=False)
            speech.save(directory_path + "maya_recordings/voice.mp3")
            print('Maya:' + speech_text)
            playsound(directory_path + 'maya_recordings/voice.mp3')
            pygame.mixer.music.stop()
            return "Music Stoped!"
        elif "Strings melody" in voice or "melody" in voice:
            speech_text = "Opening Strings Melody."
            speech = gTTS(text=speech_text, lang=language, slow=False)
            speech.save(directory_path + "maya_recordings/voice.mp3")
            print('Maya:' + speech_text)
            playsound(directory_path + 'maya_recordings/voice.mp3')
            return "Strings_Melody"
        elif "Maya mantra" in voice or "Mantra" in voice:
            speech_text = "Opening Maya Mantra."
            speech = gTTS(text=speech_text, lang=language, slow=False)
            speech.save(directory_path + "maya_recordings/voice.mp3")
            print('Maya:' + speech_text)
            playsound(directory_path + 'maya_recordings/voice.mp3')
            return "Maya_Mantra"
        elif "I need help" in voice:
            speech_text = "Okay, don't worry! I'm always there for you. You can find help in help section."
            speech = gTTS(text=speech_text, lang=language, slow=False)
            speech.save(directory_path + "maya_recordings/voice.mp3")
            print('Maya:' + speech_text)
            playsound(directory_path + 'maya_recordings/voice.mp3')
            return "Help"
        else:
            file = open(directory_path+"maya_drafts/development.txt", "r").read().replace("\n", " ")
            speech = gTTS(text=str(file), lang=language, slow=False)
            speech.save(directory_path+"maya_recordings/voice.mp3")
            print('Maya:' + file)
            playsound(directory_path+'maya_recordings/voice.mp3')

    except s_r.RequestError:
        print("\n\n\nNETWORK CONNECTION UNAVALILABLE!\n\n")
        playsound(directory_path+'maya_recordings/networkerror.wav')
    pygame.mixer.music.set_volume(1.0)
    return("Maya Assistant Closed")

#END OF MAYA VOICE ASSISTANT!