import tkinter
from tkinter import *
import tkinter.messagebox as msg
from connection import Connect
import tkinter.ttk as ttk
from tkinter.filedialog import askopenfilename
import cv2
import random

class main:
    def __init__(self,userid):
        self.bgcolour = "#C1C3C1"
        self.root=Tk()
        self.root.title('add recipy')
        self.root.state('zoomed')
        self.root.configure(bg=self.bgcolour)

        self.mainlabel=tkinter.Label(self.root,text="Add Recipe",font=('arial',28),bg="#6E726E")
        self.mainlabel.pack(pady=20, ipadx=10, ipady=10)

        self.formframe=tkinter.Frame(self.root,bg="#A1A5A1",width=self.root.winfo_screenwidth())
        self.formframe.pack()
        h=('arial',15)

        self.name=tkinter.Label(self.formframe,text="Name",font=h,bg='#A1A5A1')
        self.name.grid(row=0,column=1,pady=20,padx=20)
        self.txt1=tkinter.Entry(self.formframe,width=30)
        self.txt1.grid(row=0,column=2,pady=10,ipadx=10,ipady=10)

        self.description = tkinter.Label(self.formframe, text="Description", font=h,bg='#A1A5A1')
        self.description.grid(row=1, column=1, pady=20, padx=20)
        self.txt2 = tkinter.Text(self.formframe, width=15,height=5)
        self.txt2.grid(row=1, column=2, pady=10,ipadx=10,ipady=10)

        self.duration = tkinter.Label(self.formframe, text="Duration(in mins)", font=h,bg='#A1A5A1')
        self.duration.grid(row=2, column=1, pady=20, padx=20)
        self.txt3 = tkinter.Entry(self.formframe, width=30)
        self.txt3.grid(row=2, column=2, pady=10,ipadx=10,ipady=10)

        self.ing = tkinter.Label(self.formframe, text="Ingredients", font=h,bg='#A1A5A1')
        self.ing.grid(row=3, column=1, pady=10, padx=10)
        self.txt4 = tkinter.Text(self.formframe, width=30,height=5)
        self.txt4.grid(row=3, column=2, pady=10,ipadx=10,ipady=10)

        self.cat = tkinter.Label(self.formframe, text="Category", font=h,bg='#A1A5A1')
        self.cat.grid(row=4, column=1, pady=10, padx=10)
        self.txt5 = ttk.Combobox(self.formframe, state='readonly', values=self.getcat())
        self.txt5.grid(row=4, column=2, pady=10,ipadx=10,ipady=10)

        self.uid = tkinter.Label(self.formframe, text="User ID", font=h,bg='#A1A5A1')
        self.uid.grid(row=5, column=1, pady=10, padx=10)
        self.txt6 = tkinter.Entry(self.formframe,width=30 )
        self.txt6.grid(row=5, column=2, pady=10,ipadx=10,ipady=10)
        self.txt6.insert(0,userid)
        self.txt6.configure(state='readonly')

        self.lb1 = tkinter.Label(self.formframe, text="Select Image", font=h,bg='#A1A5A1')
        self.lb1.grid(row=6, column=1, pady=10, padx=10)
        self.txt7 = tkinter.Entry(self.formframe,width=30 )
        self.txt7.grid(row=6, column=2, pady=10,ipadx=10,ipady=10)

        self.btn2 = tkinter.Button(self.formframe, text='Select', font=('arial', 15, 'bold'), command=self.selectImage,bg='#787D78',foreground='black',activebackground='black',activeforeground="white")
        self.btn2.grid(row=6, column=3, pady=10)

        self.btn = tkinter.Button(self.root, text='Submit', width=11, height=1, font=('arial', 15, 'bold'),command=self.insertRecipy,bg='#787D78',foreground='black',activebackground='black',activeforeground="white")
        self.btn.pack(pady=5)

        self.root.mainloop()

    def selectImage(self):
        imagepath = askopenfilename(filetypes=[('Images', '*.png;*.jpg;*.jpeg')])
        self.txt7.delete(0,'end')
        self.txt7.insert(0, imagepath)

    def getcat(self):
        conn = Connect()
        cr = conn.cursor()
        q = "select name from category"
        cr.execute(q)
        result = cr.fetchall()
        lst=[]
        for i in result:
            lst.append(i[0])
        return lst

    def insertRecipy(self):
        n=self.txt1.get()
        des=self.txt2.get('1.0','end-1c')
        dur=self.txt3.get()
        ingr=self.txt4.get('1.0','end-1c')
        cat=self.txt5.get()
        us=self.txt6.get()
        if n=="" or des=="" or dur=="" or ingr=="" or cat=="" or us=="":
            msg.showinfo('',"All fields are Mandatory",parent=self.root)
        else:
            conn = Connect()
            cr = conn.cursor()
            q=f"insert into recipy values(null,'{n}','{des}','{dur}','{ingr}','{cat}',{us}, '')"
            cr.execute(q)
            conn.commit()
            id = cr.lastrowid
            file = self.txt7.get()
            img = cv2.imread(file)
            image_name = f"recipy_images/{id}.png"

            q = f"update recipy set image='{image_name}' where id='{id}'"
            print(q)
            cr.execute(q)
            cv2.imwrite(image_name, img)
            conn.commit()
            msg.showinfo('Added', " recipy Added", parent=self.root)
            # self.txt1.delete(0,'end')
            # self.txt2.delete(0,'end')
            # self.txt3.delete(0,'end')
            # self.txt4.delete(0,'end')
            # self.txt5.delete(0,'end')
            # self.txt6.delete(0,'end')



# if __name__ == '__main__':
#      x=main(2)
