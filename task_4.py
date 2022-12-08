from tkinter import *
from pygame import mixer
from gtts import gTTS


def clear_text():
    user_text.delete(1.0, END)

def get_text():
    a = user_text.get('1.0','end-1c')

    f = open('text.txt','w+',  encoding='utf-8')
    f.write(a)
    f.close
    
    f = open("text.txt", "r", encoding='utf-8')
    
    text_read = f.readline()
    
    while text_read:
        mixer.init()
        tts=gTTS(text=text_read, lang='en')
        tts.save("0.mp3")
        mixer.music.load("0.mp3")
        mixer.music.play()
        
        text_read = f.readline()
    
    f.close
    #clear_text()


root = Tk()
root.title("Speech synthesizer")
root.geometry()

lbl = Label(text="Your text", width=10)
lbl.pack(side=LEFT, anchor=N, padx=5, pady=5)

user_text = Text()
user_text.pack(fill=BOTH, pady=10, padx=10, expand=True)

button_enter = Button(root, text='Enter', command=get_text)
button_enter.pack(side=RIGHT,padx=5, pady=5)


button_clear = Button(root, text='Clear', command=clear_text)
button_clear.pack(side=RIGHT,padx=5, pady=5)

root.mainloop()
