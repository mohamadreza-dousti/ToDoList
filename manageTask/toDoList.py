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





