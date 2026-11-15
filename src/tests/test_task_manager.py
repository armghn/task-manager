import pytest
from task_manager.task_manager_src import Task
from task_manager.task_manager_src import TaskManager


class TestTask:
    @pytest.fixture
    def manager(self):
        manager = TaskManager()
        manager.tasks = [
            Task(1, "title1", "desc1"),
            Task(2, "title2", "desc2", 4),
            Task(3, "title3", "desc3", 5)
        ]
        return manager

    # def test_task(self):
    #     task = Task(1, "title1", "desc1")
    #     assert (1, "title1", "desc1", 2) == (task.task_id, task.title, task.description, task.status)

    def test_get_task(self, manager):
        task = manager.get_task(1)
        assert task.task_id == 1
        assert task.title == "title1"
        assert task.description == "desc1"

    def test_create_task(self, manager):
        manager.create_task(4, "title4", "desc4")
        task = manager.tasks[-1]
        assert task.task_id == 4
        assert task.title == "title4"
        assert task.description == "desc4"

    def test_update_task(self, manager):
        manager.update_task(3, title="new_title")
        task = manager.tasks[2]
        assert task.task_id == 3
        assert task.title == "new_title"

        manager.update_task(2, desc="new_desc")
        task = manager.tasks[1]
        assert task.task_id == 2
        assert task.description == "new_desc"

    def test_delete_task(self, manager):
        manager.delete_task(1)
        assert len(manager.tasks) == 2
        assert all(task.task_id != 1 for task in manager.tasks)



