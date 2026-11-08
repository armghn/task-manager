class Task:
    def __init__(self, task_id, title, description, status="ToDo"):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.status = status


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

    def display_task(self, task_id):
        task = self.get_task(task_id)
        return f"Title: {task.title},\nDescription: {task.description},\nStatus: {task.status}"

    def update_task(self, task_id, title=None, desc=None):
        target_task = self.get_task(task_id)

        if title is not None:
            target_task.title = title

        if desc is not None:
            target_task.description = desc

    def update_status(self, task_id, status):
        task = self.get_task(task_id)
        task.status = status



task1 = Task(1, "title1", "desc1")
task2 = Task(2, "title2", "desc2")

task_manager = TaskManager()

task_manager.add_task(task1)
task_manager.add_task(task2)

print(task_manager.display_task(1))

task_manager.update_task(1, title="new_title")
print(task_manager.display_task(1))

