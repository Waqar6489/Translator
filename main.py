from tkinter import *
from tkinter import ttk
from googletrans import Translator, LANGUAGES

def sert(text="type", src="English", dest="Urdu"):
    trans = Translator()
    trans1 = trans.translate(text, src=src.lower(), dest=dest.lower())
    return trans1.text

def data():
    cb = comb_box.get()
    cd = comb_dest.get()
    messg = sor_txt.get(1.0, END).strip()
    if messg:
        textget = sert(text=messg, src=cb, dest=cd)
        dest_txt.delete(1.0, END)
        dest_txt.insert(END, textget)

root = Tk()
root.title("SpeakEase")
root.geometry("600x700")
root.config(bg="grey")

label_txt = Label(root, text="Translator", font=("Arial", 30, "bold"), bg="grey", fg="white")
label_txt.place(x=150, y=80, height=40, width=300)

label_txt = Label(root, text="Enter Text:", font=("Arial", 20, "bold"), bg="grey", fg="white")
label_txt.place(x=22, y=145, height=40, width=200)

sor_txt = Text(root, font=("Arial", 15, "bold"), bg="White", wrap=WORD)
sor_txt.place(x=50, y=185, height=150, width=500)

list_show = list(LANGUAGES.values())
comb_box = ttk.Combobox(root, values=list_show)
comb_box.place(x=50, y=350, height=40, width=153)
comb_box.set("English")

buton = Button(root, text="Translation", relief=RAISED, command=data)
buton.place(x=230, y=350, height=40, width=153)

comb_dest = ttk.Combobox(root, values=list_show)
comb_dest.place(x=400, y=350, height=40, width=153)
comb_dest.set("Urdu")

label_txt = Label(root, text="Translated Text:", font=("Arial", 20, "bold"), bg="grey", fg="white")
label_txt.place(x=10, y=420, height=40, width=300)

dest_txt = Text(root, font=("Arial", 15, "bold"), bg="White", wrap=WORD)
dest_txt.place(x=50, y=460, height=150, width=500)

root.mainloop()
