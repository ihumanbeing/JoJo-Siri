import speech_recognition as sr
import winsound
from tkinter import *
import emoji
from gtts import gTTS
from playsound import playsound

#Tkinter window
root = Tk()
root.iconbitmap('icon.ico')
root.title("JoJo Siri")
root.resizable(0,0)
root.geometry(("250x50"))

num = 0

# Commands
outputs = [
    "giorno's theme","torture dance",
    "pillar men awaken","stardust crusaders",
    "sono chi no sodomy","hell to you",
    "morio cho","lick theme",
    "lick","kira's theme",
    "dios theme","the world",
    "dios world","walk like an egyptian",
    "i refuse", "bloody stream",
    "fighting gold", "sono chi no kioku"
]

outputs2 = ["play " + output for output in outputs]

# Song names
songs = [
    'giorno.wav','torturedance.wav',
    'awaken.wav','crusaders.wav',
    'sonochi.wav','hell2u.wav',
    "moriohcho.wav","kakyoin.wav",
    "rero.wav","kira.wav",
    "diotheme.wav","zawarudo.wav",
    "dioworld.wav","egyptian.wav",
    "irefuse.wav","bloodystream.wav",
    "fightinggold.wav","kioku.wav"
]

songs = ["audio/" + song for song in songs]

language = 'en'
spk = gTTS(text="Speak", lang=language, slow=False)
spk.save("audio/Speak.mp3")

# Get command
def rec():
    with sr.Microphone() as source:
        winsound.PlaySound(None, winsound.SND_ASYNC)
        print('Speak : ')
        
        playsound("audio/Speak.mp3")
        audio = r.listen(source)
    
        try:
            text = r.recognize_google(audio)
            text = text.lower()
            print('{}'.format(text))
            for output in outputs:
                    if output == text:
                            num = outputs.index(output)
                            winsound.PlaySound(songs[num], winsound.SND_ASYNC | winsound.SND_ALIAS )
            for output2 in outputs2:
                    if output2 == text:
                            num = outputs2.index(output2)
                            winsound.PlaySound(songs[num], winsound.SND_ASYNC | winsound.SND_ALIAS )

                       
            
        except:
            print('Voice not recognized')


#GUI
lb = Label(root, pady=5,padx=10,text="\tSpeak:  ").grid(row=1,column=3)
btn = Button(root, bd=0.5,pady=10, padx=10, text=(emoji.emojize(':microphone:')), command =rec).grid(row=1, column=4, columnspan=1)

r = sr.Recognizer()
