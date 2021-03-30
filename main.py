from future.moves import tkinter
from tkinter import *
from datetime import datetime
import gtts
from playsound import playsound
import os

def Exit():
    screen.destroy()

def Reset():
    msg.set("")
    os.remove("Sound.mp3")

#function to convert text to speech
def TextToSpeech():
    to_convert = msg.get() #to get the text to convert from user
    speech = gtts.gTTS(text=to_convert)#lang='es',tld='es')
    speech.save('Sound.mp3')
    playsound('Sound.mp3')

def Change():
    lang =StringVar()
    new = Entry(screen, width=70, textvariable=lang).place(x=250, y=185)
    to_convert = new.get()

#initialize window
if __name__=="__main__":
    main_color = 'pink'
    screen = Tk(className='Convert Text to Speech')
    screen.geometry("800x600")
    screen.configure(bg=main_color)
    date = str(datetime.now().strftime("%Y-%m-%d %H:%M"))
    print_date = Label(screen, text=date, font=20,bg=main_color).place(x=637, y=570)
    user_text = Label(screen,text="Enter Sentence",font=25,bg=main_color).place(x=100, y=180)
    msg = StringVar()
    input_area = Entry(screen, width=70, textvariable=msg).place(x=250, y=185)
    submit_button = Button(screen,text='convert',font=20,bg='grey',command=TextToSpeech).place(x=250, y=270)
    reset_button = Button(screen,text='reset',font=20,bg='grey',command=Reset).place(x=350, y=270)
    exit_button = Button(screen,text='exit',font=20,bg='grey',command=Exit).place(x=430, y=270)
    lang_button = Button(screen,text='change language',font=20,bg='grey',command=Change).place(x=500,y=270)
    screen.mainloop()




