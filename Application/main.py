import tkinter as tk
from tkinter import ttk

class App():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('240x400+500+300')
        self.root.title('Config App')
        self.mainframe = tk.Frame(self.root, background='Blue')
        self.mainframe.pack(fill='both', expand=True)

        self.text = ttk.Label(self.mainframe, text='Welcome, To Workout app', background='white', font=("Brass Mono", 20))
        self.text.grid(row=0, column=0, pady=10)

        self.text2 = ttk.Label(self.mainframe, text='Enter Your Name: ', background='white', font=("Brass Mono", 15))
        self.text2.grid(row=1, column=0, pady=5)

        self.set_text_field = ttk.Entry(self.mainframe)
        self.set_text_field.grid(row=2, column=0, pady=5)

        self.text3 = ttk.Label(self.mainframe, text='Enter Your Password: ', background='white', font=("Brass Mono", 15))
        self.text3.grid(row=3, column=0, pady=5)

        self.set_text_field2 = ttk.Entry(self.mainframe, show='*')
        self.set_text_field2.grid(row=4, column=0, pady=5)

        set_text_button = ttk.Button(self.mainframe, text='Click me To Register', command=self.set_text)
        set_text_button.grid(row=5, column=0, pady=10)

        self.text4 = ttk.Label(self.mainframe, text='Your Future Name', background='white', font=("Brass Mono", 10))
        self.text4.grid(row=6, column=0, pady=10)

        self.text5 = ttk.Label(self.mainframe, text='Your Future Password', background='white', font=("Brass Mono", 10))
        self.text5.grid(row=7, column=0, pady=10)

        self.root.mainloop()

    def set_text(self):
        newtext = self.set_text_field.get()
        newtext2 = self.set_text_field2.get()

        if len(newtext) < 3:
            self.text4.config(text='Too short name, you are not trusted, quit')
        else:
            self.text4.config(text=newtext)

        if len(newtext2) < 3:
            self.text5.config(text='Too short password, you are not trusted, quit')
        else:
            self.text5.config(text=newtext2)

if __name__ == '__main__':
    App()



