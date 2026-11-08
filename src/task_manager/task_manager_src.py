import datetime


class Task:
    def __init__(self, task_id, title, description, status="unchecked"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status
        self.created_at = datetime.datetime.now()


class TaskManager:
    def __init__(self):
        self.tasks = []

    def get_task(self, task_id):
        for task in self.tasks:
            if task.task_id == task_id:
                return task
        raise ValueError(f"There is no task with id {task_id}")

    def add_task(self, task):
        for existing_task in self.tasks:
            if task.task_id == existing_task.task_id:
                raise ValueError(f"Task ID {task.task_id} already exists!")

        self.tasks.append(task)

    def create_task(self, task_id, title, desc, status="unchecked"):
        task = Task(task_id, title, desc, status)
        self.add_task(task)

    def display_task(self, task_id):
        task = self.get_task(task_id)
        return f"Title: {task.title},\nDescription: {task.description},\nStatus: {task.status},\nCreated_at: {task.created_at}"

    def update_task(self, task_id, title=None, desc=None):
        target_task = self.get_task(task_id)

        if title is not None:
            target_task.title = title

        if desc is not None:
            target_task.description = desc

    def update_status(self, task_id, status):
        task = self.get_task(task_id)
        task.status = status

    def delete_task(self, task_id):
        task = self.get_task(task_id)
        self.tasks.remove(task)


task_manager = TaskManager()

task_manager.create_task(1, "title1", "desc1")
task_manager.create_task(2, "title2", "desc2", "checked")

task_manager.update_task(1, title="new_title")
print(task_manager.display_task(1))

task_manager.update_status(2, "unchecked")
print(task_manager.display_task(2))

task_manager.delete_task(1)
