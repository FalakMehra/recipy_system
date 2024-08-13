from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
from connection import Connect


class Main:
    def __init__(self):
        self.bgcolour = "#C1C3C1"
        self.conn =Connect()
        self.cr = self.conn.cursor()
        self.root = Tk()
        self.root.state('zoomed')
        self.root.configure(bg=self.bgcolour)
        self.root.title("View Admin")
        self.mainLabel = Label(self.root, text="View Admin", font=('arial', 26, 'bold'),bg="#6E726E",relief=SUNKEN)
        self.mainLabel.pack(pady=20,ipadx=10,ipady=10)

        self.searchFrame = Frame(self.root,bg="#A1A5A1",width=self.root.winfo_screenwidth())
        self.searchFrame.pack()

        self.searchLabel = Label(self.searchFrame, text="Search",font=('arial', 14),bg="#A1A5A1",foreground="black",activebackground="black",activeforeground="white")
        self.searchLabel.grid(row=0, column=0, pady=10, padx=10)
        self.searchBox = Entry(self.searchFrame, font=('arial', 14), width=30)
        self.searchBox.grid(row=0, column=1, pady=10, padx=10)
        self.searchBtn = Button(self.searchFrame, font=('arial', 14), text="Search", width=10, command=self.searchUser,bg="#787D78",foreground="black",activebackground="black",activeforeground="white")
        self.searchBtn.grid(row=0, column=2, pady=10, padx=10)
        self.refreshBtn = Button(self.searchFrame, font=('arial', 14), text="Refresh", width=10, command=self.getValues,bg="#787D78",foreground="black",activebackground="black",activeforeground="white")
        self.refreshBtn.grid(row=0, column=3, pady=10, padx=10)

        self.userTable = ttk.Treeview(self.root, columns=('userid', 'recipyid', 'rating', 'view'))
        self.userTable.pack(pady=20, padx=20, expand=True, fill='both')

        self.userTable.heading('userid', text="UserID")
        self.userTable.heading('recipyid', text="RecipyID")
        self.userTable.heading('rating', text="Rating")
        self.userTable.heading('view', text="View")


        self.userTable['show'] = 'headings'

        self.getValues()

        self.style = ttk.Style()
        self.style.configure("Treeview", font=('arial', 14), rowheight=40, foreground="black", background='white')
        self.style.configure("Treeview.Heading", font=('arial', 14))

        self.deleteBtn = Button(self.root, font=('arial', 14), text="Delete", width=10, command=self.deleteUser,bg="#787D78",foreground="black",activebackground='black',activeforeground="white")
        self.deleteBtn.pack(pady=10)

        self.root.mainloop()


    def deleteUser(self):
        rowid = self.userTable.selection()[0]
        item = self.userTable.item(rowid)
        data = item['values']
        q = f"delete from review where id ='{data[0]}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo("Success", "Admin has been deleted", parent=self.root)
        self.getValues()

    def getValues(self):
        q = "select userid,recipy_id,rating,view from review"
        self.cr.execute(q)
        result = self.cr.fetchall()
        count = 0
        for row in self.userTable.get_children():
            self.userTable.delete(row)

        for i in result:
            self.userTable.insert("", index=count, values=i)
            count += 1

    def searchUser(self):
        searchTxt = self.searchBox.get()
        q = f"select * from review where rating like '%{searchTxt}%' or view like '%{searchTxt}%' "
        self.cr.execute(q)
        result = self.cr.fetchall()
        count = 0
        for row in self.userTable.get_children():
            self.userTable.delete(row)

        for i in result:
            self.userTable.insert("", index=count, values=i)
            count += 1


# obj= Main()