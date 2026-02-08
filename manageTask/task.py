import customtkinter as ctk
import json

class Task():
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority
        self.check_var = ctk.StringVar(value='No')

    def CreateTask(self):
        file_name = f'{self.name}.txt'
        with open(f'manageTask/tasks_folder/{file_name}', "a+") as file:
            file.write(self.description)
        file_name_state = f'manageTask/status_setting/{self.name}.json'
        data = {
            "status" : self.check_var.get(),
            "priority":self.priority
        }
        with open(file_name_state, "w") as f:
            json.dump(data, f)
            