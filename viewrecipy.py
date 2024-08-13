import tkinter
from tkinter import *
import tkinter.messagebox as msg
from connection import Connect
import tkinter.ttk as ttk
from gtts import gTTS
import playsound
import os
import threading

class main:
    def __init__(self,userid):
        self.bgcolour = "#C1C3C1"
        self.root = Tk()
        self.root.title('View')
        self.root.state('zoomed')
        self.root.configure(bg=self.bgcolour)

        self.mainlabel = tkinter.Label(self.root, text="View Recipe", font=('arial', 28),bg="#6E726E",relief=tkinter.SUNKEN)
        self.mainlabel.pack(pady=20,ipadx=10,ipady=10)

        self.formframe = tkinter.Frame(self.root,bg="#A1A5A1",width=self.root.winfo_screenwidth())
        self.formframe.pack()
        h = ('arial', 15)

        self.lb1 = tkinter.Label(self.formframe, text="Search by name,description,duration,ingredients,category", font=h)
        self.lb1.grid(row=0, column=0)
        self.txt = tkinter.Entry(self.formframe, width=20)
        self.txt.grid(row=0, column=1, padx=20)
        self.btn1 = tkinter.Button(self.formframe, text="Search", font=('arial', 10), command=self.search,bg="#787D78",foreground="black",activebackground="black",activeforeground="white")
        self.btn2 = tkinter.Button(self.formframe, text="Refresh", font=('arial', 10), command=self.getvalues,bg="#787D78",foreground="black",activebackground="black",activeforeground="white")
        self.btn1.grid(row=0, column=2)
        self.btn2.grid(row=0, column=3, padx=20)

        self.table = ttk.Treeview(self.root, columns=('id','name', 'description','duration','ingredients','category','user'))
        self.table.pack(pady=20,padx=20, expand=True, fill='both')
        self.table.heading('id', text="ID")
        self.table.heading('name', text="NAME")
        self.table.heading('description', text="DESCRIPTION")
        self.table.heading('duration', text="DURATION")
        self.table.heading('ingredients', text="INGREDIENTS")
        self.table.heading('category', text="CATEGORY")
        self.table.heading('user', text="USER")
        self.table['show'] = 'headings'

        self.btn = tkinter.Button(self.root, text="DELETE", width=15, command=self.delete,bg="#787D78",foreground="black",activebackground="black",activeforeground="white")
        self.btn.pack(pady=10)

        self.table.bind("<Double-1>", self.open)

        self.getvalues()

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 15), rowheight=40, foreground="black", background="blue")
        style.configure('Treeview.Heading', font=('arial', 13), rowheight=40, foreground="grey")

        self.root.mainloop()

    def getvalues(self):
        conn = Connect()
        cr = conn.cursor()
        q = "select * from recipy"
        cr.execute(q)
        data = cr.fetchall()
        for row in self.table.get_children():
            self.table.delete(row)
        c = 0
        for i in data:
            self.table.insert('', index=c, value=i)
            c += 1

    def search(self):
        conn = Connect()
        cr = conn.cursor()
        s = self.txt.get()
        q = f"select * from recipy where name like '%{s}%' or duration like '%{s}%' or ingredients like'%{s}%' or category like '%{s}%' or user like '%{s}%'"
        cr.execute(q)
        data = cr.fetchall()
        for row in self.table.get_children():
            self.table.delete(row)
        c=0
        for i in data:
            self.table.insert('',index=c,value=i)
            c+=1

    def delete(self):
        conn = Connect()
        cr = conn.cursor()
        rowid = self.table.selection()
        if len(rowid) == 0:
            msg.showinfo('', "Select a row!")
        elif len(rowid) > 1:
            msg.showinfo('', "Please select only one row at a time!!")
        else:
            items = self.table.item(rowid[0])
            data = items['values']
            print (data)
            q = f"delete from recipy where id='{data[0]}'"
            cr.execute(q)
            conn.commit()
            os.remove(f"recipy_images/{data[0]}.png")
            self.getvalues()
            msg.showinfo('', "Row Deleted")

    def open(self,e):
        self.bgcolour = "#FF9147"
        data=self.table.item(self.table.selection()[0])['values']
        self.root1=Toplevel()
        self.root1.title('Update')
        self.root1.geometry('800x800')
        self.root.configure(bg=self.bgcolour)

        self.lb=tkinter.Label(self.root1,text="Update recipy",font=('arial',28),bg="#6E726E",relief=SUNKEN)
        self.lb.pack(pady=20)

        self.formframe1 = Frame(self.root1,bg="#A1A5A1",width=self.root.winfo_screenwidth())
        self.formframe1.pack()

        h = ('arial', 15)

        self.lb1 = Label(self.formframe1, text="ID", font=h,bg="#A1A5A1",foreground="black")
        self.lb1.grid(row=0, column=0, padx=20, pady=20)
        self.txt1 = Entry(self.formframe1, width=30)
        self.txt1.grid(row=0, column=1, pady=20,ipadx=10,ipady=10)
        self.txt1.insert(0, data[0])
        self.txt1.configure(state='readonly')

        self.lb2 = Label(self.formframe1, text="Name", font=h,bg="#A1A5A1",foreground="black")
        self.lb2.grid(row=1, column=0, pady=20, padx=20)
        self.txt2 = Entry(self.formframe1, width=30)
        self.txt2.grid(row=1, column=1, pady=20,ipadx=10,ipady=10)
        self.txt2.insert(0,data[1])
        # self.txt1.configure(state='readonly')

        self.lb3 = tkinter.Label(self.formframe1, text="Description", font=h,bg="#A1A5A1",foreground="black")
        self.lb3.grid(row=2, column=0, pady=20, padx=20)
        self.txt3 = tkinter.Text(self.formframe1, width=30,height=10)
        self.txt3.grid(row=2, column=1, pady=20,ipadx=10,ipady=10)
        self.txt3.insert('1.0',data[2])

        self.lb4 = tkinter.Label(self.formframe1, text="Duration", font=h,bg="#A1A5A1",foreground="black")
        self.lb4.grid(row=3, column=0, pady=20, padx=20)
        self.txt4 = tkinter.Entry(self.formframe1, width=30)
        self.txt4.grid(row=3, column=1, pady=20,ipadx=10,ipady=10)
        self.txt4.insert(0, data[3])

        self.lb5 = tkinter.Label(self.formframe1, text="Ingredients", font=h,bg="#A1A5A1",foreground="black")
        self.lb5.grid(row=4, column=0, pady=20, padx=20)
        self.txt5 = tkinter.Entry(self.formframe1, width=30)
        self.txt5.grid(row=4, column=1, pady=20,ipadx=10,ipady=10)
        self.txt5.insert(0, data[4])

        self.lb6 = tkinter.Label(self.formframe1, text="Category", font=h,bg="#A1A5A1",foreground="black")
        self.lb6.grid(row=5, column=0, pady=20, padx=20)
        self.txt6 = ttk.Combobox(self.formframe1, state='readonly', values=self.getcat())
        self.txt6.grid(row=5, column=1, pady=20,ipadx=10,ipady=10)
        self.txt6.set(data[5])

        self.lb7 = tkinter.Label(self.formframe1, text="User", font=h,bg="#A1A5A1",foreground="black")
        self.lb7.grid(row=6, column=0, pady=20, padx=20)
        self.txt7 = tkinter.Entry(self.formframe1, width=30)
        self.txt7.grid(row=6, column=1, pady=20,ipadx=10,ipady=10)
        self.txt7.insert(0, data[6])


        self.btn3 = tkinter.Button(self.root1, text="ADD", width=10, font=('arial', 15), command=self.update,bg="#BBDFC5",foreground="black",activebackground="black",activeforeground="white")
        self.btn3.pack(pady=5)

        self.btn4 = tkinter.Button(self.root1, text="PLAY", width=10, font=('arial', 15) ,command=lambda: threading.Thread(target=self.play).start())
        self.btn4.pack(pady=5)

    def getcat(self):
        conn = Connect()
        cr = conn.cursor()
        q = "select name from category"
        cr.execute(q)
        result = cr.fetchall()
        lst=[]
        for i in result:
            lst.append(i[0])
        print (lst)
        return lst

    def play(self):
        lst= os.listdir('.')
        print(lst)
        if 'hello.mp3' in lst:
            os.remove('hello.mp3')
        text1= self.txt3.get('1.0','end-1c')
        obj = gTTS(text=text1,lang='en')
        obj.save("hello.mp3")
        playsound.playsound('hello.mp3')
        os.remove('hello.mp3')


    def update(self):
        conn = Connect()
        cr = conn.cursor()
        id = self.txt1.get()
        name = self.txt2.get()
        description = self.txt3.get('1.0','end-1c')
        duration=self.txt4.get()
        ingredients = self.txt5.get()
        category = self.txt6.get()
        user= self.txt7.get()
        q=f"update recipy set name='{name}',description='{description}',duration='{duration}',ingredients='{ingredients}',category='{category}',user='{user}' where id='{id}'"
        cr.execute(q)
        conn.commit()
        self.getvalues()
        self.root1.destroy()
        msg.showinfo('',"Information Updated")

# if __name__ == '__main__':
#     x=main()