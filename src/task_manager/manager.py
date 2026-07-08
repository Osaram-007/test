from typing import List, Optional
from .models import Task
from .storage import StorageHandler

class TaskManager:
    def __init__(self, storage_path: str):
        self.storage = StorageHandler(storage_path)
        self.tasks = self.storage.load_tasks()

    def _get_next_id(self) -> int:
        if not self.tasks:
            return 1
        return max(task.id for task in self.tasks) + 1

    def add_task(self, title: str) -> Task:
        if not title.strip():
            raise ValueError("Task title cannot be empty.")
        
        task = Task(id=self._get_next_id(), title=title.strip())
        self.tasks.append(task)
        self.storage.save_tasks(self.tasks)
        return task

    def list_tasks(self) -> List[Task]:
        return self.tasks

    def get_task(self, task_id: int) -> Optional[Task]:
        for task in self.tasks:
            if task.id == task_id:
                return task
        return None

    def complete_task(self, task_id: int) -> bool:
        task = self.get_task(task_id)
        if task:
            task.completed = True
            self.storage.save_tasks(self.tasks)
            return True
        return False

    def delete_task(self, task_id: int) -> bool:
        task = self.get_task(task_id)
        if task:
            self.tasks.remove(task)
            self.storage.save_tasks(self.tasks)
            return True
        return False
