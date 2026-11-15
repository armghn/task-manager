import datetime
from enum import Enum


class Status(Enum):
    BACKLOG = 1
    TODO = 2
    DOING = 3
    DONE = 4
    BLOCK = 5


class Task:
    def __init__(self, task_id, title, description, status=Status.TODO):
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

    def create_task(self, task_id, title, desc, status=Status.TODO):
        task = Task(task_id, title, desc, status)
        self.add_task(task)

    def display_task(self, task_id):
        task = self.get_task(task_id)
        return f"Title: {task.title},\nDescription: {task.description},\nStatus: {task.status.name},\nCreated_at: {task.created_at}"

    def update_task(self, task_id, title=None, desc=None):
        target_task = self.get_task(task_id)

        if title:
            target_task.title = title

        if desc:
            target_task.description = desc

    def update_status(self, task_id, status):
        task = self.get_task(task_id)
        task.status = status

    def delete_task(self, task_id):
        task = self.get_task(task_id)
        self.tasks.remove(task)


def main():
    task_manager = TaskManager()

    class Switch:
        def case_1(self):
            task_id = int(input("task_id: "))
            title = input("title: ")
            desc = input("description: ")
            stat = input("status (Enter to skip): ")
            if stat:
                stat = Status[stat.upper()]
            else:
                stat = Status.TODO
            task_manager.create_task(task_id, title, desc, stat)

        def case_2(self):
            task_id = int(input("task_id: "))
            title = input("title (Enter to skip):")
            desc = input("description (Enter to skip):")
            task_manager.update_task(task_id, title, desc)

        def case_3(self):
            task_id = int(input("task id: "))
            stat = Status[input("status: ").upper()]
            task_manager.update_status(task_id, stat)

        def case_4(self):
            task_id = int(input("task id: "))
            print(task_manager.display_task(task_id))

        def case_5(self):
            task_id = int(input("task_id: "))
            task_manager.delete_task(task_id)

        def default(self):
            return "unknown"

        def switch(self, value):
            return getattr(self, f"case_{value}", self.default)()

    obj = Switch()

    while True:
        action = int(input(
            "\nchoose an option:\n1.create task\n2.update task\n3.update status\n4.display task\n5.delete task\n6.Exit\n"))
        if action == 6:
            break
        else:
            obj.switch(action)


if __name__ == "__main__":
    main()
