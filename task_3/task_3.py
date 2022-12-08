from tkinter import *
from decimal import *
from pygame import mixer
import time


def sound(num):
    mixer.init()
    mixer.music.load(str(num)+".mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        time.sleep(0.1)

def calculate():
    global stack
    global label
    result = 0
    operand2 = Decimal(stack.pop())
    operation = stack.pop()
    operand1 = Decimal(stack.pop())
    if operation == '+':
        result = operand1 + operand2
    if operation == '-':
        result = operand1 - operand2
    if operation == '/':
        result = operand1 / operand2
    if operation == '*':
        result = operand1 * operand2
    label.configure(text=str(result))

def click(text):
    global activeStr
    global stack
    if text == 'CE':
        sound(15)
        stack.clear()
        activeStr = ''
        label.configure(text='0')
    elif '0' <= text <= '9':
        activeStr += text
        label.configure(text=activeStr)
        sound(text)
    elif text == '.':
        sound(10)
        if activeStr.find('.') == -1:
            activeStr += text
            label.configure(text=activeStr)
    else:
        if len(stack) >= 2:
            stack.append(label['text'])
            calculate()
            sound(16)
            stack.clear()
            stack.append(label['text'])
            symb = []
            work = str(stack)
            work = work[2:-2]
            for count in range(len(work)):
                symb.append(work[count])
            for sym in symb:    
                if sym == '-':
                    sound(12)
                elif sym == '.':
                    sound(10)
                else:
                    sound(sym)
            activeStr = ''
            if text != '=':
                stack.append(text)
        else:
            if text != '=':
                if text == '+':
                    sound(11)
                elif text == '-':
                    sound(12)
                elif text == '/':
                    sound(13)
                elif text == '*':
                    sound(14)
                stack.append(label['text'])
                stack.append(text)
                activeStr = ''
                label.configure(text)  


root = Tk()
root.title('Калькулятар')

buttons = (('7', '8', '9', '/', '4'),
           ('4', '5', '6', '*', '4'),
           ('1', '2', '3', '-', '4'),
           ('.', '0', '=', '+', '4')
           )

activeStr = ''
stack = []

label = Label(root, text='0', width=35)
label.grid(row=0, column=0, columnspan=4, sticky="nsew")

button = Button(root, text='CE', command=lambda text='CE': click(text))
button.grid(row=1, column=3, sticky="nsew")
for row in range(4):
    for col in range(4):
        button = Button(root, text=buttons[row][col],
                command=lambda row=row, col=col: click(buttons[row][col]))
        button.grid(row=row + 2, column=col, sticky="nsew")

root.grid_rowconfigure(6, weight=1)
root.grid_columnconfigure(4, weight=1)

root.mainloop()


