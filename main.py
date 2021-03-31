from future.moves import tkinter
from tkinter import *
from datetime import datetime
import gtts
from playsound import playsound
import os

def Exit():
    screen.destroy()

def Reset():
    msg_text.set("")
    msg_file.set("")

#function to convert text to speech
def TextToSpeech():
    to_convert = msg_text.get() #to get the text to convert from user
    speech = gtts.gTTS(text=to_convert)
    speech.save('Sound.mp3')
    playsound('Sound.mp3')
    os.remove("Sound.mp3")

# function to convert text from file to speech. we assume that the file located in the same folder as a project
def FileToSpeech():
    file_name = msg_file.get() # to get the name of the file from the user
    file_to_convert = open(file_name, 'r')
    sentance = file_to_convert.read()
    speech = gtts.gTTS(text=sentance)
    speech.save('Sound.mp3')
    playsound('Sound.mp3')
    os.remove("Sound.mp3")
    file_to_convert.close()


if __name__=="__main__":
    # initialize window
    main_color = 'pink'
    screen = Tk(className='Convert Text to Speech')
    screen.geometry("800x600")
    screen.configure(bg=main_color)

    # define date
    date = str(datetime.now().strftime("%Y-%m-%d %H:%M"))

    # print text to the screen
    print_date = Label(screen, text=date, font=20,bg=main_color).place(x=637, y=570)
    user_text = Label(screen,text="Enter Sentence",font=25,bg=main_color).place(x=100, y=180)
    user_file = Label(screen,text='Enter File Name',font=25,bg=main_color).place(x=100, y=280)

    msg_text = StringVar()
    msg_file = StringVar()

    # define input area for the user
    input_text = Entry(screen, width=70, textvariable=msg_text).place(x=250, y=185)
    input_file = Entry(screen,width=70,textvariable=msg_file).place(x=250, y=285)

    # define different buttons
    submit_text_button = Button(screen,text='Convert Text',font=20,bg='grey',command=TextToSpeech).place(x=250, y=220)
    submit_file_button = Button(screen,text='Convert File',font=20,bg='grey',command=FileToSpeech).place(x=250, y=320)
    reset_button = Button(screen,text='Reset',font=20,bg='grey',command=Reset).place(x=350, y=420)
    exit_button = Button(screen,text='Exit',font=20,bg='grey',command=Exit).place(x=430, y=420)

    # run
    screen.mainloop()




