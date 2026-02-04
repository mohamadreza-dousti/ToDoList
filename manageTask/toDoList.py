import os
from .task import Task

class ToDoList():
    def AddTask(self, name, description, priority, save_btn):
        title = name.get()
        text = description.get(1.0, 'end')
        priority =priority.get()

        newTask = Task(title, text, priority)
        newTask.CreateTask()
        save_btn.configure(state='disabled', fg_color='green', text='saved!')

    def ShowTasks(self):
        path = 'manageTask/tasks_folder'
        tasks = os.listdir(path)
        return tasks
    
    def Remove(self, frame, btn, s_btn):
        row = btn.grid_info()['row']
        name = frame.grid_slaves(row=row, column=0)
        name = name[0].cget('text')
        btn.configure(text='removed', state='disabled')
        s_btn.configure(state='disabled')
        os.system(f'del manageTask\\tasks_folder\{name}')
    

    def showTask(self, frame, btn):
        row = btn.grid_info()["row"]
        name = frame.grid_slaves(row=row, column=0)
        name = name[0].cget('text')
        os.system(f"manageTask\\tasks_folder\{name}")







