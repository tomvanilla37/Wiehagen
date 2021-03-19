from tkinter import *

#Freitagnachmmitag neuste Version

#### TKINTER SETUP ####
Fenster = Tk()                                              # variable ereugen, die tkinter-Fenster erzeugt; auf EN ist Fenster meistens "root"
Fenster.title('SERG-Gen by Wiehagener Pythoneers')
Fenster.geometry('1024x300')

#### GLOBALE VARIABLEN ####
drop_list1 = ["Bekannt-CTA1", "Bekannt-CTA2", "Bekannt-CTA3", "Bekannt-CTA4", "Bekannt-CTA5"]
drop_list2 = ["Abverkauf-CTA1", "Abverkauf-CTA2", "Abverkauf-CTA3", "Abverkauf-CTA4", "Abverkauf-CTA5"]



#### FIRMA/KEYWORDS/CLAIM INPUT ####

labelText1 = Label(master=Fenster, bg='#1e90ff', text='Company Name')     #
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

    CTA = clicked.get()                     #CTA-Text der ausgewählt wurde und ausgegeben wird



    if len(Text1) > 4:
        zu_lang1 = len(Text1)-4             # Variable um Überlänge zu berechnen
        entryEndtext.insert(0, f'Company Name ist {zu_lang1} Zeichen zu lang!')
    elif len(Text2) > 8:
        zu_lang2 = len(Text2) - 8
        entryEndtext.insert(0, f'Keywords sind {zu_lang2} Zeichen zu lang!')
    elif len(Text3) > 8:
        zu_lang3 = len(Text3) - 8
        entryEndtext.insert(0, f'Claim ist {zu_lang3} Zeichen zu lang!')
    elif len(Text1+Text2+Text3) > 16:
        zu_lang_total = len(Text1+Text2+Text3+CTA) - 16
        entryEndtext.insert(0, f'SERP-Text ist insgesamt {zu_lang_total} Zeichen zu lang!')
    elif CTA == "WÄHLEN":
        entryEndtext.insert(0, f'Bitte Call to Action wählen! ')
    else:
        entryEndtext.insert(0, f'{Text1} {Text2} {Text3} {CTA}')


#### DROPDOWN-MENÜ #####
clicked = StringVar()
clicked.set("WÄHLEN")

drop_CTA = OptionMenu(Fenster, clicked, *drop_list1)            #drop = dropdown
drop_CTA.place(x=530, y=150, widt=440, height=31)
drop_CTA.config(state="disabled")


drop_CTA2 = OptionMenu(Fenster, clicked, *drop_list2)
drop_CTA2.place(x=530, y=150, widt=440, height=31)
drop_CTA2.config(state="disabled")



def choose_Bekanntheit():
    drop_CTA = OptionMenu(Fenster, clicked, *drop_list1)
    drop_CTA.config(state="normal")
    button_bekannt.configure(bg="white", fg="red")
    button_abverkauf.configure(bg="grey", fg="darkgrey")
    drop_CTA.place(x=530, y=150, widt=440, height=31)


def choose_Abverkauf():
    drop_CTA2 = OptionMenu(Fenster, clicked, *drop_list2)
    drop_CTA2.config(state="normal")
    button_abverkauf.configure(bg="white", fg="red")
    button_bekannt.configure(bg="grey", fg="darkgrey")
    drop_CTA2.place(x=530, y=150, widt=440, height=31)






#### ZIEL AUSWÄHLEN (BUTTONS) #####

labelText4 = Label(master=Fenster, bg='#1e90ff', text='Welches Ziel?')
labelText4.place(x=55, y=150, width=150, height=30)

button_bekannt = Button(master=Fenster, bg='darkgrey', text="Bekanntheit", command= choose_Bekanntheit)
button_bekannt.place(x=220, y=150, widt=150, height=30)

button_abverkauf = Button(master=Fenster, bg='darkgrey', text="Abverkauf", command=choose_Abverkauf)
button_abverkauf.place(x=375, y=150, widt=150, height=30)






#### SERP GENERIEREN ####

buttonZusammenfuegen = Button(master=Fenster, bg='#0BD9F5', text="SERP generieren", command= text_zusammenfuegen)
buttonZusammenfuegen.place(x=55, y=225, widt=150, height=30)
entryEndtext = Entry(master=Fenster, bg='lightgreen')               #Ausgabetext ganz unten
entryEndtext.place(x=220, y=225, widt=750, height=30)



Fenster.mainloop()





