from tkinter import *
from tkinter import ttk, messagebox
import googletrans
from googletrans import Translator
from tkinter import filedialog
from langdetect import detect


window = Tk()
bkimage = PhotoImage(file="image.png.png")
labelbg = Label(window, image = bkimage)
labelbg.place(x = 0, y =0, relwidth=1, relheight=1)
window.title("TRANSlATOR")
window.geometry("1280x720")
window.resizable(False, False)
window.configure(background="gray")
check_autodet = False


def label_change() :
    
    c1 = combo1.get()
    
    c2 = combo2.get()
    label1.configure(text=c1.upper())
    label2.configure(text=c2.upper())
    window.after(100, label_change)

def translate_now() :
    in_text = text1.get(1.0, END)
    t1 = Translator()
    if(check_autodet) :
        in_lang = detect_lang
    else :
        in_lang = combo1.get()
    out_text = t1.translate(in_text, src = in_lang, dest = combo2.get() )
    out_text = out_text.text
    text2.delete(1.0, END)
    text2.insert(END, out_text)

def browse_file() :
    filepath = filedialog.askopenfilename()
    f1 = open(filepath, 'r')
    file_in = f1.read()
    file_in = str(file_in)
    f1.close()

    t1 = Translator()
    
    file_out = t1.translate(file_in, src = combo1.get(), dest = combo2.get() )
    file_out1 = file_out.text
    file_out = str(file_out1)
    
    with open(filepath+"_tranlated", 'w', encoding='utf-8') as f1:
        f1.write(file_out)
    f1.close()
    window.destroy()

def auto_detect() :
    global detect_lang
    global check_autodet
    detect_lang = detect(text1.get(1.0, END))
    label1.configure(text = detect_lang)
    check_autodet = True


#for icon
title_icon = PhotoImage(file="google.png.png")
window.iconphoto(False, title_icon)

#for arrow
arrow_photo= PhotoImage(file="double-arrow.png")

language = googletrans.LANGUAGES
languageV = list(language.values())
lang1 = language.keys()

#first combobox

combo1 = ttk.Combobox(window, values = languageV, font = ("Comic Sans", 18), state= 'r')

combo1.place(x=100, y = 36)
combo1.set ("ENGLISH")

label1 = Label(window, text = "ENGLISH",
            font = ("ARIAL", 30, "bold"),
            bg = "#cccccc", width=16,
            border=6, relief=GROOVE)

label1.place(x = 12, y = 90)

#second combobox

combo2 = ttk.Combobox(window, values = languageV,
                    font = ("Comic Sans", 18),
                    state = 'r' )
combo2.place(x = 840, y = 36)
combo2.set("SELECT LANGUAGE")

label2 = Label(window, text = "SELECT LANGUAGE",
            font = ("ARIAL", 30, "bold"),
            bg = "#cccccc", width=16,
            border=6, relief=GROOVE)

label2.place(x = 750, y = 90)

#first frame
f1 = Frame(window, bg = 'black', bd = 5)
f1.place(x= 12, y = 198, width=450, height = 378)

text1 = Text(f1, font = ("Comic Sans", 20), bg="white",relief=GROOVE, wrap=WORD )
text1.place(x = 0, y = 0, width=440, height =368)

scrollbar1 = Scrollbar(f1)
scrollbar1.pack(side="right", fill = 'y')

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand = scrollbar1.set)

#second frame
f2 = Frame(window, bg = "black", bd = 5)
f2.place(x= 828, y = 198, width=450, height = 378)

text2 = Text(f2, font = ("Comic Sans", 20), bg="white",
                relief=GROOVE, wrap=WORD, )
text2.place(x = 0, y = 0, width=440, height =368)

scrollbar2 = Scrollbar(f2)
scrollbar2.pack(side="right", fill = 'y')

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand = scrollbar2.set)

#translation button
translate = Button(window, text = "TRANSLATE",
                font = ("Comic Sans", 20), activebackground= 'white',
                cursor='hand2', bd = 1, width= 255, height=200, bg = 'black',
                fg = 'white', command=translate_now, image=arrow_photo, compound=TOP )
translate.place(x = 515, y = 250)

#browse file button 

browse_button = Button(window, text="Add file", command=browse_file, 
                        font=("Comic Sans", 20), bg = "gray", state=ACTIVE)
browse_button.place(x= 12, y = 576)

detect_button = Button( window, text = "Auto detect", command=auto_detect, 
                        font=("Comic Sans", 20), bg = "gray", state=ACTIVE)
detect_button.place(x = 265, y = 576 )

label_change()
window.mainloop()




