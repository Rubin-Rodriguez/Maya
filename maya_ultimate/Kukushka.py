#KUKUSHKA MUSIC PLAYER
#VERSION 1.0
import os
from tkinter import *
import pygame
from tkinter import filedialog
from tqdm import tqdm
import time
from mutagen.mp3 import MP3

root = Tk()
root.title('Kukushka Ver 1.0')
root.iconbitmap('D:/Project Maya/Maya/maya_ultimate/icons/kuku.ico')
root.geometry("400x350")
#initialize Pygame Mixer
pygame.mixer.init()

#grab song length time info
def play_time():
    current_time = pygame.mixer.music.get_pos()/1000
    #converted time
    convertd_current_time =time.strftime('%M:%S', time.gmtime(current_time))

    #get currently playing song
    #next_one = song_box.curselection()
    song = song_box.get(ACTIVE)
    song = f'D:/Project Maya/Maya/maya_main/maya_music/{song}.mp3'

    #get song length with mutagen
    song_mut = MP3(song)

    #get song length
    song_length = song_mut.info.length

    # converted time
    convertd_song_length = time.strftime('%M:%S', time.gmtime(song_length))
    status_bar.config(text=f'Time Elapsed: {convertd_current_time} of {convertd_song_length} ')

    #update time
    status_bar.after(1000, play_time)
    root.mainloop()
#add song function
def add_song():
    song = filedialog.askopenfilename(initialdir='D:/Project Maya/Maya/maya_main/maya_music/', title="Choose A Song", filetypes=(("mp3 Files","*.mp3"),))
    song = song.replace("D:/Project Maya/Maya/maya_main/maya_music/", "")
    song = song.replace(".mp3", "")
    #insert into playlist
    song_box.insert(END, song)

#add many songs to playlist
def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='D:/Project Maya/Maya/maya_main/maya_music/', title="Choose A Song",
                                      filetypes=(("mp3 Files", "*.mp3"),))
    #loop thru song list replace directory
    for song in songs:
        song = song.replace("D:/Project Maya/Maya/maya_main/maya_music/", "")
        song = song.replace(".mp3", "")
        # insert into playlist
        song_box.insert(END, song)

#play selected song
def play():
    song = song_box.get(ACTIVE)
    song = f'D:/Project Maya/Maya/maya_main/maya_music/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    #call the play_time function to get time
    play_time()

#stop playing song
def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

    #clear status bar
    status_bar.config(text='')
#play the next song and the playlist
def next_song():

    #get the current song tuple number
    next_one = song_box.curselection()

    #add one to the current song number
    try:
        next_one = next_one[0]+1

        size = song_box.size()
        if next_one == size:
            next_one = next_one - size
        #grab song title from playlist
        song = song_box.get(next_one)
        song = f'D:/Project Maya/Maya/maya_main/maya_music/{song}.mp3'

        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
        #clear active bar in playlist
        song_box.selection_clear(0, END)

        #activate new song bar
        song_box.activate(next_one)
        #set active bar to next
        song_box.selection_set(next_one,last=None)
    except IndexError:
        print("Please makes sure that the selection is active!")

#previous song
def previous_song():
    # get the current song tuple number
    next_one = song_box.curselection()
    # add one to the current song number
    try:
        next_one = next_one[0] - 1

        # grab song title from playlist
        size = song_box.size()
        if next_one  == -1:
            next_one = next_one + size

        song = song_box.get(next_one)
        song = f'D:/Project Maya/Maya/maya_main/maya_music/{song}.mp3'

        pygame.mixer.music.load(song)
        pygame.mixer.music.play(loops=0)
        # clear active bar in playlist
        song_box.selection_clear(0, END)

        # activate new song bar
        song_box.activate(next_one)
        # set active bar to next
        song_box.selection_set(next_one, last=None)
    except IndexError:
        print("Please makes sure that the selection is active!")

#create Global pause variable
global paused
paused = False
#pause and and unpause songs
def pause(is_paused):
    global paused
    paused = is_paused
    if paused:
        #unpause
        pygame.mixer.music.unpause()
        paused = False
    else:
        #pause
        pygame.mixer.music.pause()
        paused = True

#delete a song
def delete_song():
    #current song
    song_box.delete(ANCHOR)
    pygame.mixer.music .stop()


#delete all songs
def delete_all_songs():
    #all song
    song_box.delete(0, END)
    pygame.mixer.music.stop()

#create playlist box
song_box = Listbox(root, bg="black", fg="green", width=60, selectbackground="gray", selectforeground="white")
song_box.pack(pady=20)

#define player control button images
back_btn_img = PhotoImage(file='D:/Project Maya/Maya/maya_ultimate/icons/back50.png')
play_btn_img = PhotoImage(file='D:/Project Maya/Maya/maya_ultimate/icons/play50.png')
pause_btn_img = PhotoImage(file='D:/Project Maya/Maya/maya_ultimate/icons/pause50.png')
stop_btn_img = PhotoImage(file='D:/Project Maya/Maya/maya_ultimate/icons/stop50.png')
forward_btn_img = PhotoImage(file='D:/Project Maya/Maya/maya_ultimate/icons/forward50.png')

#create player control frame
controls_frame = Frame(root)
controls_frame.pack()

#create player control buttons
back_button = Button(controls_frame, image=back_btn_img, borderwidth=0, command=previous_song)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command=stop)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0, command=next_song)

back_button.grid(row=0, column=0, padx=10)
play_button.grid(row=0, column=1, padx=10)
pause_button.grid(row=0, column=2, padx=10)
stop_button.grid(row=0, column=3, padx=10)
forward_button.grid(row=0, column=4, padx=10)

#create menu
my_menu = Menu(root)
root.config(menu=my_menu)

#add Add song playlist
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs",menu=add_song_menu)
add_song_menu.add_command(label="Add One Song To Playlist", command=add_song)
#add many songs to playlist
add_song_menu.add_command(label="Add Many Songs To Playlist", command=add_many_songs)
#delete song menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song From Playlist", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs From Playlist", command=delete_all_songs)


#create status bar
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

songs = os.listdir('D:/Project Maya/Maya/maya_main/maya_music/')
for song in tqdm(songs, ncols=100, desc="Loading Songs"):
    song = song.replace(".mp3", "")
    # insert into playlist
    song_box.insert(END, song)


