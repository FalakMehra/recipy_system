from tkinter import *
import tkinter.messagebox as msg
import tkinter.ttk as ttk
import connection


class Main:
    def __init__(self):
        self.bgcolour = "#C1C3C1"
        self.conn = connection.Connect()
        self.cr = self.conn.cursor()
        self.root = Tk()
        self.root.state('zoomed')
        self.root.configure(bg=self.bgcolour)
        self.root.title("View Category")
        self.mainLabel = Label(self.root, text="View Category", font=('arial', 26, 'bold'),bg="#6E726E",relief=SUNKEN)
        self.mainLabel.pack(pady=20,ipadx=10,ipady=10)

        self.searchFrame = Frame(self.root,bg="#A1A5A1",width=self.root.winfo_screenwidth())
        self.searchFrame.pack()

        self.searchLabel = Label(self.searchFrame, text="Search By Name", font=('arial', 14),bg="#B6B9B6",foreground="black",activebackground="red",activeforeground="blue")
        self.searchLabel.grid(row=0, column=0, pady=10, padx=10)
        self.searchBox = Entry(self.searchFrame, font=('arial', 14), width=30)
        self.searchBox.grid(row=0, column=1, pady=10, padx=10)
        self.searchBtn = Button(self.searchFrame, font=('arial', 14), text="Search", width=10,
                                command=self.searchCategory,bg="#787D78",foreground="black",activebackground="red",activeforeground="blue")
        self.searchBtn.grid(row=0, column=2, pady=10, padx=10)
        self.refreshBtn = Button(self.searchFrame, font=('arial', 14), text="Refresh", width=10, command=self.getValues,bg="#787D78",foreground="black",activebackground="red",activeforeground="blue")
        self.refreshBtn.grid(row=0, column=3, pady=10, padx=10)

        self.categoryTable = ttk.Treeview(self.root, columns=('name', 'description'))
        self.categoryTable.pack(pady=20, padx=20, expand=True, fill='both')

        self.categoryTable.heading('name', text="Name")

        self.categoryTable.heading('description', text="category description ")

        self.categoryTable['show'] = 'headings'
        self.categoryTable.bind("<Double-1>", self.openUpdateWindow)
        self.getValues()

        self.style = ttk.Style()
        self.style.configure("Treeview", font=('arial', 14), rowheight=40, foreground="black", background="white")
        self.style.configure("Treeview.Heading", font=('arial', 14), foreground="grey")

        self.deleteBtn = Button(self.root, font=('arial', 14), text="Delete", width=10, command=self.deleteCategory,bg="#787D78",foreground="black",activebackground="black",activeforeground="white")
        self.deleteBtn.pack(pady=10)

        self.root.mainloop()

    def openUpdateWindow(self, event):
        self.bgcolour = "#FF9147"
        rowid = self.categoryTable.selection()[0]
        item = self.categoryTable.item(rowid)
        data = item['values']
        print(data)
        self.root1 = Toplevel()
        self.root1.geometry('800x800')
        self.root1.title('Update Category')
        self.root.configure(bg=self.bgcolour)

        self.mainLabel = Label(self.root1, text="Update Category", font=('arial', 20, 'bold'),bg="#6E726E",relief=SUNKEN)
        self.mainLabel.pack(pady=20)

        self.formFrame = Frame(self.root1,bg="#A1A5A1",width=self.root.winfo_screenwidth())
        self.formFrame.pack()
        self.font = ('arial', 14)

        self.lb1 = Label(self.formFrame, text="Enter Name", font=self.font,bg="#A1A5A1",foreground="black")
        self.lb1.grid(row=1, column=0, padx=10, pady=10)
        self.txt1 = Entry(self.formFrame, width=30, font=self.font)
        self.txt1.grid(row=1, column=1, padx=10, pady=10,ipadx=10,ipady=10)
        self.txt1.insert(0, data[0])

        self.lb2 = Label(self.formFrame, text="Select description", font=self.font,bg="#A1A5A1",foreground="black")
        self.lb2.grid(row=4, column=0, padx=10, pady=10)
        self.txt2 = Entry(self.formFrame, width=30, font=self.font)
        self.txt2.grid(row=4, column=1, padx=10, pady=10,ipadx=10,ipady=10)
        self.txt2.insert(0,data[1])

        self.btn = Button(self.root1, text="Update", width=25, font=self.font, command=self.updateCategory,bg="#787D78",foreground="black",activebackground="black",activeforeground="white")
        self.btn.pack(pady=10)

    def updateCategory(self):
        name = self.txt1.get()
        description = self.txt2.get()


        q = f"update category set name='{name}',description='{description}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo('', 'Category has been Updated', parent=self.root1)
        self.root1.destroy()
        self.getValues()

    def deleteCategory(self):
        rowname = self.categoryTable.selection()[0]
        item = self.categoryTable.item(rowname)
        data = item['values']

        q = f"delete from category where name ='{data[0]}'"
        self.cr.execute(q)
        self.conn.commit()
        msg.showinfo("Success", "category has been deleted", parent=self.root)
        self.getValues()

    def getValues(self):
        q = "select name,description from category"
        self.cr.execute(q)
        result = self.cr.fetchall()
        count = 0
        for row in self.categoryTable.get_children():
            self.categoryTable.delete(row)

        for i in result:
            self.categoryTable.insert("", index=count, values=i)
            count += 1

    def searchCategory(self):
        searchTxt = self.searchBox.get()
        q = f"select name,description from category where name like '%{searchTxt}%' or description like '%{searchTxt}%'"
        self.cr.execute(q)
        result = self.cr.fetchall()
        count = 0
        for row in self.categoryTable.get_children():
            self.categoryTable.delete(row)

        for i in result:
            self.categoryTable.insert("", index=count, values=i)
            count += 1


# obj = Main()