from tkinter import *

print("hello world") 
#Test über Github 2 

Fenster = Tk()
Fenster.title('SERG-Gen by Wiehagener Pythoneers')
Fenster.geometry('1024x256')

labelText1 = Label(master=Fenster, bg='#1e90ff', text='Company Name')
labelText1.place(x=55, y=25, width=150, height=30)
entryText1 = Entry(master=Fenster, bg='white')
entryText1.place(x=220, y=25, width=750, height=30)

labelText2 = Label(master=Fenster, bg='#1e90ff', text='Keywords')
labelText2.place(x=55, y=64, width=150, height=30)
entryText2 = Entry(master=Fenster, bg='white')
entryText2.place(x=220, y=64, width=750, height=30)

labelText3 = Label(master=Fenster, bg='#1e90ff', text='Claim')
labelText3.place(x=55, y=105, width=150, height=30)
entryText3 = Entry(master=Fenster, bg='white')
entryText3.place(x=220, y=105, width=750, height=30)

def text_zusammenfuegen():
    entryEndtext.delete(0, "end")

    Text1 = str(entryText1.get())
    Text2 = str(entryText2.get())
    Text3 = str(entryText3.get())

    if len(Text1) > 4:
        zu_lang1 = len(Text1)-4
        entryEndtext.insert(0, f'Company Name ist {zu_lang1} Zeichen zu lang!')
    elif len(Text2) > 8:
        zu_lang2 = len(Text2) - 8
        entryEndtext.insert(0, f'Keywords sind {zu_lang2} Zeichen zu lang!')
    elif len(Text3) > 8:
        zu_lang3 = len(Text3) - 8
        entryEndtext.insert(0, f'Claim ist {zu_lang3} Zeichen zu lang!')
    elif len(Text1+Text2+Text3) > 16:
        zu_lang_total = len(Text1+Text2+Text3) - 16
        entryEndtext.insert(0, f'SERP-Text ist insgesamt {zu_lang_total} Zeichen zu lang!')
    else:
        entryEndtext.insert(0, f'{Text1} {Text2} {Text3}')



buttonZusammenfuegen = Button(master=Fenster, bg='#0BD9F5', text="SERP erzeugen", command=text_zusammenfuegen)
buttonZusammenfuegen.place(x=55, y=150, widt=150, height=30)
entryEndtext = Entry(master=Fenster, bg='lightgreen')
entryEndtext.place(x=220, y=150, widt=750, height=30)



Fenster.mainloop()
