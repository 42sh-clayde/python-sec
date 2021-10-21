from tkinter import *

#create a frame
root = Tk()
#Cganhe frame's title
root.title("ClaydePass")
root.geometry ("720x480")
root.minsize (480,360)
root.config(background='#000000')

#create a frame
frame = Frame(root,bg='#000000')
bouton =Frame(frame,bg='#000000')

#add a text
label_title = Label(frame,text="Welcome to my Password Manager", font=("Geneva",30), bg='#000000', fg='white')
label_title.pack()

sub_label_title = Label(frame,text="Happy to count you among our users", font=("Geneva",12), bg='#000000', fg='white')
sub_label_title.pack()

#Add a button 

log_button= Button(bouton, text ='Login').pack(side=LEFT, padx=15, pady=30) #add command=fonction 
sign_button=Button(bouton, text ='Sing up').pack(side=RIGHT, padx=15, pady=30)
#use frame
bouton.pack(expand=YES)
frame.pack(expand=YES)



#display frame
root.mainloop()

