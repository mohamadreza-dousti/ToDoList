class Task():
    def __init__(self, name, description, priority):
        self.name = name
        self.description = description
        self.priority = priority

    def CreateTask(self):
        file_name = f'{self.name}.txt'
        with open(f'manageTask/tasks_folder/{file_name}', "a+") as file:
            file.write(f'priority : {self.priority}\n')
            file.write(self.description)

