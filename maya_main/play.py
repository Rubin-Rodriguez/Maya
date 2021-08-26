import os, os.path
from playsound2 import playsound

count = len([name for name in os.listdir('./recordings')])
count = count - 1
file_name = 'maya' + str(count) + '.wav'
playsound('./recordings/' + file_name)
print('playing sound using  playsound')
