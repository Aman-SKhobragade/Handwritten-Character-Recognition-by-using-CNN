from tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from googletrans import Translator, LANGUAGES
from tkinter import Tk, Label, Button, filedialog
from PIL import Image, ImageTk

#----------- Main HCR Window -------------
win = Tk()
win.config(bg='wheat')
win.title('Handwritten Character Recognition')
# win.iconbitmap('icon 2.ico')
win.geometry('1400x780')
win.bind('<Escape>', lambda e, w=win: w.destroy())

#---------- Functions ------------

def open_image(frame):
    filepath = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])

    image = Image.open(filepath)
    image = image.resize((500, 500))

    photo = ImageTk.PhotoImage(image)

    label = Label(left_frame, image=photo)
    label.image = photo  # Keep a reference to prevent garbage collection
    label.place(x=80,y=50)

def exit():
    win.destroy()

def Translatebtn():
    win.destroy()
    root = Tk()
    root.geometry('1080x400')
    # root.iconbitmap('icon 2.ico')
    root.resizable(0, 0)
    root.title("HCR - Language Translator")
    # root.config(bg='#856ff8')
    root.config(bg='#0073e6')

    # Heading
    # Label(root, text="LANGUAGE TRANSLATOR", font="arial 20 bold", bg='#99e5f2').pack()
    Label(root, text="LANGUAGE TRANSLATOR", font="arial 20 bold", bg='#8babf1').pack()

    # INPUT AND OUTPUT TEXT WIDGET
    Label(root, text="Enter Text", font='arial 13 bold', bg='white smoke').place(x=200, y=60)
    Input_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
    Input_text.place(x=30, y=100)

    Label(root, text="Translation", font='arial 13 bold', bg='white smoke').place(x=780, y=60)
    Output_text = Text(root, font='arial 10', height=11, wrap=WORD, padx=5, pady=5, width=60)
    Output_text.place(x=600, y=100)

    #------- Lang list -----------
    language = list(LANGUAGES.values())

    src_lang = ttk.Combobox(root, values=language, width=22)
    src_lang.place(x=20, y=60)
    src_lang.current(src_lang.set('english'))
    # src_lang.set('-Select input language-')

    dest_lang = ttk.Combobox(root, values=language, width=22)
    dest_lang.place(x=890, y=60)
    dest_lang.set('Select Output Language-')

    #---------  Define function ---------

    def Translate():
        translator = Translator()
        translated = translator.translate(text=Input_text.get(1.0, END), src=src_lang.get(), dest=dest_lang.get())

        Output_text.delete(1.0, END)
        Output_text.insert(END, translated.text)


    #---------  Translate Button ----------
    trans_btn = Button(root, text='Translate', font='arial 12 bold', pady=5, command=Translate, bg='royal blue1',
                       activebackground='sky blue')
    trans_btn.place(x=490, y=180)


# --------- Main Frames ------------
back_frame = Frame(win,bg='#5ba300',bd='5',relief=RIDGE)
back_frame.place(x=25,y=20,width=1480,height=760)

left_frame = Frame(win,bg='#0073e6',bd='5',relief=RIDGE)
# left_frame = Frame(win,bg='#856ff8',bd='5',relief=RIDGE)
left_frame.place(x=50,y=40,width=700,height=680)

l_title = Label(left_frame,text='Input Image',bg='yellow',font=('Times new roman',18))
l_title.grid(row=0,columnspan=2,pady=10,padx=10)

# separator = ttk.Separator(back_frame, orient='vertical')
# separator.place(relx=0.47, rely=0, relwidth=0.1, relheight=1)
select_button = Button(left_frame, text="Select Image",command=lambda: open_image(win))
select_button.place(x=300,y=590)

right_frame = Frame(win,bg='#856ff8',bd='5',relief=RIDGE)
right_frame.place(x=780,y=40,width=700,height=680)

r_title = Label(right_frame,text='Text Panel',bg='yellow',font=('Times new roman',18))
r_title.grid(row=0,columnspan=2,pady=10,padx=10)

Output_text = Text(right_frame, font='arial 20', height=18, wrap=WORD, padx=5, pady=5, width=42)
Output_text.place(x=20, y=50)

btn = Button(back_frame,text='Exit',font=('Times new roman',10,'bold'),bg='#4681f4',width='15',height='2',command=exit)
btn.place(x=1320,y=700)

btn = Button(back_frame,text='Traslate',font=('Times new roman',10,'bold'),bg='#4681f4',width='15',height='2',command=Translatebtn)
btn.place(x=1190,y=700)

win.mainloop()