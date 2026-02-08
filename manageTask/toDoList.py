import os
from .task import Task
import json

class ToDoList():
    def AddTask(self, name, description, priority, save_btn):
        title = name.get()
        text = description.get(1.0, 'end')
        priority = priority.get()
        self.task = Task(title, text, priority)
        self.task.CreateTask()
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
        os.system(f'del manageTask\\status_setting\{name[0:-4]}.json')
    

    def showTask(self, frame, btn):
        row = btn.grid_info()["row"]
        name = frame.grid_slaves(row=row, column=0)
        name = name[0].cget('text')
        os.system(f"manageTask\\tasks_folder\{name}")
    
    def status(self, var, frame, c):
        row = var.grid_info()['row']
        name = frame.grid_slaves(row=row, column=0)
        name = name[0].cget('text')
        self.load_check_var(name[0:-4], c)
    
    def set(self, var, frame):
        row = var.grid_info()['row']
        name = frame.grid_slaves(row=row, column=0)
        name = name[0].cget('text')
        self.set_var(var, name[0:-4])

    def load_check_var(self, name, var):
        file_name = f'manageTask/status_setting/{name}.json'
        if os.path.exists(file_name):
            with open(file_name, "r") as f:
                data = json.load(f)
            var.set(data['status'])

    def set_var(self, var, name):
        file_name = f'manageTask/status_setting/{name}.json'
        data = {
            "status" : var.get()
        }
        with open(file_name, "w") as f:
            json.dump(data, f)







