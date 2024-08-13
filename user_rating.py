import tkinter
from tkinter import *
import tkinter.messagebox as msg

import connection

from connection import Connect
import tkinter.ttk as ttk

class main:
    def __init__(self,userid):
        self.bgcolour = "#C1C3C1"
        # self.uid=userid
        self.root = Tk()
        self.root.title('View User')
        self.root.state('zoomed')
        self.root.configure(bg=self.bgcolour)

        self.lb = tkinter.Label(self.root, text='View Recipes', font=('arial', 28),bg="#6E726E",relief=SUNKEN)
        self.lb.pack(pady=20,ipadx=10,ipady=10)

        self.formframe = tkinter.Frame(self.root,bg="#A1A5A1",width=self.root.winfo_screenwidth())
        self.formframe.pack()

        h = ('arial', 15)
        self.lb1 = tkinter.Label(self.formframe, text="Search", font=h,bg="#5A5E5A",foreground="black",activebackground="red",activeforeground="blue")
        self.lb1.grid(row=0, column=0)
        self.txt = tkinter.Entry(self.formframe, width=30)
        self.txt.grid(row=0, column=1, padx=20)
        self.btn1 = tkinter.Button(self.formframe, text="Search", font=('arial', 10), command=self.search,bg="#787D78",foreground="black",activebackground="black",activeforeground="white")
        self.btn2 = tkinter.Button(self.formframe, text="Refresh", font=('arial', 10), command=self.getvalues,bg="#787D78",foreground="black",activebackground="black",activeforeground="white")
        self.btn1.grid(row=0, column=2)
        self.btn2.grid(row=0, column=3, padx=20)

        self.table = ttk.Treeview(self.root, columns=('id', 'userid', 'recipeid', 'ratings', 'description'))
        self.table.pack(pady=10, expand=True, fill='both')
        self.btn = tkinter.Button(self.root, text="DELETE", width=15, command=self.delete)
        self.btn.pack(pady=10)
        self.table.heading('id', text="ID")
        self.table.heading('userid', text="USER ID")
        self.table.heading('recipeid', text="RECIPE ID")
        self.table.heading('ratings', text="RATINGS")
        self.table.heading('description', text="REVIEW")
        self.table['show'] = 'headings'

        self.getvalues(userid)

        style = ttk.Style()
        style.configure('Treeview', font=('arial', 15), rowheight=40, foreground="black", background="white")
        style.configure('Treeview.Heading', font=('arial', 13), rowheight=40, foreground="grey")

        self.root.mainloop()

    def getvalues(self,userid):
        self.conn=connection.Connect()
        self.cr=self.conn.cursor()
        q=f"select * from review where userid='{userid}'"
        self.cr.execute(q)

        data=self.cr.fetchall()
        for row in self.table.get_children():
            self.table.delete(row)
        c=0
        for i in data:
            self.table.insert('',index=c , value=i)
            c+=1

    def search(self):
        self.conn=connection.Connect()
        self.cr=self.conn.cursor()
        s=self.txt.get()
        q=f"select * from review where ratings like '%{s}%'  or recipe_id like '%{s}%'"
        self.cr.execute(q)
        data = self.cr.fetchall()

        for row in self.table.get_children():
            self.table.delete(row)
        c=0
        for i in data:
            self.table.insert('',index=c,value=i)
            c+=1

    def delete(self):
        rowid = self.table.selection()
        if len(rowid)==0:
            msg.showinfo('',"Select a row!")
        elif len(rowid)>1:
            msg.showinfo('',"Please select only one row at a time!!")
        else:
            items=self.table.item(rowid[0])
            data=items['values']
            q=f"delete from review where id='{data[0]}'"
            self.cr.execute(q)
            self.conn.commit()
            self.getvalues()
            msg.showinfo('',"Row Deleted",parent=self.root)

# if __name__ == '__main__':
#     x=main()