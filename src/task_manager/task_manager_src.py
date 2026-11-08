class Task:
    def __init__(self, task_id, title, description, status="ToDo"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status


class TaskManager:
    def __init__(self):
        self.tasks = []
        self.next_id = 1

    def add_task(self, title, description, status="ToDo"):
        task = Task(title, description, status)
        self.tasks.append(task)
        self.next_id += 1

        # for existing_task in self.tasks:
        #     if task.task_id == existing_task.task_id:
        #         raise ValueError(f"Task ID {task.task_id} already exists!")
        #
        # self.tasks.append(task)










task1 = Task(1, "title1", "desc1")
task2 = Task(2, "title2", "desc2")
task_manager = TaskManager()
task_manager.add_task(task1)
task_manager.add_task(task2)
