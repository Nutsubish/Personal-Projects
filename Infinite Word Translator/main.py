from tkinter import *
from tkinter import ttk,messagebox
from googletrans import *
import googletrans
import textblob
  

root = Tk()
root.title("Google Translator")
root.geometry("1080x400")


def label_change():
    c=button1.get()
    c1 = button2.get()
    label1.configure(text=c)
    label2.configure(text=c1)
    root.after(1000,label_change)


def translate_now():
    global language
    try:
        text_ = text1.get(1.0, END).strip()
        c2 = button1.get()
        c3 = button2.get()
        
        if text_:
            translator = Translator()
            words = translator.detect(text_)
            lan = words.lang
            
            lan_ = None
            for i, j in language.items():
                if j == c3:
                    lan_ = i
                    break
            
            if lan_:
                translated = translator.translate(text_, src=lan, dest=lan_)
                text2.delete(1.0, END)
                text2.insert(END, translated.text)
            else:
                messagebox.showerror("Translation Error", "Target language not found.")
    except Exception as e:
        messagebox.showerror("Translation Error", f"Please try again. Error: {e}")





language = googletrans.LANGUAGES
languageV= list(language.values())
lang1 = language.keys()

button1 = ttk.Combobox(root, values=languageV, font='Roboto 14', state="r")
button1.place(x=110,y=20)
button1.set("ENGLISH")

label1 = Label(root,text="From Language",font="segoe 30 bold", bg="white",width=18,bd=5,relief=GROOVE,fg="yellow")
label1.place(x=10,y=50)

f=Frame(root,bg="Black",bd=5)
f.place(x=10,y=118,width=440,height=210)

text1 = Text(f,bg="yellow",relief=GROOVE,wrap=WORD,font="segoe 30")
text1.place(x=0,y=0,width=430,height=200)

scrollbar1 = Scrollbar(f)
scrollbar1.pack(side="right",fill="y")

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)



button2 = ttk.Combobox(root,values=languageV, font='RobotV 14', state="r")
button2.place(x=730,y= 20)
button2.set("SELECT LANGUAGE")

label2 = Label(root,text="To Language",font="segoe 30 bold", bg="white",width=18,bd=5,relief=GROOVE,fg="yellow")
label2.place(x=620,y=50)


f1=Frame(root,bg="Black",bd=5)
f1.place(x=620,y=118,width=440,height=210)

text2 = Text(f1,bg="yellow",relief=GROOVE,wrap=WORD,font="segoe 30")
text2.place(x=0,y=0,width=430,height=200)

scrollbar2 = Scrollbar(f1)
scrollbar2.pack(side="right",fill="y")

scrollbar2.configure(command=text2.yview)
text2.configure(yscrollcommand=scrollbar2.set)

#to translate
translate = Button(root,text="Translate",font = "Roboto 15 bold italic",activebackground="purple",bd=5,bg='red',fg='white',command=translate_now)
translate.place(x=480,y=250)



label_change()


root.configure(bg="white")
root.mainloop()
