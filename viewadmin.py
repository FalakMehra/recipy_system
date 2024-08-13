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


         self.root.title("View Admin")
         self.mainLabel = Label(self.root, text="View Admin", font=('arial', 26, 'bold'),bg="#6E726E",relief=SUNKEN)
         self.mainLabel.pack(pady=20,ipadx=10,ipady=10)

         self.searchFrame = Frame(self.root,bg="#A1A5A1",width=self.root.winfo_screenwidth())
         self.searchFrame.pack()

         self.searchLabel = Label(self.searchFrame, text="Search By Name, Email, Mobile", font=('arial', 14),bg="#A1A5A1",foreground="black",activebackground="red",activeforeground="blue")
         self.searchLabel.grid(row=0, column=0, pady=10,padx=10)
         self.searchBox = Entry(self.searchFrame, font=('arial', 14), width=30)
         self.searchBox.grid(row=0, column=1, pady=10, padx=10)
         self.searchBtn = Button(self.searchFrame, font=('arial', 14), text="Search", width=10, command=self.searchAdmin,bg="#787D78",foreground="black",activebackground="red",activeforeground="blue")
         self.searchBtn.grid(row=0, column=2, pady=10, padx=10)
         self.refreshBtn = Button(self.searchFrame, font=('arial', 14), text="Refresh", width=10, command=self.getValues,bg="#787D78",foreground="black",activebackground="red",activeforeground="blue")
         self.refreshBtn.grid(row=0, column=3, pady=10, padx=10)


         self.adminTable = ttk.Treeview(self.root, columns=('id', 'name','email', 'mobile', 'role'))
         self.adminTable.pack(pady=20, padx=20,expand=True, fill='both')

         self.adminTable.heading('id', text="ID")
         self.adminTable.heading('name', text="Name")
         self.adminTable.heading('email', text="Email")
         self.adminTable.heading('mobile', text="Mobile")
         self.adminTable.heading('role', text="Admin Role (Type)")

         self.adminTable['show'] = 'headings'
         self.adminTable.bind("<Double-1>", self.openUpdateWindow)
         self.getValues()

         self.style = ttk.Style()
         self.style.configure('Treeview', font=('arial', 20), rowheight=40, foreground="black", background="white")
         self.style.configure('Treeview.Heading', font=('arial', 23), rowheight=40, foreground="grey")

         self.deleteBtn = Button(self.root, font=('arial', 14), text="Delete", width=10, command=self.deleteAdmin,bg="#787D78",foreground="black",activebackground="red",activeforeground="blue")
         self.deleteBtn.pack(pady=10)

         self.root.mainloop()


     def openUpdateWindow(self,event):
         self.bgcolour = "#C1C3C1"
         rowid = self.adminTable.selection()[0]
         item = self.adminTable.item(rowid)
         data = item['values']
         print(data)
         self.root1 = Toplevel()
         self.root1.geometry('800x800')

         self.root1.title('Update Admin')
         self.root.configure(bg=self.bgcolour)

         self.mainLabel = Label(self.root1, text="Update Admin", font=('arial', 20, 'bold'),bg="#6E726E",relief=SUNKEN)
         self.mainLabel.pack(pady=20)

         self.formFrame = Frame(self.root1,bg="#A1A5A1",width=self.root.winfo_screenwidth())

         self.formFrame.pack()
         self.font = ('arial', 14)

         self.lb1 = Label(self.formFrame, text="Admin ID", font=self.font,bg="#A1A5A1",foreground="black")
         self.lb1.grid(row=0, column=0, padx=10, pady=10)
         self.txt1 = Entry(self.formFrame, width=30, font=self.font)
         self.txt1.grid(row=0, column=1, padx=10, pady=10,ipadx=10,ipady=10)
         self.txt1.insert(0, data[0])
         self.txt1.configure(state="readonly")

         self.lb2 = Label(self.formFrame, text="Enter Name", font=self.font,bg="#A1A5A1",foreground="black")
         self.lb2.grid(row=1, column=0, padx=10, pady=10)
         self.txt2 = Entry(self.formFrame, width=30, font=self.font)
         self.txt2.grid(row=1, column=1, padx=10, pady=10,ipadx=10,ipady=10)
         self.txt2.insert(0, data[1])

         self.lb3 = Label(self.formFrame, text="Enter Email", font=self.font,bg="#A1A5A1",foreground="black")
         self.lb3.grid(row=2, column=0, padx=10, pady=10)
         self.txt3 = Entry(self.formFrame, width=30, font=self.font)
         self.txt3.grid(row=2, column=1, padx=10, pady=10,ipadx=10,ipady=10)
         self.txt3.insert(0, data[2])

         self.lb4 = Label(self.formFrame, text="Enter Mobile", font=self.font,bg="#A1A5A1",foreground="black")
         self.lb4.grid(row=3, column=0, padx=10, pady=10)
         self.txt4 = Entry(self.formFrame, width=30, font=self.font)
         self.txt4.grid(row=3, column=1, padx=10, pady=10,ipadx=10,ipady=10)
         self.txt4.insert(0, data[3])

         self.lb5 = Label(self.formFrame, text="Select Role", font=self.font,bg="#A1A5A1",foreground="black")
         self.lb5.grid(row=4, column=0, padx=10, pady=10)
         self.txt5 = ttk.Combobox(self.formFrame, width=29, font=self.font, values=['Super Admin', "Admin"],
                                  state='readonly')
         self.txt5.grid(row=4, column=1, padx=10, pady=10,ipadx=10,ipady=10)
         self.txt5.set(data[4])

         self.btn = Button(self.root1, text="Update", width=25, font=self.font,bg="#787D78",foreground="black",activebackground="black",activeforeground="white", command=self.updateAdmin)
         self.btn.pack(pady=10)

     def updateAdmin(self):
         id = self.txt1.get()
         name = self.txt2.get()
         email = self.txt3.get()
         mobile = self.txt4.get()
         role = self.txt5.get()

         q = f"update admin set name='{name}', email='{email}',mobile='{mobile}',role='{role}' where id='{id}'"
         self.cr.execute(q)
         self.conn.commit()
         msg.showinfo('', 'Admin has been Updated',parent=self.root1)
         self.root1.destroy()
         self.getValues()

     def deleteAdmin(self):
         rowid = self.adminTable.selection()[0]
         item = self.adminTable.item(rowid)
         data = item['values']
         # print(data)

         q = f"delete from admin where id ='{data[0]}'"
         self.cr.execute(q)
         self.conn.commit()
         msg.showinfo("Success", "Admin has been deleted", parent=self.root)
         self.getValues()


     def getValues(self):
          q = "select id,name,email,mobile,role from admin"
          self.cr.execute(q)
          result = self.cr.fetchall()
          count = 0
          for row in self.adminTable.get_children():
               self.adminTable.delete(row)

          for i in result:
               self.adminTable.insert("", index=count, values=i)
               count += 1

     def searchAdmin(self):
          searchTxt = self.searchBox.get()
          q = f"select id,name,email,mobile,role from admin where name like '%{searchTxt}%' or email like '%{searchTxt}%' or mobile like '%{searchTxt}%'"
          self.cr.execute(q)
          result = self.cr.fetchall()
          count = 0
          for row in self.adminTable.get_children():
              self.adminTable.delete(row)

          for i in result:
              self.adminTable.insert("", index=count, values=i)
              count += 1
# obj=Main()