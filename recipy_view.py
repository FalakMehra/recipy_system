from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk as ttk
import tkinter.messagebox as msg
from connection import Connect
import customtkinter
from gtts import gTTS
import playsound
import os
import threading

import connection


class Main:
    def __init__(self,userid,username):
        self.id=userid
        name=username
        self.bgcolour = "#C1C3C1"
        self.root = Toplevel()
        self.root.state('zoomed')
        self.root.configure(bg=self.bgcolour)

        self.mainLabel = Label(self.root, text="Recipe List", font=('', 28, 'bold'),bg="#6E726E",relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.recipyFrame = customtkinter.CTkScrollableFrame(self.root, width=self.root.winfo_screenwidth(),height=self.root.winfo_screenheight())
        self.recipyFrame.pack(pady=10)

        self.recipyFrame.columnconfigure(0)

        self.getRecipy()

        self.root.mainloop()

    def getRecipy(self):
        self.conn =Connect()
        self.cr = self.conn.cursor()

        q = f"select * from recipy where image !=''"
        self.cr.execute(q)
        result = self.cr.fetchall()
        print(result)
        self.showRecipy(result)

    def showRecipy(self, recipes):
        for i in recipes:
            print(i[1])
            self.f = Frame(self.recipyFrame, width=self.root.winfo_screenwidth())
            self.f.pack(expand=True, fill='both')

            img = Image.open(fp=i[-1])
            print(img)
            img = img.resize((200,200))
            imgTk = ImageTk.PhotoImage(image=img)
            self.l = Label(self.f, image=imgTk)
            self.l.image=imgTk
            self.l.grid(row=0, column=0, pady=10, padx=10)

            self.f1 = Frame(self.f)
            self.f1.grid(row=0, column=1, pady=10, padx=10)

            self.nameLabel = Label(self.f1, text=i[1], font=('', 14))
            self.nameLabel.pack(pady=10)
            self.duration = Label(self.f1, text=f"Duration - {i[3]}", font=('', 12))
            self.duration.pack(pady=10)
            self.category = Label(self.f1, text=f"Category - {i[5]}", font=('', 12))
            self.category.pack(pady=10)

            self.btn = Button(self.f1, text="View More", font=('', 14), command=
                              lambda r=i: self.playRecipy(r),bg="#787D78",foreground="black",activebackground="black",activeforeground="white")
            self.btn.pack()



    def playRecipy(self, recipy):
        print(recipy)
        self.root1 = Toplevel()
        self.root1.title('Recipy')
        self.root1.state('zoomed')

        self.mainLabel =Label(self.root1, text=f"{recipy[1]}", font=('', 28, 'bold'))
        self.mainLabel.pack(pady=20)

        self.recipyFrame1 = customtkinter.CTkScrollableFrame(self.root1, width=self.root1.winfo_screenwidth(),height=self.root1.winfo_screenheight())
        self.recipyFrame1.pack(pady=20)

        self.f2 = Frame(self.recipyFrame1, width=self.root1.winfo_screenwidth(),height=self.root1.winfo_screenheight())
        self.f2.grid(row=0,column=0)

        img = Image.open(fp=recipy[-1])
        print(img)
        img = img.resize((500,500))
        imgTk = ImageTk.PhotoImage(image=img)
        self.lb = Label(self.f2, image=imgTk)
        self.lb.image = imgTk
        self.lb.grid(row=0, column=0, pady=5, padx=5)

        self.f3 = Frame(self.f2)
        self.f3.grid(row=0, column=1, pady=5, padx=5)


        self.duration = Label(self.f3, text=f"Duration-{recipy[3]}", font=('', 18,'bold'))
        self.duration.pack(anchor='w')

        self.category = Label(self.f3, text=f"Category-{recipy[5]}", font=('', 18,'bold'))
        self.category.pack(anchor='w')

        self.category = Label(self.f3, text=f"Description", font=('', 18,'bold'))
        self.category.pack(anchor='w')
        self.category = Label(self.f3, text=f"{recipy[2]}", font=('', 18),wraplength=1000)
        self.category.pack(anchor='w')

        self.category = Label(self.f3, text=f"Ingredients", font=('', 18,'bold'))
        self.category.pack(anchor='w')
        self.category = Label(self.f3, text=f"{recipy[4]}", font=('', 18),wraplength=1000)
        self.category.pack(anchor='w')

        self.btn4 = Button(self.f2, text="PLAY", width=10, font=('arial', 15),
                                   command=lambda: threading.Thread(target=self.play, args=[recipy]).start(),bg="#787D78",foreground="black",activebackground="red",activeforeground="blue")
        self.btn4.grid(row=4,column=1)
        self.f5 = Frame(self.recipyFrame1)
        self.f5.grid(row=1, column=0)

        self.lb1 = Label(self.f5, text="ID", font=('arial',18))
        self.lb1.grid(row=0, column=0, padx=20, pady=20)
        self.txt1 = Entry(self.f5, width=30)
        self.txt1.grid(row=0, column=1, pady=10)
        self.txt1.insert(0,self.id)
        self.txt1.configure(state='readonly')


        self.lb2 = Label(self.f5, text='RecipyID', font=('arial', 14))
        self.txt2 = Entry(self.f5, font=('arial', 14))
        self.lb2.grid(row=0, column=2, pady=10, padx=10)
        self.txt2.grid(row=0, column=3, pady=10, padx=10)
        self.txt2.insert(0,recipy[0])
        self.txt2.configure(state='readonly')

        self.lb3 = Label(self.f5, text='Enter Ratings', font=('arial', 14))
        self.txt3 = Entry(self.f5, font=('arial', 14))
        self.lb3.grid(row=0, column=4, pady=10, padx=10)
        self.txt3.grid(row=0, column=5, pady=10, padx=10)

        self.view =Label(self.f5, text="View", font=('arial', 14))
        self.view.grid(row=1, column=1, pady=20, padx=20)
        self.txt4 =Text(self.f5, width=30, height=5)
        self.txt4.grid(row=1, column=2, pady=20)

        rid=recipy[0]
        self.bt1 =Button(self.f5, text='Submit', font=('arial', 14), command=lambda:self.insertreview(rid),bg="#BBDFC5",foreground="black",activebackground="black",activeforeground="white")
        self.bt1.grid(row=2, column=2, pady=10)



    def insertreview(self,rid):

        Ratings= self.txt3.get()
        View= self.txt4.get('1.0','end-1c')

        if Ratings== '' or View== '':
            msg.showwarning('WARNING', 'PLEASE FILL ALL THE DETAILS')
        else:
            conn = Connect()
            cr = conn.cursor()
            q = f"insert into review values(null,'{id}','{rid}','{Ratings}','{View}')"
            cr.execute(q)
            conn.commit()
            msg.showinfo("SUCCESS", "REVIEW HAS BEEN ADDED")

    def play(self,recipy):
        lst = os.listdir('.')
        print(lst)
        if 'hello.mp3' in lst:
            os.remove('hello.mp3')

        obj = gTTS(text=recipy[2], lang='en')
        obj.save("hello.mp3")
        playsound.playsound('hello.mp3')
        os.remove('hello.mp3')

        self.root1.mainloop()


# obj = Main()