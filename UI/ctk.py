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

        ctr = 0
        for task in tasks:
            task_label = ctk.CTkLabel(self.display, text=task, width=80)
            task_label.grid(row=ctr, column=0)

            remove_btn = ctk.CTkButton(self.display, text='remove', width=80)
            remove_btn.grid(row=ctr, column=1)

            show_task = ctk.CTkButton(self.display, text='show', width=80)
            show_task.grid(row=ctr, column=2)

            ctr += 1

        back_btn = ctk.CTkButton(self.display, text='back', command=lambda:self.Back(back_btn))
        back_btn.grid(row=ctr,column=0, columnspan=3, pady=15)

