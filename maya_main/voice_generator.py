from gtts import gTTS
from playsound2 import playsound

language = 'en-uk'
#change filename before executing!

filename = "sign_out_maya"

file = open("./maya_drafts/"+filename+".txt", "r").read().replace("\n", " ")
speech = gTTS(text=str(file), lang=language, slow=False)
speech.save("./maya_recordings/"+filename+".mp3")
print('Maya:' + file)
playsound('./maya_recordings/'+filename+".mp3")