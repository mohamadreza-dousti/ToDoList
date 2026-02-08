import customtkinter as ctk
from manageTask.toDoList import ToDoList as tdl

class Ui(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("CREATED BY DOUSTI")
        self.geometry('400x400')

        self.add = ctk.CTkButton(self, text='add task', corner_radius=10, width=100, height=40,
        command=self.AddTask)
        self.add.pack(pady=20)

        self.show = ctk.CTkButton(self, text='show tasks', corner_radius=10, width=100, height=40,
        command=self.ShowTasks)
        self.show.pack(pady=10)

        self.display = ctk.CTkScrollableFrame(self, width=350, height=250,
                                            corner_radius=10)
        self.display.pack(pady=5)
    
    def Back(self, back):
        self.add.configure(state='abled')
        self.show.configure(state='abled')
        back.configure(state='disabled')
        for widget in self.display.winfo_children():
            widget.destroy()
    
    def Refresh(self):
        for widget in self.display.winfo_children():
            widget.destroy()
        self.ShowTasks()



    def AddTask(self):
        newTask = tdl()
        
        self.add.configure(state='disabled')
        self.show.configure(state='disabled')

        title_entry = ctk.CTkEntry(self.display, width=350, height=40, corner_radius=10,
                           placeholder_text='Title')
        title_entry.pack(pady=20)

        description_label = ctk.CTkLabel(self.display, text='description')
        description_label.pack(pady=0)

        text_box = ctk.CTkTextbox(self.display, width=350, height=150, corner_radius=10,
                                border_width=2)
        text_box.pack(pady=10)

        priority = ctk.CTkEntry(self.display, width=350, height=40,corner_radius=10,
                            placeholder_text="priority")
        priority.pack(pady=10)

        save_btn = ctk.CTkButton(self.display, text='Save', command=lambda:newTask.AddTask(title_entry, text_box, priority, save_btn))
        save_btn.pack(pady=10)

        back_btn = ctk.CTkButton(self.display, text='back', command=lambda:self.Back(back_btn))
        back_btn.pack(pady=10)
    
    def ShowTasks(self):
        dirlist = tdl()

        tasks = dirlist.ShowTasks()

        self.add.configure(state='disabled')
        self.show.configure(state='disabled')

        self.display.grid_columnconfigure(0, weight=1)
        self.display.grid_columnconfigure(1, weight=1)
        self.display.grid_columnconfigure(2, weight=1)
        self.display.grid_columnconfigure(3, weight=1)
        self.display.grid_columnconfigure(4, weight=1)

        ctr = 0
        remove_vars = {}
        show_vars = {}
        status_vars = {}
        check_var = {}
        for task in tasks:
            task_label = ctk.CTkLabel(self.display, text=task, width=80)
            task_label.grid(row=ctr, column=0)

            remove_vars[f'remove_btn{ctr}'] = ctk.CTkButton(self.display, text='remove', width=80,
            command=lambda i=ctr : dirlist.Remove(self.display, remove_vars[f'remove_btn{i}'], show_vars[f'show_task{i}']))
            remove_vars[f'remove_btn{ctr}'].grid(row=ctr, column=1)

            show_vars[f'show_task{ctr}'] = ctk.CTkButton(self.display, text='show', width=80,
            command=lambda i=ctr : dirlist.showTask(self.display, show_vars[f'show_task{i}']))
            show_vars[f'show_task{ctr}'].grid(row=ctr, column=2)

            check_var[f'var{ctr}'] = ctk.StringVar(value='No')
            status_vars[f'status{ctr}'] = ctk.CTkCheckBox(self.display, text='DONE', variable=check_var[f'var{ctr}'], offvalue='No', onvalue='Yes',
                                                          command=lambda i=ctr : dirlist.set(status_vars[f'status{i}'], self.display))
            status_vars[f'status{ctr}'].grid(row=ctr, column=3, padx=2)
            dirlist.status(status_vars[f'status{ctr}'], self.display, check_var[f'var{ctr}'])

            ctr += 1

        back_btn = ctk.CTkButton(self.display, text='back', command=lambda:self.Back(back_btn))
        back_btn.grid(row=ctr,column=0, columnspan=2, pady=15)

        refresh_btn = ctk.CTkButton(self.display, text='refresh🔄️', command=self.Refresh)
        refresh_btn.grid(row=ctr, column=3, columnspan=2)

